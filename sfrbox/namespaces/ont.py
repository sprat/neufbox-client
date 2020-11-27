"""
ONT namespace module
"""
from ._base import Namespace, GetMethod, PostMethod


class ONT(Namespace):
    """
    ONT API namespace definition
    """
    __namespace__ = 'ont'
    get_info = GetMethod('getInfo')
    sync = PostMethod('sync')
    push = PostMethod('push', params=['name', 'value'], optional_params=['force'])
    pull = GetMethod('pull')
