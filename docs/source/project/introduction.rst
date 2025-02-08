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
       subgraph FPGA
           A[PCIe2MM Bridge] ==> B[FPGA Memory Map]
           subgraph Customer Request
               B[FPGA Memory Map] ==> C[UART LVDS]
               B[FPGA Memory Map] ==> D[UART RS422]
           end
       end
       C[UART LVDS]  <==> E[DUT]
       D[UART RS422] <==> E[DUT]
