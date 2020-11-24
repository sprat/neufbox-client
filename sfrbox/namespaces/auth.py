"""
Auth namespace module
"""
from ._base import Namespace, Method


class Auth(Namespace):
    """
    Auth API namespace definition
    """
    __namespace__ = 'auth'
    get_token = Method('getToken')
    check_token = Method('checkToken', params=['token', 'hash'])
