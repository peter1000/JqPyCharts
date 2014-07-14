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
   jqpc_write__selected_resources,
   jqpc_html__insert_js_css_resources,
   jqpc_html__insert_chart,
   jqpc_html__insert_jqplotchart_script
)



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

   needed_resources = [
      'jquery.min.js',
      'jquery.jqplot.min.js',
      'jqplot.highlighter.min.js',
      'jqplot.canvasAxisLabelRenderer.min.js',
      'jqplot.categoryAxisRenderer.min.js',
      'jqplot.canvasTextRenderer.min.js',

      'jqplot.barRenderer.min.js',
      'jqplot.pointLabels.min.js',

      'jqplot.pieRenderer.min.js',

      'jquery.jqplot.min.css'
   ]

   source_dir_path = 'scripts'
   chart_id1 = 'macronutrient_ratio_g'


   jqpc_write__selected_resources('jqplot_scripts', needed_resources, source_dir_path, force=False)

   js_css_resources_header = (jqpc_html__insert_js_css_resources(needed_resources, source_dir_path, indent='      '))

   extra_variables_lines_dict = {'chart_data': [['Fat', 200], ['Protein', 21], ['Carbohydrate', 10]]}

   jqplot_options_txt = '''
               {
                  title: 'Macronutrient Ratio (g)',
                  grid: {
                     drawBorder: true,
                     drawGridlines: true,
                     background: '#fffdf6',
                     shadow:true
                  },

                  seriesDefaults: {

                     // Make this a pie chart.
                     renderer: jQuery.jqplot.PieRenderer,

                     rendererOptions: {
                        diameter: 200,
                        startAngle: 90,
                        fill: true,
                        highlightMouseOver: true,
                        sliceMargin:5,
                        shadow: true,
                        shadowOffset:0.8,
                        shadowAlpha:0.5,
                        shadowDepth:5,
                        // Put data labels on the pie slices.
                        // By default, labels show the percentage of the slice.
                        showDataLabels: true,
                        //dataLabels: the options 'value', 'percent', 'label' OR an array of labels.
                        dataLabels: 'percent',
                        dataLabelFormatString:'%.1f %',
                        dataLabelThreshold: 9,
                        dataLabelCenterOn: true,
                        dataLabelNudge: 0,
                        dataLabelPositionFactor: 0.65,
                     }
                  },
                  seriesColors: ["#EAA228", "#4bb2c5", "#c5b47f"],
                  highlighter: {
                     show: true,
                     tooltipLocation: 'sw',
                     useAxesFormatters: false,
                     tooltipAxes: 'n',
                     yvalues: 2,
                     formatString: '<table class="jqplot-highlighter">' +
                     '<tr><td><strong>%s</strong></td><td></td></tr>' +
                     '<tr><td>Daily Grams:</td><td>%s</td></tr></table>'
                  },
                  legend: {
                     placement: 'insideGrid',
                     show: true,
                     labels: ['Fat: 86100 g', 'Protein: 33600 g', 'Carbohydrate: 37800 g'],
                     rendererOptions: {
                        numberRows: 3
                     },
                     rowSpacing: '0.5em',
                     fontSize: 15,
                     location: 'e'
                  }
               }'''
   jqplotchart_script1 = jqpc_html__insert_jqplotchart_script(chart_id1, extra_variables_lines_dict, jqplot_options_txt, enable_plugins=True, base_indent='      ')

   html_chart_insert_tag1 = jqpc_html__insert_chart(chart_id1, width_px=480, height_px=300, margin_top_px=0, margin_bottom_px=0, margin_right_px=0, margin_left_px=0, indent='      ')

   example2_html_code = html_template.format(
      js_css_resources_header=js_css_resources_header,
      jqplotchart_script1=jqplotchart_script1,
      html_chart_insert_tag1=html_chart_insert_tag1,
   )

   with open('example2.html', 'w') as file_:
      file_.write(example2_html_code)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == '__main__':
   main()
