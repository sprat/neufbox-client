"""
SFR Box API Client
"""
from setuptools import setup


setup(
    name='sfrbox-client',
    description='SFR Box API Client',
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'requests',
        'xmltodict'
    ],
    packages=[
        'sfrbox'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-pylint',
            'requests-mock'
        ],
    }
)
