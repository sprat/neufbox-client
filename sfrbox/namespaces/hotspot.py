"""
Hotspot namespace module
"""
from ._base import Namespace, GetMethod, PostMethod


class Hotspot(Namespace):
    """
    Hotspot API namespace definition
    """
    __namespace__ = 'hotspot'
    enable = PostMethod('enable')
    disable = PostMethod('disable')
    get_client_list = GetMethod('getClientList')
    get_info = GetMethod('getInfo')
    set_mode = PostMethod('setMode', params=['mode'])
    restart = PostMethod('restart')
    start = PostMethod('start')
    stop = PostMethod('stop')
