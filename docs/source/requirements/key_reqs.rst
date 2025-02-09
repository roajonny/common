High-Level (Customer)
=====================

*High-Level Requirements* are the customer requirements which serve as the
"handshake" between the customer and the design team about what the product is
supposed to do

|

.. needtable::
   :columns: id; title; tags; status

|

.. req:: UART over RS422
   :id: KEY_001
   :status: open
   :links: T_HITL
   :tags: comms

   The FPGA will provide a UART targeting an external RS422 IC which
   software-controllable over PCI-Express

|

.. req:: UART over LVDS
   :id: KEY_002
   :status: open
   :links: T_HITL
   :tags: comms

   The FPGA will provide a UART targeting an external LVDS IC which
   software-controllable over PCI-Express
