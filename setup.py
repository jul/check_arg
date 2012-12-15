#!/usr/bin/env python
# -*- coding: "utf-8" -*-

#from setuptools import setup, find_packages
from distutils.core import setup
import unittest
import sys
#from distutils.command.build_py import build_py as _build_py
#import unittest
#import sys


setup(
        name='check_arg',
        version='0.1.0',
        author='Julien Tayon',
        author_email='julien@tayon.net',
        packages=['check_arg'],
        url='http://github.org/jul/check_arg',
        license="License :: OSI Approved :: BSD License",
        description="wrapping decorator to enhance the documentation",
        long_description=open("README.txt").read(),
        requires=[ ],
        classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
)
