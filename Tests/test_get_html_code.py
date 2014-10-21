""" tests main_code: test_get_html_code.py
"""
from inspect import (
   getfile as inspect_getfile,
   currentframe as inspect_currentframe,
)
from os.path import (
   abspath as path_abspath,
   dirname as path_dirname,
   join as path_join,
   relpath as path_relpath,
)
from sys import path as sys_path

from nose.tools import (
   eq_,
   raises as nose_raises
)


SCRIPT_PATH = path_dirname(path_abspath(inspect_getfile(inspect_currentframe())))
PROJECT_ROOT = path_dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'JqPyCharts'
ROOT_PACKAGE_PATH = path_join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

sys_path.insert(0, PROJECT_ROOT)

from JqPyCharts.main_code import (
   jqpc_get_html_chart_div,
   jqpc_get_html_jqplotchart_script,
   jqpc_get_html_js_css_resources,
   jqpc_write__resource_dict
)
from JqPyCharts.utils import Err


# noinspection PyUnusedLocal
def test_jqpc_get_html_js_css_resources_ok1():
   """ Tests: test_jqpc_get_html_js_css_resources_ok1
   """
   print('::: TEST: test_jqpc_get_html_js_css_resources_ok1()')

   source_scripts_path = path_join(SCRIPT_PATH, 'source_scripts')
   # make sure we have the needed resources
   jqpc_write__resource_dict('jqplot_scripts', source_scripts_path, force=False)

   needed_resources = [
      'jquery.min.js',
      'jquery.jqplot.min.css',
      'jqplot.highlighter.min.js',
   ]
   out_js_css_resources = jqpc_get_html_js_css_resources(
      needed_resources, 
      source_scripts_path, 
      path_relpath(source_scripts_path),
      indent='      '
   )

# noinspection PyUnusedLocal
def test_jqpc_get_html_js_css_resources_ok2():
   """ Tests: test_jqpc_get_html_js_css_resources_ok2
   """
   print('::: TEST: test_jqpc_get_html_js_css_resources_ok2()')

   source_scripts_path = path_join(SCRIPT_PATH, 'source_scripts')
   # make sure we have the needed resources
   jqpc_write__resource_dict('jqplot_scripts', source_scripts_path, force=False)

   needed_resources = [
      'jquery.min.js',
      'jquery.jqplot.min.css',
      'jqplot.highlighter.min.js',
   ]
   out_js_css_resources = jqpc_get_html_js_css_resources(
      needed_resources, 
      source_scripts_path, 
      path_abspath(source_scripts_path),
      indent='      '
   )

# noinspection PyUnusedLocal
@nose_raises(Err)
def test_jqpc_get_html_js_css_resources__expect_failure1():
   """ Tests: test_jqpc_get_html_js_css_resources__expect_failure1
   """
   print('::: TEST: test_jqpc_get_html_js_css_resources__expect_failure1()')

   source_scripts_path = path_join(SCRIPT_PATH, 'source_scripts')
   # make sure we have the needed resources
   jqpc_write__resource_dict('jqplot_scripts', source_scripts_path, force=False)

   needed_resources = [
      'jquery.min.js',
      'jquery.jqplot.min.css',
      'wrong_resource_name',
   ]
   out_js_css_resources = jqpc_get_html_js_css_resources(
      needed_resources, 
      source_scripts_path, 
      path_relpath(source_scripts_path),
      indent='      '
   )


# noinspection PyUnusedLocal
@nose_raises(Err)
def test_jqpc_get_html_js_css_resources__expect_failure2():
   """ Tests: test_jqpc_get_html_js_css_resources__expect_failure2
   """
   print('::: TEST: test_jqpc_get_html_js_css_resources__expect_failure2()')

   source_scripts_path = path_join(SCRIPT_PATH, 'source_scripts')
   # make sure we have the needed resources
   jqpc_write__resource_dict('jqplot_scripts', source_scripts_path, force=False)

   needed_resources = [
      'jquery.min.js',
      'jquery.jqplot.min.css',
      'wrong_ending.wrong',
   ]
   out_js_css_resources = jqpc_get_html_js_css_resources(
      needed_resources, 
      source_scripts_path, 
      path_relpath(source_scripts_path),
      indent='      '
   )


