#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" pyjdpu

  Copyright 2019 Slash Gordon

  Use of this source code is governed by an MIT-style license that
  can be found in the LICENSE file.
"""

from setuptools import setup, find_packages

EXCLUDE_FROM_PACKAGES = ['test', 'test.*', 'test*']
VERSION = '1.0.0'

with open('README.md', 'r') as fh:
    long_description = fh.read()

INSTALL_REQUIRES = (
    [
        'uplink==0.9.0',
    ]
)

setup(
    name='pyjdpu',
    version=VERSION,
    author='Slash Gordon',
    author_email='slash.gordon.dev@gmail.com',
    package_dir={'': 'src'},
    description='Updater tool for Jenkins docker plugin.txt',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SlashGordon/pyjdpu',
    install_requires=INSTALL_REQUIRES,
    packages=find_packages('src', exclude=EXCLUDE_FROM_PACKAGES),
    entry_points={'console_scripts': [
            'pyjdpu = pyjdpu:app',
    ]},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
