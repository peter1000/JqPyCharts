""" setup / install / distribute
"""
import setuptools
import sys

from JqPyCharts import Version


if sys.version_info[:2] < (3, 4):
   sys.exit('JqPyCharts is only tested with Python 3.4.1 or higher:\ncurrent version: {0:d}.{1:d}'.format(sys.version_info[:2][0], sys.version_info[:2][1]))

print('\n\n==============================\n`JqPyCharts` VERSION: {}:\n   is developed on TESTED_HOST_OS platform: {}\n==============================\n\n'.format(Version.__version__, Version.TESTED_HOST_OS))


def read_requires(filename):
   """ Helper: read_requires
   """
   requires = []
   with open(filename, 'r') as file_:
      for line in file_:
         line = line.strip()
         if not line or line.startswith('#'):
            continue
         requires.append(line)
   return requires


setuptools.setup(
   name='JqPyCharts',
   version=Version.__version__,
   author='peter1000',
   author_email='https://github.com/peter1000',
   url='https://github.com/peter1000/',
   license='BSD-3-Clause',
   keywords='python web charts javascript css',
   packages=setuptools.find_packages(),
   include_package_data=True,
   scripts=[
   ],
   install_requires=read_requires('requirements.txt'),
   test_suite='nose.collector',
   use_2to3=False,
   zip_safe=True,
   platforms=['Linux'],
   classifiers=[
      'Development Status :: 3 - Alpha',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python :: 3',
      'Topic :: Internet :: WWW/HTTP',
   ],
   description='Selection of: Javascripts / Css for simple charts',
   long_description=open("README.rst", "r").read(),
)

#use: make to generate a source distribution tar
