#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def _read(filename):
    with open(filename) as f:
        return f.read()

# Load package version.
exec(_read('nvget/_version.py'))

setup(
    name='nvget',
    version=__version__,
    description='nvget',
    long_description=_read('README.rst'),
    url='https://github.com/kmaehashi/nvget',
    author='Kenichi Maehashi',
    author_email='webmaster@kenichimaehashi.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['nvget'],
    test_suite='nvget.test',
    entry_points={
        'console_scripts': [
            'nvget=nvget.cli:nvget',
        ],
    },
    install_requires=[
        'selenium',
        'requests',
    ],
)
