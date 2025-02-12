Scope of Work
=================

.. tutorial-project:: HITL FPGA Implementation
   :id: T_HITL
   :tags: tutorial
   :layout: clean_l
   :status: na
   :collapse: true

   .. tabs:: 

      .. tab:: Description

         The FPGA needs to implement two UART interfaces over external RS422 and
         LVDS ICs, which are controllable by host software over PCI-Express

      .. tab:: Flat-Sat (Image)

         .. image:: images/esa_flat_sat.png
            :width: 400

|

.. mermaid::

   %%{init: {'theme':'dark'}}%%
   flowchart LR
       host[Host SW] <==> a[PCIe2MM Bridge]
       subgraph Custom Hardware
           subgraph FPGA
               a[PCIe2MM Bridge] <==> b[**Memory Map**]
               subgraph **Customer Request**
                   b[**Memory Map**] <==> c[**UART**]
                   b[**Memory Map**] <==> d[**UART**]
               end
           end
       c[**UART**] <==> e[UUT]
       d[**UART**] <==> f[UUT]
       end
   e[RS422 IC] <==> g[UUT]
   f[LVDS IC]  <==> g[UUT]

|

The :doc:`../requirements/high_level_reqs` section captures the customer's
high-level needs in requirements format.

.. note::
   
   The *Scope of Work* is a general description of what the customer is asking
   for - this information is captured in a Sphinx-Needs "object" and is the
   root of the :doc:`../requirements/traceability`
