import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    readme = f.read()

setup(
    name='expediaRequester',
    version='0.1',
    description='Python wrapper for Expedia API',
    long_description=readme,
    author='Nimit Shah',
    author_email='nimit.svnit@gmail.com',
    packages=['expediaRequester'],
    package_data={'': ['LICENSE']},
    package_dir={'expediaRequester': 'expediaRequester'},
    install_requires=['requests'],
    license=license,
)
