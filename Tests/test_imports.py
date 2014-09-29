""" tests all modules for syntax correctness and internal imports
"""
from glob import glob
from importlib.machinery import (
   SourceFileLoader,
)
from inspect import (
   getfile as inspect_getfile,
   currentframe as inspect_currentframe,
)
from os import (
   walk as os_walk,
)
from os.path import (
   abspath as path_abspath,
   basename as path_basename,
   dirname as path_dirname,
   join as path_join,
   splitext as path_splitext,
)
from sys import path as sys_path


SCRIPT_PATH = path_dirname(path_abspath(inspect_getfile(inspect_currentframe())))
PROJECT_ROOT = path_dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'JqPyCharts'
ROOT_PACKAGE_PATH = path_join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

sys_path.insert(0, PROJECT_ROOT)


def test_all_imports_py():
   """ Tests: test_all_imports_py: for syntax correctness and internal imports
   """
   print('::: TEST: test_all_imports_py()')
   all_modules_path = []
   for root, dirnames, filenames in os_walk(ROOT_PACKAGE_PATH):
      all_modules_path.extend(glob(root + '/*.py'))
   for py_module_file_path in all_modules_path:
      module_filename = path_basename(py_module_file_path)
      module_filename_no_ext = path_splitext(module_filename)[0]

      py_loader = SourceFileLoader(module_filename_no_ext, py_module_file_path)
      py_loader.load_module(module_filename_no_ext)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   test_all_imports_py()
