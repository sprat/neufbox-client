"""
Test script
"""
import os
from pprint import pprint
from dotenv import load_dotenv
from sfrbox import Client, username_password


def main():
    """Main program"""
    load_dotenv()
    hostname = os.getenv('SFRBOX_HOSTNAME')
    username = os.getenv('SFRBOX_USERNAME')
    password = os.getenv('SFRBOX_PASSWORD')

    client = Client(hostname)
    client.login(username_password(username, password))

    print('LAN info:')
    pprint(client.lan.get_info())

    print('WAN info:')
    pprint(client.wan.get_info())


if __name__ == '__main__':
    main()
