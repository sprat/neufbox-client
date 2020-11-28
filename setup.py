"""
Neufbox API Client
"""
from setuptools import setup


setup(
    name='neufbox-client',
    description='Neufbox API Client',
    license='MIT License',
    keywords='neuf, sfr, redbysfr, box, api, client',
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'requests',
        'xmltodict'
    ],
    packages=[
        'neufbox'
    ],
    extras_require={
        'test': [
            'python-dotenv',
            'pytest',
            'pytest-cov',
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
