Low-Level / Derived
===================

.. needtable::
   :columns: id; title; tags; status
   :tags: LL
   :show_filters:

|

.. note::
   
   *Low-Level Requirements* are most important for the design team, where the
   technical requirements / verification criteria is established and performed
   with traceability to the high-level (customer) requirements

   *Derived Requirements* could be *Key Requirements* which need to be
   further elaborated and specified before they're useful from a digital
   design / verification perspective

|

.. req:: UART Baud Rate (RS422)
   :id: LL_001
   :status: open
   :links: HL_001
   :tags: comms; LL 

   The FPGA *shall* provide a UART w/ programmable baud rate for the following
   rates:

   #. 115.2K (default)
   #. 57.6K
   #. 19.2K
   #. 9600
   #. 4800

|

.. req:: UART Frame Format (RS422)
   :id: LL_002
   :status: open
   :links: HL_001
   :tags: comms; LL

   The FPGA *shall* provide a UART w/ a frame format defined by the following:

   .. list-table::
      :align: left
      :widths: 10 50 10
      :header-rows: 1

      * - Field
        - Description
        - Value
      * - [10]
        - UART stop bit
        - 1
      * - [9]
        - UART parity bit (odd)
        - D/C
      * - [8:1]
        - UART data
        - D/C
      * - [0]
        - UART start bit
        - 0

|

.. req:: UART Frame Synchronization (RS422)
   :id: LL_003
   :status: open
   :links: HL_001
   :tags: comms; LL

   The FPGA *shall* provide a synchronization signal that aligns to the UART frame
   with a +/- 2ms margin

|

.. req:: UART Control/Status (RS422)
   :id: LL_004
   :status: open
   :links: HL_001
   :tags: comms; LL

   The FPGA *shall* provide 32-bit control/status registers which are aligned
   on a 4-byte boundary for the UART interface, which is accessible by host software over PCI-Express

|

.. req:: UART Baud Rate (LVDS)
   :id: LL_005
   :status: closed
   :links: HL_002
   :tags: comms; LL 

   The FPGA *shall* provide a UART w/ programmable baud rate for the following
   rates:

   #. 115.2K 
   #. 57.6K
   #. 19.2K (default)
   #. 9600
   #. 4800

|

.. req:: UART Frame Format (LVDS)
   :id: LL_006
   :status: closed
   :links: HL_002
   :tags: comms; LL

   The FPGA *shall* provide a UART w/ a frame format defined by the following:

   .. list-table::
      :align: left
      :widths: 10 50 10
      :header-rows: 1

      * - Field
        - Description
        - Value
      * - [10]
        - UART stop bit
        - 1
      * - [9]
        - UART parity bit (odd)
        - D/C
      * - [8:1]
        - UART data
        - D/C
      * - [0]
        - UART start bit
        - 0

|

.. req:: UART Frame Synchronization (LVDS)
   :id: LL_007
   :status: closed
   :links: HL_002
   :tags: comms; LL

   The FPGA *shall* provide a synchronization signal that aligns to the UART frame
   with a +/- 2ms margin

|

.. req:: UART Control/Status (LVDS)
   :id: LL_008
   :status: in-progress
   :links: HL_002
   :tags: comms; LL

   The FPGA *shall* provide 32-bit control/status registers which are aligned
   on a 4-byte boundary for the UART interface, which is accessible by host software over PCI-Express