# noinspection PyPep8
def test_jqpc_get_html_chart_div_ok():
   """ Tests: test_jqpc_get_html_chart_div_ok
   """
   print('::: TEST: test_jqpc_get_html_chart_div_ok()')

   chart_id = 1
   out_insert_chart = jqpc_get_html_chart_div(
      chart_id,
      width_px=300,
      height_px=300,
      margin_top_px=0,
      margin_bottom_px=0,
      margin_right_px=0,
      margin_left_px=0,
      indent=''
   )

   eq_(
      out_insert_chart,
      '''<div id="1" style="width:300px; height:300px; margin-top:0px; margin-bottom:0px; margin-right:0px; margin-left:0px;"></div>''',
      msg=None
   )


# noinspection PyUnusedLocal
def test_jqpc_get_html_jqplotchart_script_ok():
   """ Tests: test_jqpc_get_html_jqplotchart_script_ok
   """
   print('::: TEST: test_jqpc_get_html_jqplotchart_script_ok()')

   chart_id = 1
   extra_variables_lines_dict = {
      'chart_data': [200, 21, 10],
      'chart_colors': ['#EAA228', '#4bb2c5', '#c5b47f'],
      'chart_ticks': ['Fat', 'Protein', 'Carbohydrate'],
      'chart_legends': ['legend1', 'legend2', 'legend3'],
   }

   jqplot_options_txt = '''
            {
               title: 'JqPyCharts Simple Pie Chart (Example3)',
               grid: {
                  drawBorder: true,
                  drawGridlines: true,
                  background: '#fffdf6',
                  shadow:true
               },
               seriesDefaults: {
                  renderer: jQuery.jqplot.PieRenderer,

                  rendererOptions: {
                     startAngle: 90,
                     fill: true,
                     highlightMouseOver: true,
                     sliceMargin:5,
                     shadow: true,
                     shadowOffset:0.8,
                     shadowAlpha:0.5,
                     shadowDepth:5,
                     showDataLabels: true,
                     dataLabels: 'percent',
                     dataLabelFormatString:'%.1f %',
                     dataLabelThreshold: 9.0,
                     dataLabelCenterOn: true,
                     dataLabelNudge: 0,
                     dataLabelPositionFactor: 0.65,
                  }
               },
               seriesColors: chart_colors,
               highlighter: {
                  show: true,
                  tooltipLocation: 'sw',
                  useAxesFormatters: false,
                  tooltipAxes: 'n',
                  yvalues: 2,
                  formatString: '<table class="jqplot-highlighter">' +
                  '<tr><td><strong>%s</strong></td><td></td></tr>' +
                  '<tr><td>Grams:</td><td>%s</td></tr></table>'
               },
               legend: {
                  placement: 'insideGrid',
                  show: true,
                  labels: chart_legends,
                  rowSpacing: '0.5em',
                  fontSize: 15,
                  location: 'e'
               }
            }
'''
   jqplotchart_script = jqpc_get_html_jqplotchart_script(
      chart_id,
      extra_variables_lines_dict,
      jqplot_options_txt,
      enable_plugins=True,
      base_indent='      '
   )


