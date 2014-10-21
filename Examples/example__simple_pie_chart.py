""" Example implementation: simple_pie_chart
"""
from inspect import (
   getfile as inspect_getfile,
   currentframe as inspect_currentframe,
)
from os.path import (
   abspath as path_abspath,
   dirname as path_dirname,
   join as path_join,
)
from sys import path as sys_path


SCRIPT_PATH = path_dirname(path_abspath(inspect_getfile(inspect_currentframe())))
PROJECT_ROOT = path_dirname(SCRIPT_PATH)

ROOT_PACKAGE_NAME = 'JqPyCharts'
ROOT_PACKAGE_PATH = path_join(PROJECT_ROOT, ROOT_PACKAGE_NAME)

sys_path.insert(0, PROJECT_ROOT)


from JqPyCharts.main_code import jqpc_simple_pie_chart


html_template = '''
<!DOCTYPE html>
<html>
   <head>
{js_css_resources_header}
{jqplotchart_script1}
{jqplotchart_script2}
{jqplotchart_script3}
{jqplotchart_script4}
   </head>
   <body>
      <br>
      {html_chart_insert_tag1}
      <br>
      {html_chart_insert_tag2}
      <br>
      {html_chart_insert_tag3}
      <br>
      {html_chart_insert_tag4}
      <br>
   </body>
</html>
'''


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():

   # common var
   source_dir_path = path_abspath('scripts')
   script_src_tag_dir_path = 'scripts'
   background = '#fffdf6'
   legend_font_px = 15
   data_label_threshold = 9.0
   width_px = 550
   height_px = 300
   margin_top_px = 0
   margin_bottom_px = 0
   margin_right_px = 0
   margin_left_px = 0

   js_css_resources_header1, jqplotchart_script1, html_chart_insert_tag1 = jqpc_simple_pie_chart(
      absolute_source_dir_path=source_dir_path,
      script_src_tag_dir_path=script_src_tag_dir_path,
      chart_id='id_1',
      chart_title='JqPyCharts Simple Pie Chart: 3 (with defined legends)',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', 'Fat: 200 g'),
         ('Protein', 21, '#4bb2c5', 'Protein: 21 g'),
         ('Carbohydrate', 10, '#c5b47f', 'Carbohydrate: 10 g')
      ],

      highlighter_prefix='Grams',
      background=background,
      legend_font_px=legend_font_px,
      data_label_threshold=data_label_threshold,
      width_px=width_px,
      height_px=height_px,
      margin_top_px=margin_top_px,
      margin_bottom_px=margin_bottom_px,
      margin_right_px=margin_right_px,
      margin_left_px=margin_left_px
   )

   js_css_resources_header2, jqplotchart_script2, html_chart_insert_tag2 = jqpc_simple_pie_chart(
      absolute_source_dir_path=source_dir_path,
      script_src_tag_dir_path=script_src_tag_dir_path,
      chart_id='id_2',
      chart_title='JqPyCharts Simple Pie Chart: 2 (with no defined legends)',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', ''),
         ('Protein', 21, '#4bb2c5', ''),
         ('Carbohydrate', 10, '#c5b47f', '')
      ],

      highlighter_prefix='Grams',
      background=background,
      legend_font_px=legend_font_px,
      data_label_threshold=data_label_threshold,
      width_px=width_px,
      height_px=height_px,
      margin_top_px=margin_top_px,
      margin_bottom_px=margin_bottom_px,
      margin_right_px=margin_right_px,
      margin_left_px=margin_left_px
   )

   js_css_resources_header3, jqplotchart_script3, html_chart_insert_tag3 = jqpc_simple_pie_chart(
      absolute_source_dir_path=source_dir_path,
      script_src_tag_dir_path=script_src_tag_dir_path,
      chart_id='id_3',
      chart_title='JqPyCharts Simple Pie Chart: 3 (with None legends)',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', None),
         ('Protein', 21, '#4bb2c5', None),
         ('Carbohydrate', 10, '#c5b47f', None)
      ],

      highlighter_prefix='Grams',
      background=background,
      legend_font_px=legend_font_px,
      data_label_threshold=data_label_threshold,
      width_px=width_px,
      height_px=height_px,
      margin_top_px=margin_top_px,
      margin_bottom_px=margin_bottom_px,
      margin_right_px=margin_right_px,
      margin_left_px=margin_left_px
   )

   js_css_resources_header4, jqplotchart_script4, html_chart_insert_tag4 = jqpc_simple_pie_chart(
      absolute_source_dir_path=source_dir_path,
      script_src_tag_dir_path=script_src_tag_dir_path,
      chart_id='id_4',
      chart_title='JqPyCharts Simple Pie Chart: 4 (no highlighter_prefix)',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', 'Fat: 200 g'),
         ('Protein', 21, '#4bb2c5', 'Protein: 21 g'),
         ('Carbohydrate', 10, '#c5b47f', 'Carbohydrate: 10 g')
      ],

      highlighter_prefix='',
      background=background,
      legend_font_px=legend_font_px,
      data_label_threshold=data_label_threshold,
      width_px=width_px,
      height_px=height_px,
      margin_top_px=margin_top_px,
      margin_bottom_px=margin_bottom_px,
      margin_right_px=margin_right_px,
      margin_left_px=margin_left_px
   )

   example_final_html_code = html_template.format(
      js_css_resources_header=js_css_resources_header1,
      jqplotchart_script1=jqplotchart_script1,
      jqplotchart_script2=jqplotchart_script2,
      jqplotchart_script3=jqplotchart_script3,
      jqplotchart_script4=jqplotchart_script4,
      html_chart_insert_tag1=html_chart_insert_tag1,
      html_chart_insert_tag2=html_chart_insert_tag2,
      html_chart_insert_tag3=html_chart_insert_tag3,
      html_chart_insert_tag4=html_chart_insert_tag4,
   )

   with open('example__simple_pie_chart.html', 'w') as file_:
      file_.write(example_final_html_code)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()
