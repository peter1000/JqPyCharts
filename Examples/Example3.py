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


from JqPyCharts.MainCode import jqpc_simple_pie_chart


html_template = '''
<!DOCTYPE html>
<html>
   <head>
{js_css_resources_header}
{jqplotchart_script1}
   </head>
   <body>
{html_chart_insert_tag1}
   </body>
</html>
'''


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def main():

   js_css_resources_header, jqplotchart_script1, html_chart_insert_tag1 = jqpc_simple_pie_chart(
      source_dir_path='scripts',
      chart_id='Example3Id',
      chart_title='JqPyCharts Simple Pie Chart (Example3)',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', 'Fat: 200 g'),
         ('Protein', 21, '#4bb2c5', 'Protein: 21 g'),
         ('Carbohydrate', 10, '#c5b47f', 'Carbohydrate: 10 g')
      ],
      #chart_data_matrix = [('Fat', 200, '#EAA228', ''), ('Protein', 21, '#4bb2c5', ''), ('Carbohydrate', 10, '#c5b47f', '')],
      #chart_data_matrix = [('Fat', 200, '#EAA228', None), ('Protein', 21, '#4bb2c5', None), ('Carbohydrate', 10, '#c5b47f', None)],

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

   example3_html_code = html_template.format(
      js_css_resources_header=js_css_resources_header,
      jqplotchart_script1=jqplotchart_script1,
      html_chart_insert_tag1=html_chart_insert_tag1,
   )

   with open('example3__simple_pie_chart.html', 'w') as file_:
      file_.write(example3_html_code)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()
