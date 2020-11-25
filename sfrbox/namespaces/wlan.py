"""
WLAN namespace module
"""
from ._base import Namespace, GetMethod, PostMethod


class WLAN(Namespace):
    """
    WLAN API namespace definition
    """
    __namespace__ = 'wlan'
    enable = PostMethod('enable')
    disable = PostMethod('disable')
    get_client_list = GetMethod('getClientList')
    get_info = GetMethod('getInfo')
    get_scan_list = GetMethod('getScanList')
    set_channel = PostMethod('setChannel', params=['channel'])
    set_wl0_enc = PostMethod('setWl0Enc', params=['enc'])
    set_wl0_enc_type = PostMethod('setWl0Enctype', params=['enctype'])
    set_wl0_key_type = PostMethod('setWl0Keytype', params=['keytype'])
    set_wl0_ssid = PostMethod('setWl0Ssid', params=['ssid'])
    set_wl0_wpa_key = PostMethod('setWl0Wpakey', params=['wpakey'])
    set_wlan_mode = PostMethod('setWlanMode', params=['mode'])
    start = PostMethod('start')
    stop = PostMethod('stop')
    restart = PostMethod('restart')
