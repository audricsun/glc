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
    'requests >= 2.20.0,< 3',
    'click >= 7',
    'rich >= 1'
]


tests_require = [
    'pytest >= 2.9',
    'pytest-flake8 >= 1',
    'pytest-cov',
    'pytest-mock',
]


if sys.version_info[:2] < (3, 4):
    tests_require.append('mock >= 1.0.1, < 4')

extras_require = {
    ':sys_platform == "win32"': ['colorama >= 0.4, < 1'],
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
    name='glc',
    version=find_version("glc", "__init__.py"),
    description='GitLab command line interface',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/evinoca/glc',
    project_urls={
        'Documentation': 'https://gli.readthedocs.io/en/latest/',
        'Changelog': 'https://github.com/evinoca/glc/blob/release/CHANGELOG.md',
        'Source': 'https://github.com/evinoca/glc',
        'Tracker': 'https://github.com/evinoca/glc/issues',
    },
    author='Audric Sun',
    author_email='audric.s@outlook.com',
    license='MIT',
    packages=find_packages(exclude=['tests.*', 'tests']),
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['glc=glc.cli.entry:cli'],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
