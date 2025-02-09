High-Level (Customer)
=====================

.. needtable::
   :columns: id; title; tags; status
   :tags: HL
   :show_filters:

|

.. note::
   
   *High-Level Requirements* are the customer requirements which serve as the
   "handshake" between the customer and the design team about what the product
   is supposed to do

|

.. req:: UART over RS422
   :id: HL_001
   :status: open
   :links: T_HITL
   :tags: comms; HL

   The FPGA will provide a UART w/ an additional frame-synchronization signal targeting an external RS422 IC which
   software-controllable over PCI-Express

|

.. req:: UART over LVDS
   :id: HL_002
   :status: in-progress
   :links: T_HITL
   :tags: comms; HL

   The FPGA will provide a UART w/ an additional frame-synchronization signal targeting an external LVDS IC which
   software-controllable over PCI-Express
