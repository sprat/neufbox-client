"""
PPP namespace module
"""
from ._base import Namespace, GetMethod


class PPP(Namespace):
    """
    PPP API namespace definition
    """
    __namespace__ = 'ppp'
    get_credentials = GetMethod('getCredentials')
    get_info = GetMethod('getInfo')
    # TODO: set_credentials = PostMethod('setCredentials')
