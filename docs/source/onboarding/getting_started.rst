Getting Started
===============

Overview of tools used
----------------------

This documentation is rendered using `Sphinx
<https://www.sphinx-doc.org/en/master/>`_, which is a Python-based
documentation generator that takes plain-text source files in `reStructuredText
(rST) <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ to
produce various output formats (this example uses HTML).

Additionally, Sphinx is extensible by other Python packages to expand it's
functionality - these tools are summarized below:

|

.. list-table::
   :widths: 20 50
   :header-rows: 1

   * - Tool
     - Description
   * - `Sphinx-Needs <https://www.sphinx-needs.com/>`_
     - Requirements lifecycle management
   * - `Mermaid <https://mermaid.js.org/intro/>`_
     - Diagrams and charting
   * - `Wavedrom <https://wavedrom.com/>`_
     - Digital timing diagrams

|

`Visio
<https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software>`_
/ `draw.io <https://www.drawio.com/>`_ can be used to generate any diagrams
more complex than can be done with Mermaid, as they both support ``.svg``
format.

|

Activating the virtual environment
----------------------------------

Confirm the `Python Virtual Environment <https://realpython.com/python-virtual-environments-a-primer/#what-is-a-python-virtual-environment>`_
is active - you should see ``(.venv)`` next to your username on the command line:

|

.. figure:: ./images/venv_confirmation.png

   *Virtual environment is active*

|

If you don't see it, navigate to where you cloned the repository and source the
``init_venv.sh`` bash script:

|

.. figure:: ./images/venv_script.png

   *Location of environment initialization script*

|

.. note::

   The script takes care of the virtual environment setup, and installs package
   dependencies for all the tools mentioned throughout this example
   documentation, so you can just focus on tutorials and effectively skip any
   steps that ask you to run any ``pip install`` commands

|

Creating your sandbox
---------------------

Next, you'll want to create your own working directory, or a "sandbox", for
going through the tutorials in the next section. 

In the repo, let's run ``mkdir sandbox`` and you should see that it was
created:

|

.. figure:: ./images/make_sandbox.png

   *Creating the tutorial sandbox*

|

Let's navigate to the sandbox and starting building the foundation.
