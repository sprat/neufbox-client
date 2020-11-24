"""
Client module
"""
import hashlib
import hmac
import requests
import xmltodict

from .property import NamespaceProperty
from .namespaces import Auth, Wan, Lan


# TODO: add authentication
# TODO: handle post routes
# TODO: complete the API namespaces
class Client:
    """
    SFR Box API client
    See https://lafibre.info/sfr-les-news/spec-api-rest-box-de-sfr/?action=dlattach;attach=85818
    """
    # namespaces...
    auth = NamespaceProperty(Auth)
    wan = NamespaceProperty(Wan)
    lan = NamespaceProperty(Lan)

    def __init__(self, hostname):
        self.hostname = hostname
        self._session = requests.Session()

    @property
    def api_url(self):
        """Return the API url"""
        return f'http://{self.hostname}/api/1.0'

    def get(self, method, **parameters):
        """Perform a GET request with a fully qualified method"""
        response = self._session.get(self.api_url, params=dict(
            method=method,
            **parameters
        ))
        return self._process_response(response)

    @staticmethod
    def _compute_hash(token, password):
        """Compute a password hash for a given token"""
        token_bytes = token.encode('ascii')
        password_bytes = password.encode('ascii')
        password_hash_bytes = hashlib.sha256(password_bytes).hexdigest().encode('ascii')
        return hmac.new(token_bytes, password_hash_bytes, hashlib.sha256).hexdigest()

    @staticmethod
    def _process_response(response):
        """Process the API response"""
        response.raise_for_status()

        result = xmltodict.parse(
            response.text,
            dict_constructor=dict,
            attr_prefix='',
            postprocessor=_value_postprocessor
        )['rsp']

        status = result.pop('stat')
        result.pop('version', None)
        if status == 'ok':
            return next(iter(result.values()))  # get the value of the remaining key
        raise result['err']


def _value_postprocessor(_, key, value):
    """Post-process the string values parsed from the XML"""
    try:
        return key, int(value)
    except (ValueError, TypeError):
        return key, value
