"""
Auth namespace module
"""
from ._base import Namespace, GetMethod


class Auth(Namespace):
    """
    Auth API namespace definition
    """
    __namespace__ = 'auth'
    get_token = GetMethod('getToken')
    check_token = GetMethod('checkToken', params=['token', 'hash'])
