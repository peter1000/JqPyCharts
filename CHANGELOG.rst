===============
Release History
===============

.. _whats-new:

Version 4.0.0     2014-10-21
============================

Features:
---------

   .. note::

      `JqPyCharts 4.0.0` is not backwards compatible (raise version to 4 to reflect that)

      - renamed and added: function parameters


   - changed: :py:func:`JqPyCharts.main_code.jqpc_simple_bar_chart`

      - for horizontal bar chars: switched the order of bars which is now the same as the `chart_data_matrix`

   - added option to: specify relative path for sources tags

   - added option to specify a html class for the chart for css styling

      - :py:func:`JqPyCharts.main_code.jqpc_get_html_chart_div`


Fixes/Other Changes:
--------------------

   - updated requirement:

      - PSphinxTheme>=2.0.3

   - updated Required Software


Version 2.0.2     2014-10-04
============================

Fixes/Other Changes:
--------------------

   - updated requirement:

      - PSphinxTheme>=2.0.1

   - updated Required Software

   - updated: updated docs: Projects using JqPyCharts


Version 2.0.1     2014-10-01
============================

Fixes/Other Changes:
--------------------

   - updated requirement: PSphinxTheme>=2.0.0
   - Required Software: setuptools >= 6.0.2, PySpeedIT >=1.0.7


Version 2.0.0     2014-09-29
============================

Features:
---------

   - Version 2.0.0

      .. note::

         `JqPyCharts 2.0.0` is not backwards compatible

            - renamed some functions

   - new documentation uses: PSphinxTheme

   - added option for 'horizontal bar charts'
   - added `highlighter` to bar charts


Fixes/Other Changes:
--------------------

   - Fixed Error in: JqPyCharts Simple Bar Chart
   - Fixed Error: function: `jqpc_html__insert_chart`  with Margins (error with margin-top tag)
   - Added more test cases
   - jqpc_get_html_js_css_resources(): uses now relative path in html outputs


Version 1.0.0     2014-07-14
============================

   - Release v. 1.0.0


Project start 2014-07-02
========================

   - project start
