""" Example implementation
"""
from inspect import (
   getfile,
   currentframe
)
from os.path import (
   abspath,
   dirname,
   join
)
from sys import path as syspath


SCRIPT_PATH = dirname(abspath(getfile(currentframe())))
PROJECT_ROOT = dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'JqPyCharts'
ROOT_PACKAGE_PATH = join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

syspath.insert(0, PROJECT_ROOT)


from JqPyCharts.MainCode import (
   jqpc_get_string__encoded_dict_from_folder,
   jqpc_write__selected_resources,
   jqpc_write__resource_dict
)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():
   
   jqpc_write__selected_resources('jqplot_scripts', ['jquery.min.js'], 'scripts', force=False)
   
   jqpc_write__resource_dict('jqplot_scripts', 'scripts', force=False)
   
   # Helper to add copy/past manually: new resources to the: MainCode.py
   #print(jqpc_get_string__encoded_dict_from_folder('test', 'scripts'))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()
