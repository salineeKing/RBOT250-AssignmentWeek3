import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='rbot250',
    version='0.0.0',
    packages=find_packages(
        include=('rbot250', 'rbot250.*')),
)
