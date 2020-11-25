"""
Lan namespace module
"""
from ._base import Namespace, GetMethod


class Lan(Namespace):
    """
    Lan API namespace definition
    """
    __namespace__ = 'lan'
    get_info = GetMethod('getInfo')
    get_hosts_list = GetMethod('getHostsList')
