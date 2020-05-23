#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import codecs
import os
import re
import sys

import pkg_resources
from setuptools import find_packages
from setuptools import setup


def read(*parts):
    path = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(path, encoding='utf-8') as fobj:
        return fobj.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


install_requires = [
    'cached-property >= 1.2.0, < 2',
    'docopt >= 0.6.1, < 1',
    'PyYAML >= 3.10, < 6',
    'requests >= 2.20.0, < 3',
    'texttable >= 0.9.0, < 2',
    'websocket-client >= 0.32.0, < 1',
    'distro >= 1.5.0, < 2',
    'docker[ssh] >= 3.7.0, < 5',
    'dockerpty >= 0.4.1, < 1',
    'six >= 1.3.0, < 2',
    'jsonschema >= 2.5.1, < 4',
    'python-dotenv >= 0.13.0, < 1',
]


tests_require = [
    'ddt >= 1.2.2, < 2',
    'pytest < 6',
]


if sys.version_info[:2] < (3, 4):
    tests_require.append('mock >= 1.0.1, < 4')

extras_require = {
    ':python_version < "3.2"': ['subprocess32 >= 3.5.4, < 4'],
    ':python_version < "3.4"': ['enum34 >= 1.0.4, < 2'],
    ':python_version < "3.5"': ['backports.ssl_match_hostname >= 3.5, < 4'],
    ':python_version < "3.3"': ['backports.shutil_get_terminal_size == 1.0.0',
                                'ipaddress >= 1.0.16, < 2'],
    ':sys_platform == "win32"': ['colorama >= 0.4, < 1'],
    'socks': ['PySocks >= 1.5.6, != 1.5.7, < 2'],
    'tests': tests_require,
}


try:
    if 'bdist_wheel' not in sys.argv:
        for key, value in extras_require.items():
            if key.startswith(':') and pkg_resources.evaluate_marker(key[1:]):
                install_requires.extend(value)
except Exception as e:
    print("Failed to compute platform dependencies: {}. ".format(e) +
          "All dependencies will be installed as a result.", file=sys.stderr)
    for key, value in extras_require.items():
        if key.startswith(':'):
            install_requires.extend(value)


setup(
    name='gli',
    version=find_version("gli", "__init__.py"),
    description='GitLab command line interface',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/evinoca/gli',
    project_urls={
        'Documentation': 'https://github.com/evinoca/gli',
        'Changelog': 'https://github.com/evinoca/gli/blob/release/CHANGELOG.md',
        'Source': 'https://github.com/evinoca/gli',
        'Tracker': 'https://github.com/evinoca/gli/issues',
    },
    author='Audric Sun',
    author_email='audric.s@outlook.com',
    license='MIT',
    packages=find_packages(exclude=['tests.*', 'tests']),
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    entry_points={
        'console_scripts': ['gli=gli.utils.entry:cli'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
)
