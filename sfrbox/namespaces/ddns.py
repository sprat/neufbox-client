"""
DDNS namespace module
"""
from ._base import Namespace, GetMethod, PostMethod


class DDNS(Namespace):
    """
    DDNS API namespace definition
    """
    __namespace__ = 'ddns'
    disable = PostMethod('disable')
    enable = PostMethod('enable')
    force_update = PostMethod('forceUpdate')
    get_info = GetMethod('getInfo')
    set_service = PostMethod('setService', params=['service', 'username', 'password', 'hostname'])
    # service: (dyndns|no-ip|ovh|dyndnsit|changeip|sitelutions)
