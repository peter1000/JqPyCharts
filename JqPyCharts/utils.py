"""
================
JqPyCharts.utils
================

Overview
========
This module defines a couple of helpers.


Classes
=========
.. autoclass:: Err

"""

from JqPyCharts import TESTED_HOST_OS


class Err(Exception):
   """ Prints an own raised Project Error

   :param error_type: (str) to specify mostly from which part the error comes: e.g. CONFIG
   :param info: (list) list of strings (text info) to print as message: each list item starts at a new line
   """

   def __init__(self, error_type, info):
      """ Constructor.
      """
      Exception.__init__(self, error_type, info)
      self.__error_type = error_type
      self.__info = '\n'.join(info)
      self.__txt = '''

========================================================================
JqPyCharts-{} ERROR:


  {}

This `JqPyCharts` was tested with:
  HOST OS: {}
========================================================================

'''.format(self.__error_type, self.__info, TESTED_HOST_OS)
      print(self.__txt)
