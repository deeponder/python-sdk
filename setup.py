#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import logging

from os import path
from setuptools import setup, find_packages


try:
    pkg_name = 'deepwisdom'
    libinfo_py = path.join(pkg_name, '_version.py')
    with open(libinfo_py, 'r', encoding='utf8') as f:
        for line in f:
            if line.startswith('__version__'):
                exec(line)
                break
    exec(line)  # gives __version__
    assert bool(__version__)
except Exception:
    logging.warning("Not version info found")
    __version__ = '0.0.0'
try:
    with open('requirements.txt', encoding='utf8') as f:
        _install_requires = f.read().splitlines()
except FileNotFoundError:
    _install_requires = []

try:
    with open('README.md', encoding='utf8') as f:
        _long_description = f.read()
except FileNotFoundError:
    _long_description = ''

_description = "天机sdk"

setup(
    name=pkg_name,
    version=__version__,
    packages=find_packages(exclude=('datarobot',)),
    description=_description,
    long_description=_long_description,
    long_description_content_type='text/markdown',
    license='Apache 2.0',
    package_data={"": ["templates/*.j2"]},
    install_requires=_install_requires,

    url="",
)
