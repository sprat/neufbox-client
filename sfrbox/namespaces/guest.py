"""
Guest namespace module
"""
from ._base import Namespace, GetMethod, PostMethod


class Guest(Namespace):
    """
    Guest API namespace definition
    """
    __namespace__ = 'guest'
    get_info = GetMethod('getInfo')
    enable = PostMethod('enable')
    disable = PostMethod('disable')
    set_ssid = PostMethod('setSsid', params=['ssid'])
    set_wpa_key = PostMethod('setWpakey', params=['wpakey'])
