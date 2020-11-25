"""
Client module
"""
import hashlib
import hmac
import requests
import xmltodict

from .property import NamespaceProperty
from .namespaces import Auth, Lan, PPP, Wan


class ClientError(Exception):
    """SFR Box API Error"""

    def __init__(self, code, message):
        self.code = code
        super().__init__(message)


# TODO: handle post routes
# TODO: complete the API namespaces
class Client:
    """
    SFR Box API client
    See https://lafibre.info/sfr-les-news/spec-api-rest-box-de-sfr/?action=dlattach;attach=85818
    """

    # namespaces
    auth = NamespaceProperty(Auth)
    lan = NamespaceProperty(Lan)
    ppp = NamespaceProperty(PPP)
    wan = NamespaceProperty(Wan)

    def __init__(self, hostname):
        self.hostname = hostname
        self._session = requests.Session()
        self._token = None

    @property
    def api_url(self):
        """Return the API url"""
        return f'http://{self.hostname}/api/1.0'

    def login(self, auth_callback):
        """Login: this creates an authentication token that can be used to access
        the private methods. An authentication callback should be provided: it will
        be called with the requested authentication method (passwd / button / all),
        and should return either a username/password tuple (for password authentication),
        or None (for push-button authentication), after the user has taken action."""
        # ask for a token
        msg = self.auth.get_token()
        token = msg['token']
        method = msg['method']

        # prompt for username/password or wait until button pushed
        credentials = auth_callback(method)

        # compute hashed password if password provided
        hash_value = None
        if credentials:
            username, password = credentials
            username_hash = self._compute_hash(token, username)
            password_hash = self._compute_hash(token, password)
            hash_value = username_hash + password_hash

        # check authentication, which makes the token eventually valid
        result = self.auth.check_token(token=token, hash=hash_value)
        self._token = result['token']

    def logout(self):
        """Logout: forget the current token"""
        self._token = None

    def get(self, method, **parameters):
        """Perform a GET request with a fully qualified method"""
        params = {'method': method}
        if self._token:
            params['token'] = self._token
        params.update(parameters)
        response = self._session.get(self.api_url, params=params)
        return self._process_response(response)

    @staticmethod
    def _compute_hash(token, value):
        """Compute a password hash for a given token"""
        token_bytes = token.encode('ascii')
        value_bytes = value.encode('ascii')
        value_hash_bytes = hashlib.sha256(value_bytes).hexdigest().encode('ascii')
        return hmac.new(token_bytes, value_hash_bytes, hashlib.sha256).hexdigest()

    @staticmethod
    def _process_response(response):
        """Process the API response"""
        response.raise_for_status()

        payload = xmltodict.parse(
            response.text,
            dict_constructor=dict,
            attr_prefix='',
            postprocessor=_value_postprocessor
        )['rsp']

        status = payload.pop('stat')
        payload.pop('version', None)
        if status == 'ok':
            return next(iter(payload.values()))  # get the value of the remaining key

        error = payload['err']
        raise ClientError(error['code'], error['msg'])


def _value_postprocessor(_, key, value):
    """Post-process the string values parsed from the XML"""
    try:
        return key, int(value)
    except (ValueError, TypeError):
        return key, value
