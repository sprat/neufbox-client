"""
Neufbox API Client
"""
from setuptools import setup


with open('README.md', 'r') as readme_file:
    LONG_DESCRIPTION = readme_file.read()


setup(
    name='neufbox-client',
    description='Neufbox API Client',
    author='Sylvain Prat',
    author_email='sylvain.prat+neufbox-client@gmail.com',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license='MIT License',
    keywords='neuf, sfr, redbysfr, box, api, client',
    url='https://github.com/sprat/neufbox-client',
    download_url='https://pypi.python.org/pypi/neufbox-client',
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
    python_requires='>=3.0',
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
