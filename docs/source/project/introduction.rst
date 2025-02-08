Introduction
============

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

The client is working on a hardware-in-the-loop (HITL) testbed application that requires an FPGA on their custom hardware to
implement two UART interfaces which will be controlled by SW over PCI-Express.

They've already developed and verified this hardware, and need designer
engineers to design the UART logic as well as their controllers - it might look
something like this:

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
