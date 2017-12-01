#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    maintainer='shtouff',
    maintainer_email='remi.paulmier@g***l.com',
    name='t0nd3uz',
    packages=find_packages('src/', exclude=['tests', 'tests.*']),
    package_dir={'': 'src'},
    scripts=['scripts/t0nd3uz'],
    install_requires=[
        'click',
    ],
)
