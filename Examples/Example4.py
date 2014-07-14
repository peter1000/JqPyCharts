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


from JqPyCharts.MainCode import jqpc_simple_bar_chart


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

   js_css_resources_header, jqplotchart_script1, html_chart_insert_tag1 = jqpc_simple_bar_chart(
      source_dir_path='scripts',
      chart_id='Example4Id',
      chart_title='JqPyCharts Simple Bar Chart (Example4)',
      chart_x_label='Grams',
      chart_data_matrix=[
         ('Fat', 200, '#EAA228', '200 g (57.7 %)'),
         ('Protein', 21, '#4bb2c5', '21 g (21.3 %)'),
         ('Carbohydrate', 10, '#c5b47f', '10 g (24.0 %)')
      ],
      width_px=480,
      height_px=300,
   )

   example4_html_code = html_template.format(
      js_css_resources_header=js_css_resources_header,
      jqplotchart_script1=jqplotchart_script1,
      html_chart_insert_tag1=html_chart_insert_tag1,
   )

   with open('example4__simple_bar_chart.html', 'w') as file_:
      file_.write(example4_html_code)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()
