#!/usr/bin/env python

from setuptools import setup

requirements = []
version = '0.0.1'

print(f'Turing {version}')

with open('requirements.txt') as req_file:
    for req in req_file.readlines():
        req = req.split('\n')[0]

        print(f'Requires: {req}')
        requirements.append(req)

setup(name='turing',
      version=version,
      description='A flexible, lightweight and easy to use completely-automated-public-turing-test module for Python (for humans, duh).',
      author='xTrayambak',
      author_email='xtrayambak@gmail.com',
      url='https://www.github.com/xTrayambak/turing',
      packages=['turing'],
      requires = req
)
