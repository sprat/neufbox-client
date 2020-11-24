"""
Namespace base module
"""
from abc import ABC
from functools import partial


class Namespace(ABC):
    """
    API namespace definition
    """
    __namespace__ = ''

    def __init__(self, client):
        self.client = client

    def call_method(self, method, **kwargs):
        """Execute a method in a namespace"""
        method_name = f'{self.__namespace__}.{method.name}'
        return self.client.get(method_name, **kwargs)


class Method:
    """
    API method definition
    """
    def __init__(self, name, params = None):
        self.name = name
        self.params = params or []

    def __get__(self, namespace, objtype = None):
        return partial(namespace.call_method, self)
