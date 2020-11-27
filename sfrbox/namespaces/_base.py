"""
Namespace base module
"""
from abc import ABC
from functools import partial


class Namespace(ABC):
    """
    API namespace definition. Should be subclassed to define concrete namespaces
    """
    __namespace__ = ''

    def __init__(self, client):
        self.client = client

    @classmethod
    def binding(cls):
        """Returns a descriptor that creates the namespace instance when the property is accessed"""
        return _Binding(cls)


class Method(ABC):
    """
    Abstract API method definition
    """

    _client_method = ''

    def __init__(self, name, params=None, optional_params=None):
        self.name = name
        self.params = params or []
        self.optional_params = optional_params or []

    def _call(self, namespace, **kwargs):
        qualified_name = f'{namespace.__namespace__}.{self.name}'
        client_method = getattr(namespace.client, self._client_method)
        return client_method(qualified_name, **kwargs)

    def __get__(self, namespace, objtype = None):
        return partial(self._call, namespace)


class GetMethod(Method):
    """API GET method definition"""

    _client_method = 'get'


class PostMethod(Method):
    """API POST method definition"""

    _client_method = 'post'


class _Binding:
    """
    Creates a Namespace instance when the associated property is accessed on the Client instance
    """
    def __init__(self, namespace_factory):
        self.namespace_factory = namespace_factory

    def __get__(self, client, client_type=None):
        return self.namespace_factory(client)
