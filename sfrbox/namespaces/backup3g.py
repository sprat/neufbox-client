"""
Backup3g namespace module
"""
from ._base import Namespace, GetMethod, PostMethod


class Backup3g(Namespace):
    """
    Backup3g API namespace definition
    """
    __namespace__ = 'backup3g'
    force_data_link = PostMethod('forceDataLink', params=['mode'])
    force_voip_link = PostMethod('forceVoipLink', params=['mode'])
    get_pin_code = GetMethod('getPinCode')
    set_pin_code = PostMethod('setPinCode', params=['pincode'])
