.. _README:

******************
JqPyCharts: README
******************

**JqPyCharts: Selection of: Javascripts / Css for simple charts**

.. contents::
   :depth: 3


HTML Documentation
==================

HTML documentation of the project is hosted at: `JqPyCharts-HTML documentation <http://jqpycharts.readthedocs.org/>`_


System Requirements
===================

:ref:`RequiredSoftware`   (in  `development-source: 'docs/source/main_docs'`)


Installation
------------

1. python packages might be available from pypi: to be installed with: pip/pip3

   `pip installing packages <http://pip.readthedocs.org/en/latest/user_guide.html#installing-packages>`_

   .. code-block:: sh

      $ sudo pip3 install JqPyCharts

2. or run the standard package installation from the source folder:

   .. code-block:: sh

      $ python3 setup.py install

3. or use the top-level Makefile from the `development-source: 'root folder'`: to see all options run:

   .. code-block:: sh

      $ make

4. or add the folder to the python path: see **RandomNotes**   (in `development-source: 'info folder'`)


Build the Documentation
-----------------------

MAIN plus API documentation in `development-source: 'docs folder'`

**To build: run the `development-source: top-level` Makefile**

.. code-block:: sh

   $ make docs

Resulting `html documentation` will be in:
   /docs/JqPyCharts-DOCUMENTATION/html/index.html


Getting Started
===============

- Generate the documentation or read the .rst files

- Run any tests: in the `development-source: top-level` (root) project folder execute:

   .. code-block:: sh

      $ make tests

- Check out any `Examples folder`, `SpeedCheck folder`, `Tests folder`


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

.. seealso:: `development source: Example3.py`

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


   This will produce a html page with a chart like the one below

   .. image:: img/simple_pie_chart.png


Simple Bar Chart
++++++++++++++++

There is a simple higher level function to help in producing simple bar charts.

.. seealso:: `development source: Example3.py`

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


   This will produce a html page with a chart like the one below

   .. image:: img/simple_bar_chart.png


Code Examples
=============

for code examples see the files in `development source folder`: Examples and read the jqplot documentation


Code Usage - How To Implement
=============================


Common Errors
-------------

- Json true/True: in jqpc_html__insert_jqplotchart_script() jqplot_options:

   - this is a python json obj and uses: True/False ect..


Getting Help
============

No help is provided. You may try to open a new `issue` at github but it is uncertain if anyone will look at it.

|
|

`JqPyCharts` is distributed under the terms of the BSD 3-clause license.
Consult LICENSE.rst or http://opensource.org/licenses/BSD-3-Clause.

(c) 2014, `peter1000` https://github.com/peter1000
All rights reserved.

|
|
