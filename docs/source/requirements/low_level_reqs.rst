Low-Level / Derived
===================

.. needtable::
   :columns: id; title; tags; status
   :tags: LL
   :show_filters:

|
      
.. note::
   
   *Low-Level Requirements* are most applicable to the design team, where the
   technical requirements, specification, and verification criteria is
   established and performed with traceability to the high-level (customer)
   requirements

   *Derived Requirements* could be *Key Requirements* which needed further
   elaboration to be useful from a digital design / verification perspective

   At this level, *Specifications* are black-box behavioral models for
   requirements that design teams design to, and verification teams reference
   to build their simulation harnesses + test cases

   A :doc:`traceability` is helpful for visualizing the hierarchy of
   requirements

Low-Level / Derived (Full Descriptions)
---------------------------------------

|

.. req:: UART Baud Rate (CH.1)
   :id: LL_001
   :status: open
   :links: HL_001
   :tags: comms; LL 

   .. tabs::

      .. tab:: Description

         The FPGA *shall* provide a UART w/ programmable baud rate for the following
         rates:

         #. 115.2K (default)
         #. 57.6K
         #. 19.2K
         #. 9600
         #. 4800

      .. tab:: Specification

         Bit period, *T*, specified for each baud rate:
         
         #. 115.2K : T = 8.7us 
         #. 57.6K  : T = 17.3us
         #. 19.2K  : T = 52.1us
         #. 9600   : T = 104.2us
         #. 4800   : T = 208.3us

         .. wavedrom::

            { "signal" : [
                    {                      node: '.A.B............'},
                    { "name": 'uart_ch', "wave": 'x=.=.....|.=.=.x', "data": ['start', 'data', 'parity', 'stop'] }
            ],
            edge: ['A+B T']}

      .. tab:: Verification Method

         Analysis: verified by simulation
         
         |

         Verification *shall* be considered complete when simulation
         demonstrates the UART achieves a bit period within a +/- 5% for each
         baud rate

|

.. req:: UART Frame Format (CH.1)
   :id: LL_002
   :status: open
   :links: HL_001
   :tags: comms; LL

   .. tabs::

      .. tab:: Description

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

      .. tab:: Specification

         For a UART frame with 8-bit data payload = 0x3:

         .. wavedrom::

            { "signal" : [
                { "name": "uart_format", "wave": 'x|x==.......==x', "data": ['start', 'data', 'parity', 'stop'] },
                { "name": "uart_data",   "wave": 'x|10......1...x' },
                { "name": "frame_sync",  "wave": 'x|01..........0' }
            ]}

      .. tab:: Verification Method

         Analysis: verified by simulation

         |

         Verification *shall* be considered complete when simulation
         demonstrates correct frame format over 100 consecutive loopback
         transmissions
          
|

.. req:: UART Frame Synchronization (CH.1)
   :id: LL_003
   :status: open
   :links: HL_001
   :tags: comms; LL

   .. tabs::

      .. tab:: Description

         The FPGA *shall* provide a synchronization signal that aligns to the UART frame
         with a +/- 2ms margin

      .. tab:: Specification

         For a UART frame with 8-bit data payload = 0x3:

         .. wavedrom::

            { "signal" : [
                { "name": "uart_format", "wave": 'x|x==.......==x', "data": ['start', 'data', 'parity', 'stop'] },
                { "name": "uart_data",   "wave": 'x|10......1...x' },
                { "name": "frame_sync",  "wave": 'x|01..........0' }
            ]}

      .. tab:: Verification Method

         Analysis: verified by simulation

         |

         Verification *shall* be considered complete when simulation
         demonstrates the frame synchronization is within the +/- 2ms margin

|

.. req:: UART Control/Status (CH.1)
   :id: LL_004
   :status: open
   :links: HL_001
   :tags: comms; LL

   .. tabs::

      .. tab:: Description

         The FPGA *shall* provide 32-bit control/status registers which are aligned
         on a 4-byte boundary for the UART interface, which is accessible by host software over PCI-Express

      .. tab:: Verification Method

         Analysis: verified by simulation

         |

         Verification *shall* be considered complete when simulation
         demonstrates register writes/reads occur on a 4-byte boundary starting
         from the base address

|

.. req:: UART Baud Rate (CH.2)
   :id: LL_005
   :status: closed
   :links: HL_002
   :tags: comms; LL 

   .. tabs::

      .. tab:: Description

         The FPGA *shall* provide a UART w/ programmable baud rate for the following
         rates:

         #. 115.2K 
         #. 57.6K
         #. 19.2K (Default)
         #. 9600
         #. 4800

      .. tab:: Specification

         Bit period, *T*, specified for each baud rate:
         
         #. 115.2K : T = 8.7us 
         #. 57.6K  : T = 17.3us
         #. 19.2K  : T = 52.1us
         #. 9600   : T = 104.2us
         #. 4800   : T = 208.3us

         .. wavedrom::

            { "signal" : [
                    {                      node: '.A.B............'},
                    { "name": 'uart_ch', "wave": 'x=.=.....|.=.=.x', "data": ['start', 'data', 'parity', 'stop'] }
            ],
            edge: ['A+B T']}

      .. tab:: Verification Method

         Analysis: verified by simulation

         |
         
         Verification *shall* be considered complete when simulation
         demonstrates the UART achieves a bit period within a +/- 5% for each
         baud rate

|

.. req:: UART Frame Format (CH.2)
   :id: LL_006
   :status: closed
   :links: HL_002
   :tags: comms; LL

   .. tabs::

      .. tab:: Description

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

      .. tab:: Specification

         For a UART frame with 8-bit data payload = 0x3:

         .. wavedrom::

            { "signal" : [
                { "name": "uart_format", "wave": 'x|x==.......==x', "data": ['start', 'data', 'parity', 'stop'] },
                { "name": "uart_data",   "wave": 'x|10......1...x' },
                { "name": "frame_sync",  "wave": 'x|01..........0' }
            ]}

      .. tab:: Verification Method

         Analysis: verified by simulation

         |

         Verification *shall* be considered complete when simulation
         demonstrates correct frame format over 100 consecutive loopback
         transmissions

|

.. req:: UART Frame Synchronization (CH.2)
   :id: LL_007
   :status: closed
   :links: HL_002
   :tags: comms; LL

   .. tabs::

      .. tab:: Description

         The FPGA *shall* provide a synchronization signal that aligns to the UART frame
         with a +/- 2ms margin

      .. tab:: Specification

         For a UART frame with 8-bit data payload = 0x3:

         .. wavedrom::

            { "signal" : [
                { "name": "uart_format", "wave": 'x|x==.......==x', "data": ['start', 'data', 'parity', 'stop'] },
                { "name": "uart_data",   "wave": 'x|10......1...x' },
                { "name": "frame_sync",  "wave": 'x|01..........0' }
            ]}

      .. tab:: Verification Method

         Analysis: verified by simulation

         |

         Verification *shall* be considered complete when simulation
         demonstrates the frame synchronization is within the +/- 2ms margin

|

.. req:: UART Control/Status (CH.2)
   :id: LL_008
   :status: in-progress
   :links: HL_002
   :tags: comms; LL

   .. tabs::

      .. tab:: Description

         The FPGA *shall* provide 32-bit control/status registers which are aligned
         on a 4-byte boundary for the UART interface, which is accessible by host software over PCI-Express

      .. tab:: Verification Method

         Analysis: verified by simulation

         |

         Verification *shall* be considered complete when simulation
         demonstrates register writes/reads occur on a 4-byte boundary starting
         from the base address
