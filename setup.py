"""
SFR Box API Client
"""
from setuptools import setup


setup(
    name='sfrbox-client',
    description='SFR Box API Client',
    license='MIT License',
    keywords='sfr, box, api, client',
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
            'python-dotenv',
            'pytest',
            'pytest-pylint',
            'requests-mock'
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
