"""
SFR Box Root module
"""
from .client import Client, ClientError
from .auth import username_password


__all__ = ['Client', 'ClientError', 'username_password']
