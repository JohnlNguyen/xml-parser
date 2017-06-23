from distutils.core import setup
import os
from setuptools import setup

version = open('VERSION.txt').read()

setup(
    name='xml-parser',
    version=version,
    license='MIT',
    description='Parse MySQL XML datadump',
    author='John Nguyen',
    author_email='jolnguyen@ucdavis.edu',
    url='https://github.com/JohnlNguyen/XML-Parser',
    packages=['parse'],
    zip_safe=False,
)

      