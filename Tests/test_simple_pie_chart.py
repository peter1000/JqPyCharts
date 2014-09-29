""" tests main_code: test_simple_pie_chart.py
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
   relpath as path_relpath,
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

from JqPyCharts.main_code import jqpc_simple_pie_chart
from JqPyCharts.utils import Err


def test_jqpc_simple_pie_chart_ok1():
   """ Tests: test_jqpc_simple_pie_chart_ok1
   """
   print('::: TEST: test_jqpc_simple_pie_chart_ok1()')

   scripts_pie_chart_path = path_join(SCRIPT_PATH, 'scripts_pie_chart_test_jqpc_simple_pie_chart_ok1')

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)

   js_css_resources_header, jqplotchart_script, html_chart_insert_tag = jqpc_simple_pie_chart(
      source_dir_path=scripts_pie_chart_path,
      chart_id='example_id',
      chart_title='JqPyCharts simple_pie_chart',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', 'Fat: 200 g'),
         ('Protein', 21, '#4bb2c5', 'Protein: 21 g'),
         ('Carbohydrate', 10, '#c5b47f', 'Carbohydrate: 10 g')
      ],
      highlighter_prefix='Grams',
      background='#fffdf6',
      legend_font_px=15,
      data_label_threshold=9.0,
      width_px=480,
      height_px=300,
      margin_top_px=0,
      margin_bottom_px=0,
      margin_right_px=0,
      margin_left_px=0
   )

   for resource_name in [
      'jquery.min.js',
      'jquery.jqplot.min.js',
      'jqplot.highlighter.min.js',
      'jqplot.canvasTextRenderer.min.js',
      'jqplot.pieRenderer.min.js',
      'jquery.jqplot.min.css']:

      resource_dir_path__abspath = path_join(scripts_pie_chart_path, resource_name)
      resource_dir_path__relpath = path_relpath(resource_dir_path__abspath)
      if resource_dir_path__abspath[-2:] == 'js':
         check_line = '<script type="text/javascript" src="{}"></script>'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      elif resource_dir_path__abspath[-3:] == 'css':
         check_line = '<link rel="stylesheet" type="text/css" href="{}">'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      else:
         raise Err('test_jqpc_simple_pie_chart_ok1', [
            '`resource_name`: <{}> must end with <.js> or <.css>'.format(resource_name)
         ])

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)


def test_jqpc_simple_pie_chart_ok2():
   """ Tests: test_jqpc_simple_pie_chart_ok2
   """
   print('::: TEST: test_jqpc_simple_pie_chart_ok2()')

   scripts_pie_chart_path = path_join(SCRIPT_PATH, 'scripts_pie_chart_test_jqpc_simple_pie_chart_ok2')

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)

   js_css_resources_header, jqplotchart_script, html_chart_insert_tag = jqpc_simple_pie_chart(
      source_dir_path=scripts_pie_chart_path,
      chart_id='example_id',
      chart_title='JqPyCharts simple_pie_chart',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', ''),
         ('Protein', 21, '#4bb2c5', ''),
         ('Carbohydrate', 10, '#c5b47f', '')
      ],
      highlighter_prefix='Grams',
      background='#fffdf6',
      legend_font_px=15,
      data_label_threshold=9.0,
      width_px=480,
      height_px=300,
      margin_top_px=0,
      margin_bottom_px=0,
      margin_right_px=0,
      margin_left_px=0
   )

   for resource_name in [
      'jquery.min.js',
      'jquery.jqplot.min.js',
      'jqplot.highlighter.min.js',
      'jqplot.canvasTextRenderer.min.js',
      'jqplot.pieRenderer.min.js',
      'jquery.jqplot.min.css']:

      resource_dir_path__abspath = path_join(scripts_pie_chart_path, resource_name)
      resource_dir_path__relpath = path_relpath(resource_dir_path__abspath)
      if resource_dir_path__abspath[-2:] == 'js':
         check_line = '<script type="text/javascript" src="{}"></script>'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      elif resource_dir_path__abspath[-3:] == 'css':
         check_line = '<link rel="stylesheet" type="text/css" href="{}">'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      else:
         raise Err('test_jqpc_simple_pie_chart_ok2', [
            '`resource_name`: <{}> must end with <.js> or <.css>'.format(resource_name)
         ])

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)


def test_jqpc_simple_pie_chart_ok3():
   """ Tests: test_jqpc_simple_pie_chart_ok3
   """
   print('::: TEST: test_jqpc_simple_pie_chart_ok3()')

   scripts_pie_chart_path = path_join(SCRIPT_PATH, 'scripts_pie_chart_test_jqpc_simple_pie_chart_ok3')

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)

   js_css_resources_header, jqplotchart_script, html_chart_insert_tag = jqpc_simple_pie_chart(
      source_dir_path=scripts_pie_chart_path,
      chart_id='example_id',
      chart_title='JqPyCharts simple_pie_chart',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', 'Fat: 200 g'),
         ('Protein', 21, '#4bb2c5', None),
         ('Carbohydrate', 10, '#c5b47f', 'Carbohydrate: 10 g')
      ],
      highlighter_prefix='Grams',
      background='#fffdf6',
      legend_font_px=15,
      data_label_threshold=9.0,
      width_px=480,
      height_px=300,
      margin_top_px=0,
      margin_bottom_px=0,
      margin_right_px=0,
      margin_left_px=0
   )

   for resource_name in [
      'jquery.min.js',
      'jquery.jqplot.min.js',
      'jqplot.highlighter.min.js',
      'jqplot.canvasTextRenderer.min.js',
      'jqplot.pieRenderer.min.js',
      'jquery.jqplot.min.css']:

      resource_dir_path__abspath = path_join(scripts_pie_chart_path, resource_name)
      resource_dir_path__relpath = path_relpath(resource_dir_path__abspath)
      if resource_dir_path__abspath[-2:] == 'js':
         check_line = '<script type="text/javascript" src="{}"></script>'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      elif resource_dir_path__abspath[-3:] == 'css':
         check_line = '<link rel="stylesheet" type="text/css" href="{}">'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      else:
         raise Err('test_jqpc_simple_pie_chart_ok3', [
            '`resource_name`: <{}> must end with <.js> or <.css>'.format(resource_name)
         ])

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)


def test_jqpc_simple_pie_chart_ok4():
   """ Tests: test_jqpc_simple_pie_chart_ok4: empty highlighter_prefix
   """
   print('::: TEST: test_jqpc_simple_pie_chart_ok4()')

   scripts_pie_chart_path = path_join(SCRIPT_PATH, 'scripts_pie_chart_test_jqpc_simple_pie_chart_ok4')

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)

   js_css_resources_header, jqplotchart_script, html_chart_insert_tag = jqpc_simple_pie_chart(
      source_dir_path=scripts_pie_chart_path,
      chart_id='example_id',
      chart_title='JqPyCharts simple_pie_chart',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', ''),
         ('Protein', 21, '#4bb2c5', ''),
         ('Carbohydrate', 10, '#c5b47f', '')
      ],
      highlighter_prefix='',
      background='#fffdf6',
      legend_font_px=15,
      data_label_threshold=9.0,
      width_px=480,
      height_px=300,
      margin_top_px=0,
      margin_bottom_px=0,
      margin_right_px=0,
      margin_left_px=0
   )

   for resource_name in [
      'jquery.min.js',
      'jquery.jqplot.min.js',
      'jqplot.highlighter.min.js',
      'jqplot.canvasTextRenderer.min.js',
      'jqplot.pieRenderer.min.js',
      'jquery.jqplot.min.css']:

      resource_dir_path__abspath = path_join(scripts_pie_chart_path, resource_name)
      resource_dir_path__relpath = path_relpath(resource_dir_path__abspath)
      if resource_dir_path__abspath[-2:] == 'js':
         check_line = '<script type="text/javascript" src="{}"></script>'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      elif resource_dir_path__abspath[-3:] == 'css':
         check_line = '<link rel="stylesheet" type="text/css" href="{}">'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      else:
         raise Err('test_jqpc_simple_pie_chart_ok4', [
            '`resource_name`: <{}> must end with <.js> or <.css>'.format(resource_name)
         ])

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)


@nose_raises(Err)
def test_jqpc_simple_pie_chart__expect_failure1():
   """ Tests: test_jqpc_simple_pie_chart__expect_failure1: chart_id with spaces
   """
   print('::: TEST: test_jqpc_simple_pie_chart__expect_failure1()')

   scripts_pie_chart_path = path_join(SCRIPT_PATH, 'scripts_pie_chart_test_jqpc_simple_pie_chart__expect_failure1')

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)

   js_css_resources_header, jqplotchart_script, html_chart_insert_tag = jqpc_simple_pie_chart(
      source_dir_path=scripts_pie_chart_path,
      chart_id='example_id wrong can not have spaces',
      chart_title='JqPyCharts simple_pie_chart',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', 'Fat: 200 g'),
         ('Protein', 21, '#4bb2c5', None),
         ('Carbohydrate', 10, '#c5b47f', 'Carbohydrate: 10 g')
      ],
      highlighter_prefix='',
      background='#fffdf6',
      legend_font_px=15,
      data_label_threshold=9.0,
      width_px=480,
      height_px=300,
      margin_top_px=0,
      margin_bottom_px=0,
      margin_right_px=0,
      margin_left_px=0
   )

   for resource_name in [
      'jquery.min.js',
      'jquery.jqplot.min.js',
      'jqplot.highlighter.min.js',
      'jqplot.canvasTextRenderer.min.js',
      'jqplot.pieRenderer.min.js',
      'jquery.jqplot.min.css']:

      resource_dir_path__abspath = path_join(scripts_pie_chart_path, resource_name)
      resource_dir_path__relpath = path_relpath(resource_dir_path__abspath)
      if resource_dir_path__abspath[-2:] == 'js':
         check_line = '<script type="text/javascript" src="{}"></script>'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      elif resource_dir_path__abspath[-3:] == 'css':
         check_line = '<link rel="stylesheet" type="text/css" href="{}">'.format(resource_dir_path__relpath)
         ok_(check_line in js_css_resources_header, msg=None)
      else:
         raise Err('test_jqpc_simple_pie_chart__expect_failure1', [
            '`resource_name`: <{}> must end with <.js> or <.css>'.format(resource_name)
         ])

   if path_exists(scripts_pie_chart_path):
      shutil_rmtree(scripts_pie_chart_path)


# CLEAN any left dirs
def test_clean_created_dirs():
   """ Tests: test_clean_created_dirs: this is just a helper to clean the dirs created in the tests
   """
   print('::: TEST: test_clean_created_dirs()')

   for dir_name in [
      'scripts_pie_chart_test_jqpc_simple_pie_chart_ok1',
      'scripts_pie_chart_test_jqpc_simple_pie_chart_ok2',
      'scripts_pie_chart_test_jqpc_simple_pie_chart_ok3',
      'scripts_pie_chart_test_jqpc_simple_pie_chart_ok4',
      'scripts_pie_chart_test_jqpc_simple_pie_chart__expect_failure1',
   ]:
      clean_path = path_join(SCRIPT_PATH, dir_name)
      if path_exists(clean_path):
         shutil_rmtree(clean_path)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   pass
   test_jqpc_simple_pie_chart_ok1()
   test_jqpc_simple_pie_chart_ok2()
   test_jqpc_simple_pie_chart_ok3()
   test_jqpc_simple_pie_chart_ok4()
   test_jqpc_simple_pie_chart__expect_failure1()

   test_clean_created_dirs()
