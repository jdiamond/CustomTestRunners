#!/usr/bin/env python

from distutils.core import setup

setup(name='CustomTestRunners',
      version='1.0',
      description='Custom Test Runners',
      author='Jason Diamond',
      author_email='jason@diamond.name',
      url='http://github.com/jdiamond/CustomTestRunners',
      packages=['customtestrunners'],
      package_data={'customtestrunners': ['*.png']},
     )

