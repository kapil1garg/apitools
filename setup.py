#!/usr/bin/env python
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup configuration."""

import platform

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    import setuptools

# Configure the required packages and scripts to install, depending on
# Python version and OS.
REQUIRED_PACKAGES = [
    'httplib2>=0.8',
    'oauth2client>=1.5.2',
    'setuptools>=18.5',
    'six>=1.9.0',
    ]

CLI_PACKAGES = [
    'google-apputils>=0.4.0',
    'python-gflags>=2.0',
]

TESTING_PACKAGES = [
    'google-apputils>=0.4.0',
    'unittest2>=0.5.1',
    'mock>=1.0.1',
]

CONSOLE_SCRIPTS = [
    'gen_client = apitools.gen.gen_client:main',
    'oauth2l = apitools.scripts.oauth2l:run_main [cli]',
]

py_version = platform.python_version()

if py_version < '2.7':
    REQUIRED_PACKAGES.append('argparse>=1.2.1')

_APITOOLS_VERSION = '0.4.14'

with open('README.rst') as fileobj:
    README = fileobj.read()

setuptools.setup(
    name='google-apitools',
    version=_APITOOLS_VERSION,
    description='client libraries for humans',
    long_description=README,
    url='http://github.com/craigcitro/apitools',
    author='Craig Citro',
    author_email='craigcitro@google.com',
    # Contained modules and scripts.
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
        },
    install_requires=REQUIRED_PACKAGES,
    tests_require=REQUIRED_PACKAGES + CLI_PACKAGES + TESTING_PACKAGES,
    extras_require={
        'cli': CLI_PACKAGES,
        'testing': TESTING_PACKAGES,
        },
    # Add in any packaged data.
    include_package_data=True,
    package_data={
        'apitools.data': ['*'],
    },
    # PyPI package information.
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    license='Apache 2.0',
    keywords='apitools',
    )
