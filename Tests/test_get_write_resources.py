""" tests main_code: test_get_write_resources.py
"""
from inspect import (
   getfile as inspect_getfile,
   currentframe as inspect_currentframe,
)
from os.path import (
   abspath as path_abspath,
   dirname as path_dirname,
   exists as path_exists,
   join as path_join,
)
from shutil import rmtree as shutil_rmtree
from sys import path as sys_path

from nose.tools import (
   ok_,
   raises as nose_raises
)


SCRIPT_PATH = path_dirname(path_abspath(inspect_getfile(inspect_currentframe())))
PROJECT_ROOT = path_dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'JqPyCharts'
ROOT_PACKAGE_PATH = path_join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

sys_path.insert(0, PROJECT_ROOT)

from JqPyCharts.main_code import (
   jqpc_get_resources_dict,
   jqpc_write__resource_dict,
   jqpc_write__selected_resources,
)
from JqPyCharts.utils import Err


def test_jqpc_get_resources_dict_ok():
   """ Tests: test_jqpc_get_resources_dict_ok
   """
   print('::: TEST: test_jqpc_get_resources_dict_ok()')

   resource_dict = jqpc_get_resources_dict('jqplot_scripts')
   ok_('jquery.min.js' in resource_dict, msg=None)
   ok_('jqplot.pointLabels.min.js' in resource_dict, msg=None)


# noinspection PyUnusedLocal
@nose_raises(Err)
def test_jqpc_get_resources_dict__expect_failure1():
   """ Tests: test_jqpc_get_resources_dict__expect_failure1
   """
   print('::: TEST: test_jqpc_get_resources_dict__expect_failure1()')

   resource_dict = jqpc_get_resources_dict('not_existing')


def test_jqpc_write__resource_dict_ok1():
   """ Tests: test_jqpc_write__resource_dict_ok1
   """
   print('::: TEST: test_jqpc_write__resource_dict_ok1()')

   out_dir_path = path_join(SCRIPT_PATH, 'out_dir_path_test_jqpc_write__resource_dict_ok1')
   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)

   jqpc_write__resource_dict('jqplot_scripts', out_dir_path, force=False)
   jqpc_write__resource_dict('jqplot_scripts', out_dir_path, force=True)
   jqpc_write__resource_dict('jqplot_scripts', out_dir_path, force=False)

   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)


@nose_raises(Err)
def test_jqpc_write__resource_dict__expect_failure1():
   """ Tests: test_jqpc_write__resource_dict__expect_failure1
   """
   print('::: TEST: test_jqpc_write__resource_dict__expect_failure1()')

   out_dir_path = path_join(SCRIPT_PATH, 'out_dir_test_jqpc_write__resource_dict__expect_failure1')
   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)

   jqpc_write__resource_dict('wrong_name', out_dir_path, force=True)
   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)


@nose_raises(Err)
def test_jqpc_write__resource_dict__expect_failure2():
   """ Tests: test_jqpc_write__resource_dict__expect_failure2
   """
   print('::: TEST: test_jqpc_write__resource_dict__expect_failure2()')

   out_dir_path = path_join(SCRIPT_PATH, 'out_dir_test_jqpc_write__resource_dict__expect_failure2')
   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)

   jqpc_write__resource_dict('wrong'
                             '-name', out_dir_path, force=False)
   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)


def test_jqpc_write__selected_resources_ok1():
   """ Tests: test_jqpc_write__selected_resources_ok1
   """
   print('::: TEST: test_jqpc_write__selected_resources_ok1()')

   out_dir_path = path_join(SCRIPT_PATH, 'out_dir_test_jqpc_write__selected_resources_ok1')
   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)

   list_of_resource_names = ['excanvas.min.js', 'jqplot.highlighter.min.js', 'jquery.jqplot.min.css']
   jqpc_write__selected_resources('jqplot_scripts', list_of_resource_names, out_dir_path, force=False)

   for file_name in list_of_resource_names:
      ok_(path_exists(path_join(out_dir_path, file_name)), msg=None)

   list_of_resource_names = ['excanvas.min.js', 'jqplot.highlighter.min.js', 'jquery.jqplot.min.css']
   jqpc_write__selected_resources('jqplot_scripts', list_of_resource_names, out_dir_path, force=False)

   list_of_resource_names = ['excanvas.min.js', 'jqplot.highlighter.min.js', 'jquery.jqplot.min.css']
   jqpc_write__selected_resources('jqplot_scripts', list_of_resource_names, out_dir_path, force=True)

   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)


@nose_raises(Err)
def test_jqpc_write__selected_resources__expect_failure1():
   """ Tests: test_jqpc_write__selected_resources__expect_failure1
   """
   print('::: TEST: test_jqpc_write__selected_resources__expect_failure1()')

   out_dir_path = path_join(SCRIPT_PATH, 'out_dir_test_jqpc_write__selected_resources__expect_failure1')
   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)

   list_of_resource_names = ['excanvas.min.js', 'jqplot.highlighter.min.js', 'wrong_resource_name']
   jqpc_write__selected_resources('jqplot_scripts', list_of_resource_names, out_dir_path, force=False)

   if path_exists(out_dir_path):
      shutil_rmtree(out_dir_path)


# CLEAN any left dirs
def test_clean_created_dirs():
   """ Tests: test_clean_created_dirs: this is just a helper to clean the dirs created in the tests
   """
   print('::: TEST: test_clean_created_dirs()')

   for dir_name in [
      'out_dir_path_test_jqpc_write__resource_dict_ok1',
      'out_dir_test_jqpc_write__resource_dict__expect_failure1',
      'out_dir_test_jqpc_write__resource_dict__expect_failure2',
      'out_dir_test_jqpc_write__selected_resources_ok1',
      'out_dir_test_jqpc_write__selected_resources__expect_failure1']:
      clean_path = path_join(SCRIPT_PATH, dir_name)
      if path_exists(clean_path):
         shutil_rmtree(clean_path)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   pass
   test_jqpc_get_resources_dict_ok()
   test_jqpc_get_resources_dict__expect_failure1()

   test_jqpc_write__resource_dict_ok1()
   test_jqpc_write__resource_dict__expect_failure1()
   test_jqpc_write__resource_dict__expect_failure2()

   test_jqpc_write__selected_resources_ok1()
   test_jqpc_write__selected_resources__expect_failure1()

   test_clean_created_dirs()
