"""
PPP namespace module
"""
from ._base import Namespace, Method


class PPP(Namespace):
    """
    PPP API namespace definition
    """
    __namespace__ = 'ppp'
    get_credentials = Method('getCredentials')
    get_info = Method('getInfo')
    # TODO: set_credentials = Method('setCredentials')