# noinspection PyUnusedLocal
@nose_raises(Err)
def test_jqpc_get_html_jqplotchart_script__expect_failure1():
   """ Tests: test_jqpc_get_html_jqplotchart_script__expect_failure1
   """
   print('::: TEST: test_jqpc_get_html_jqplotchart_script__expect_failure1()')

   chart_id = 1
   extra_variables_lines_dict = {
      'chart_data_wrong_key': [200, 21, 10],
      'chart_colors': ['#EAA228', '#4bb2c5', '#c5b47f'],
      'chart_ticks': ['Fat', 'Protein', 'Carbohydrate'],
      'chart_legends': ['legend1', 'legend2', 'legend3'],
   }

   jqplot_options_txt = '''
            {
               title: 'JqPyCharts Simple Pie Chart (Example3)',
               grid: {
                  drawBorder: true,
                  drawGridlines: true,
                  background: '#fffdf6',
                  shadow:true
               },
               seriesDefaults: {
                  renderer: jQuery.jqplot.PieRenderer,

                  rendererOptions: {
                     startAngle: 90,
                     fill: true,
                     highlightMouseOver: true,
                     sliceMargin:5,
                     shadow: true,
                     shadowOffset:0.8,
                     shadowAlpha:0.5,
                     shadowDepth:5,
                     showDataLabels: true,
                     dataLabels: 'percent',
                     dataLabelFormatString:'%.1f %',
                     dataLabelThreshold: 9.0,
                     dataLabelCenterOn: true,
                     dataLabelNudge: 0,
                     dataLabelPositionFactor: 0.65,
                  }
               },
               seriesColors: chart_colors,
               highlighter: {
                  show: true,
                  tooltipLocation: 'sw',
                  useAxesFormatters: false,
                  tooltipAxes: 'n',
                  yvalues: 2,
                  formatString: '<table class="jqplot-highlighter">' +
                  '<tr><td><strong>%s</strong></td><td></td></tr>' +
                  '<tr><td>Grams:</td><td>%s</td></tr></table>'
               },
               legend: {
                  placement: 'insideGrid',
                  show: true,
                  labels: chart_legends,
                  rowSpacing: '0.5em',
                  fontSize: 15,
                  location: 'e'
               }
            }
'''
   jqplotchart_script = jqpc_get_html_jqplotchart_script(
      chart_id,
      extra_variables_lines_dict,
      jqplot_options_txt,
      enable_plugins=True,
      base_indent='      '
   )


# noinspection PyUnusedLocal
@nose_raises(Err)
def test_jqpc_get_html_jqplotchart_script__expect_failure2():
   """ Tests: test_jqpc_get_html_jqplotchart_script__expect_failure2
   """
   print('::: TEST: test_jqpc_get_html_jqplotchart_script__expect_failure2()')

   chart_id = 1
   extra_variables_lines_dict = {
      'chart_data': (200, 21, 10),
      'chart_colors': ['#EAA228', '#4bb2c5', '#c5b47f'],
      'chart_ticks': ['Fat', 'Protein', 'Carbohydrate'],
      'chart_legends': ['legend1', 'legend2', 'legend3'],
   }

   jqplot_options_txt = '''
            {
               title: 'JqPyCharts Simple Pie Chart (Example3)',
               grid: {
                  drawBorder: true,
                  drawGridlines: true,
                  background: '#fffdf6',
                  shadow:true
               },
               seriesDefaults: {
                  renderer: jQuery.jqplot.PieRenderer,

                  rendererOptions: {
                     startAngle: 90,
                     fill: true,
                     highlightMouseOver: true,
                     sliceMargin:5,
                     shadow: true,
                     shadowOffset:0.8,
                     shadowAlpha:0.5,
                     shadowDepth:5,
                     showDataLabels: true,
                     dataLabels: 'percent',
                     dataLabelFormatString:'%.1f %',
                     dataLabelThreshold: 9.0,
                     dataLabelCenterOn: true,
                     dataLabelNudge: 0,
                     dataLabelPositionFactor: 0.65,
                  }
               },
               seriesColors: chart_colors,
               highlighter: {
                  show: true,
                  tooltipLocation: 'sw',
                  useAxesFormatters: false,
                  tooltipAxes: 'n',
                  yvalues: 2,
                  formatString: '<table class="jqplot-highlighter">' +
                  '<tr><td><strong>%s</strong></td><td></td></tr>' +
                  '<tr><td>Grams:</td><td>%s</td></tr></table>'
               },
               legend: {
                  placement: 'insideGrid',
                  show: true,
                  labels: chart_legends,
                  rowSpacing: '0.5em',
                  fontSize: 15,
                  location: 'e'
               }
            }
'''
   jqplotchart_script = jqpc_get_html_jqplotchart_script(
      chart_id,
      extra_variables_lines_dict,
      jqplot_options_txt,
      enable_plugins=True,
      base_indent='      '
   )


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   pass
   test_jqpc_get_html_js_css_resources_ok1()
   test_jqpc_get_html_js_css_resources_ok2()
   test_jqpc_get_html_js_css_resources__expect_failure1()
   test_jqpc_get_html_js_css_resources__expect_failure2()

   test_jqpc_get_html_chart_div_ok()

   test_jqpc_get_html_jqplotchart_script_ok()
   test_jqpc_get_html_jqplotchart_script__expect_failure1()
   test_jqpc_get_html_jqplotchart_script__expect_failure2()
