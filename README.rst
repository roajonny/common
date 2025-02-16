Description
===========

This directory provides "Docs-as-Code" infrastructure and Python3 tools for
FPGA development.

It contains python scripts (3.10.12) for generating HDL, starting points for
.vimrc/.bashrc to set up Linux user environment, and a "Hardware-as-Software"
`documentation template <https://roajonny.github.io/index.html>`_ which doubles
as a workflow tutorial/onboarding guide.

Doc. Build Instructions
=======================

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
