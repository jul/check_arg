#!/usr/bin/env python
# -*- coding: "utf-8" -*-

#from setuptools import setup, find_packages
from distutils.core import setup
import unittest
import sys
#from distutils.command.build_py import build_py as _build_py
#import unittest
#import sys

def test():
    """Specialized Python source builder."""
    from check_arg import test_valid
    loader= unittest.TestLoader()
    suite=loader.loadTestsFromModule(test_valid)
    runner=unittest.TextTestRunner()
    result=runner.run(suite)
    if  not result.wasSuccessful():
        raise Exception( "Test Failed: Aborting install")

if "install" in sys.argv or "sdist" in sys.argv or "update" in sys.argv:
    test()

setup(
        name='check_arg',
        version='0.1.0',
        author='Julien Tayon',
        author_email='julien@tayon.net',
        packages=['check_arg'],
        url='http://check_arg.readthedocs.org/',
        license=open('LICENSE.txt').read(),
        description="wrapping decorator to enhance the documentation",
        long_description="License :: OSI Approved :: BSD License",
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
