"""
Auth module
"""


def username_password(username, password):
    """Authenticate with username/password"""
    def get(method):
        if method in ('passwd', 'all'):
            return (username, password)
        return None

    return get
