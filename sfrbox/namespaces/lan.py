"""
Lan namespace module
"""
from ._base import Namespace, GetMethod, PostMethod


class Lan(Namespace):
    """
    Lan API namespace definition
    """
    __namespace__ = 'lan'
    add_dns_host = PostMethod('addDnsHost', params=['ip', 'name'])
    delete_dns_host = PostMethod('deleteDnsHost', params=['ip', 'name'])
    get_dns_host_list = GetMethod('getDnsHostList')
    get_hosts_list = GetMethod('getHostsList')
    get_info = GetMethod('getInfo')
