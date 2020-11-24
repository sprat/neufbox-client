"""
Wan namespace module
"""
from ._base import Namespace, Method


class Wan(Namespace):
    """
    Wan API namespace definition
    """
    __namespace__ = 'wan'
    get_info = Method('getInfo')
