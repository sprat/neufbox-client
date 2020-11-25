"""
Wan namespace module
"""
from ._base import Namespace, GetMethod


class Wan(Namespace):
    """
    Wan API namespace definition
    """
    __namespace__ = 'wan'
    get_info = GetMethod('getInfo')
