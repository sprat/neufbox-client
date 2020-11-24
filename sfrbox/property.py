"""
Property module
"""


class NamespaceProperty:
    """
    Descriptor that creates a Namespace instance when the associated property is accessed on the
    Client instance
    """
    def __init__(self, namespace_factory):
        self.namespace_factory = namespace_factory

    def __get__(self, client, client_type=None):
        return self.namespace_factory(client)
