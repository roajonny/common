Description
===========

This directory provides "Docs-as-Code" infrastructure and tools for FPGA
development.

It contains python scripts for generating HDL, vimrc/bashrc templates for
setting up user environments, and a `documentation template
<https://roajonny.github.io/index.html>`_ which doubles as
a tutorial/onboarding guide for a *hardware-as-software* workflow methodology.

System Dependencies
===================

* `Python3 <https://docs.python-guide.org/starting/install3/linux/>`_ (>= *3.10.12*)
* `Graphviz <https://graphviz.org/download/>`_ (graphical rendering engine)

Build Instructions
==================

#. Navigate to this directory in a Bash terminal and run ``source init_venv.sh``
#. Navigate to ``docs/`` and run ``make`` to build the template documentation
#. Navigate to ``docs/build/`` and open ``index.html`` in the browser of your
   choice to view

List of Tools
=============

.. list-table::
   :widths: 50 20
   :header-rows: 1

   * - Tool
     - Tags
   * - Documentation template generator
     - Sphinx
   * - HDL module template generator
     - Verilog
   * - HDL testbench template generator
     - Verilog 
   * - HDL FSM template generator
     - Verilog
   * - HDL D-FF template generator
     - Verilog
