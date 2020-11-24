"""
Client tests
"""
from sfrbox import Client


LAN_GET_INFO = """\
<?xml version="1.0" ?>
<rsp stat="ok">
      <lan ip_addr="192.168.1.1" netmask="255.255.255.0" dhcp_active="on" dhcp_start="192.168.1.20" dhcp_end="192.168.1.100" dhcp_lease="86400" />
</rsp>
"""


def test_compute_hash():
    """Test that the hash computation match the example specified in the documentation"""
    result = Client._compute_hash('43f6168e635b9a90774cc4d3212d5703c11c9302', 'admin')  # pylint: disable=protected-access
    assert result == '7aa3e8b3ed7dfd7796800b4c4c67a0c56c5e4a66502155c17a7bcef5ae945ffa'


def test_lan_get_info(requests_mock):
    """Test that client.lan.get_info() returns a properly formatted dict"""
    requests_mock.get('http://192.168.1.1/api/1.0?method=lan.getInfo', text=LAN_GET_INFO)

    client = Client('192.168.1.1')
    result = client.lan.get_info()
    assert result == {
        'ip_addr': '192.168.1.1',
        'netmask': '255.255.255.0',
        'dhcp_active': 'on',
        'dhcp_start': '192.168.1.20',
        'dhcp_end': '192.168.1.100',
        'dhcp_lease': 86400
    }
