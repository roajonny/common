Scope of Work
=================

The *Scope of Work* is a general description of what the customer is asking
for, and should get its own section in the requirements documentation:

|

.. tutorial-project:: HITL FPGA Implementation
    :id: T_HITL
    :tags: tutorial
    :layout: clean_l
    :status: na
    :collapse: true

    The FPGA needs to implement two UART interfaces targeting RS422 and LVDS, which
    are accessible/controllable by host software over PCI-Express

|

.. mermaid::

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
