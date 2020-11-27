"""
System namespace module
"""
from ._base import Namespace, GetMethod, PostMethod


class System(Namespace):
    """
    System API namespace definition
    """
    __namespace__ = 'system'
    get_info = GetMethod('getInfo')
    get_if_list = GetMethod('getIfList')
    get_wpa_key = GetMethod('getWpaKey')
    reboot = PostMethod('reboot')
    set_net_mode = PostMethod('setNetMode', params=['mode'])
    set_ref_client = PostMethod('setRefClient', params=['refclient'])
