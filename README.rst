.. _LongDescription:

***********************
JqPyCharts: Description
***********************

.. rubric:: JqPyCharts:
.. rubric:: Selection of: Javascripts / Css for simple charts

.. contents::
   :depth: 3


HTML Documentation
==================

HTML documentation of the project is hosted at: `JqPyCharts-HTML documentation <http://jqpycharts.readthedocs.org/>`_

Or `Package Documentation <http://pythonhosted.org//JqPyCharts/>`_


Main Info
=========

Just a selection of different javascripts / css for simple charts.

**Credit goes to all the projects which `JqPyCharts` makes use of:**

- `jquery <https://jquery.org/>`_
- `jqPlot <https://bitbucket.org/cleonello/jqplot>`_


Main Features
-------------

Just encoded files and some function to help write them out with python.
Mainly here so that one can make it a requirement for a project.



Simple Pie Chart
++++++++++++++++

There is a simple higher level function to help in producing simple pie charts.

seealso `development source: Example3.py`

- Define some html template

   .. code-block:: python

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

- add the function: `jqpc_simple_pie_chart` and write the html

   .. code-block:: python

      js_css_resources_header, jqplotchart_script1, html_chart_insert_tag1 = jqpc_simple_pie_chart(
         source_dir_path='scripts',
         chart_id='Example3Id',
         chart_title='JqPyCharts Simple Pie Chart (Example3)',
         chart_data_matrix = [
            ('Fat', 200, '#EAA228', 'Fat: 86100 g'),
            ('Protein', 21, '#4bb2c5', 'Protein: 33600 g'),
            ('Carbohydrate', 10, '#c5b47f', 'Carbohydrate: 37800 g')
         ],
         highlighter_prefix='Grams',
         background='#fffdf6',
         width_px=480,
         height_px=300,
      )

      example3_html_code = html_template.format(
         js_css_resources_header=js_css_resources_header,
         jqplotchart_script1=jqplotchart_script1,
         html_chart_insert_tag1=html_chart_insert_tag1,
      )

      with open('example3__simple_pie_chart.html', 'w') as file_:
         file_.write(example3_html_code)


Simple Bar Chart
++++++++++++++++

There is a simple higher level function to help in producing simple bar charts.

seealso `development source: Example3.py`

- Define some html template

   .. code-block:: python

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

- add the function: `jqpc_simple_bar_chart` and write the html

   .. code-block:: python

      js_css_resources_header, jqplotchart_script1, html_chart_insert_tag1 = jqpc_simple_bar_chart(
         source_dir_path='scripts',
         chart_id='Example4Id',
         chart_title='JqPyCharts Simple Bar Chart (Example4)',
         chart_x_label='Grams',
         chart_data_matrix = [
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


Code Examples
=============

for code examples see the files in `development source folder`: Examples and read the jqplot documentation


Projects using JqPyCharts
=========================

`projects` which make use of: **JqPyCharts**

`HealthNutritionPlanner <https://github.com/peter1000/HealthNutritionPlanner>`_  (Plan: weight loss, healthy diets, meals.)

|
|

`JqPyCharts` is distributed under the terms of the BSD 3-clause license.
Consult LICENSE.rst or http://opensource.org/licenses/BSD-3-Clause.

(c) 2014, `peter1000` https://github.com/peter1000
All rights reserved.

|
|
