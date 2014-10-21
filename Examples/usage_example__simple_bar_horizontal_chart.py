""" Example implementation: usage_example__simple_bar_chart
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


from JqPyCharts.main_code import jqpc_simple_bar_chart


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():

   html_template = '''
<!DOCTYPE html>
<html>
   <head>
{js_css_resources_header}
{jqplotchart_script1}
   </head>
   <body>
      <br>
      {html_chart_insert_tag1}
      <br>
   </body>
</html>
'''

   js_css_resources_header1, jqplotchart_script1, html_chart_insert_tag1 = jqpc_simple_bar_chart(
      absolute_source_dir_path=path_abspath('scripts'),
      script_src_tag_dir_path='scripts',
      chart_id='id_1',
      chart_title='JqPyCharts Simple Bar Chart: 1 (with defined legends)',
      chart_x_label='',
      chart_x_label_fontdict=None,
      chart_ticks_fontdict=None,
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', '200 g'),
         ('Protein', 21, '#4bb2c5', '21 g'),
         ('Carbohydrate', 10, '#c5b47f', '10 g')
      ],
      highlighter_prefix='Grams',
      background='#fffdf6',
      horizontal=True,
      draw_grid_lines=False,
      width_px=650,
      height_px=300,
      margin_top_px=0,
      margin_bottom_px=0,
      margin_right_px=0,
      margin_left_px=0
   )

   example_final_html_code = html_template.format(
      js_css_resources_header=js_css_resources_header1,
      jqplotchart_script1=jqplotchart_script1,
      html_chart_insert_tag1=html_chart_insert_tag1,
   )

   with open('usage_example__simple_bar_horizontal_chart.html', 'w') as file_:
      file_.write(example_final_html_code)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()
