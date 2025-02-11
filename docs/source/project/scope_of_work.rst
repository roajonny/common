Scope of Work
=================

.. tutorial-project:: HITL FPGA Implementation
    :id: T_HITL
    :tags: tutorial
    :layout: clean_l
    :status: na
    :collapse: true

    The FPGA needs to implement two UART interfaces over external RS422 and
    LVDS ICs, which are controllable by host software over PCI-Express

|

.. mermaid::

   %%{init: {'theme':'dark'}}%%
   flowchart LR
       host[Host SW] <==> a[PCIe2MM Bridge]
       subgraph FPGA
           a[PCIe2MM Bridge] <==> b[**Memory Map**]
           subgraph **Customer Request**
               b[**Memory Map**] <==> c[**UART LVDS**]
               b[**Memory Map**] <==> d[**UART RS422**]
           end
       end
       c[**UART LVDS**]  ==> e[UUT]
       d[**UART RS422**] ==> e[UUT]

|

The :doc:`../requirements/high_level_reqs` section captures the customer's
high-level needs in requirements format.

.. note::
   
   The *Scope of Work* is a general description of what the customer is asking
   for - a Sphinx-Needs "object" is created to capture the information and is
   the root of the :doc:`../requirements/traceability`
