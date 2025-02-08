Introduction
============

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

The client is working on a hardware-in-the-loop (HITL) testbed application for
satellite avionics that require an FPGA on their custom test hardware to
implement two UART interfaces controllable by SW over PCI-Express to
communicate with their UUT/s.

They've already developed and verified this custom hardware, and need design
engineers to implement the UART logic as well as their respective controllers
- at a high level, it might look something like this:

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
