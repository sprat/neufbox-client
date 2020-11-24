"""
Lan namespace module
"""
from ._base import Namespace, Method


class Lan(Namespace):
    """
    Lan API namespace definition
    """
    __namespace__ = 'lan'
    get_info = Method('getInfo')
    get_hosts_list = Method('getHostsList')
