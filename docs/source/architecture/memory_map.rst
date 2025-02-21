Memory Map
==========

.. list-table::
   :align: left
   :widths: 20 20 50
   :header-rows: 1

   * - Base Address
     - Bank Name
     - Description
   * - 0x00000000
     - `UART_CH1`_
     - Provides control and status for UART_CH1
   * - 0x01000000
     - `UART_CH2`_
     - Provides control and status for UART_CH2
   * - 0x02000000
     - RESERVED
     - RESERVED
   * - 0x03000000
     - RESERVED
     - RESERVED
   * - 0x04000000
     - RESERVED
     - RESERVED

.. note::

   Memory Maps are typically divided into regions, or *banks* to organize and
   partition a design's functionality

|

UART_CH1
--------

.. list-table::
   :align: left
   :widths: 20 30 50 30
   :header-rows: 1

   * - Offset
     - Register Name
     - Description
     - Default Value
   * - 0x0
     - `UART_CH1_EN_POKE`_
     - Enables UART channel
     - 0x00000000
   * - 0x4
     - `UART_CH1_RATE_POKE`_
     - Selects UART rate
     - 0x00000000
   * - 0x8
     - `UART_CH1_TX_FIFO_POKE`_
     - Buffers UART TX data
     - 0x00000000
   * - 0xC
     - `UART_CH1_TX_SEND_POKE`_
     - Enables UART transmission of FIFO data
     - 0x00000000
   * - 0x10
     - `UART_CH1_RX_FIFO_PEEK`_
     - Buffers UART RX data
     - 0x00000000

.. note::

   The registers in this template are either read-only/write-only and adopt the
   following naming convention, to be as descriptive as possible and intuitive
   to work with from an end-user perspective: ``<BANK
   NAME>_<FUNCTION>_<POKE/PEEK>``

|

UART_CH1_EN_POKE
~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60                           
   :header-rows: 1

   * - Field
     - Description
   * - [31:1]
     - RESERVED
   * - [0]
     - | '1' : Enable UART's RS422 IC
       | '0' : Disable UART's RS422 IC

UART_CH1_RATE_POKE
~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:3]
     - RESERVED
   * - [2:0]
     - | '000' : 115.2k (default)
       | '001' : 57.6k
       | '010' : 19.2k
       | '011' : 9600
       | '100' : 4800

UART_CH1_TX_FIFO_POKE
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:0]
     - Write data

UART_CH1_TX_SEND_POKE
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:1]
     - RESERVED
   * - [0]
     - | '1' : Start sending
       | '0' : Stop sending

UART_CH1_RX_FIFO_PEEK
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:0]
     - Read data

UART_CH2
--------

.. list-table::
   :align: left
   :widths: 20 30 50 30
   :header-rows: 1

   * - Offset
     - Register Name
     - Description
     - Default Value
   * - 0x0
     - `UART_CH2_EN_POKE`_
     - Enables UART channel
     - 0x00000000
   * - 0x4
     - `UART_CH2_RATE_POKE`_
     - Selects UART rate
     - 0x00000002
   * - 0x8
     - `UART_CH2_TX_FIFO_POKE`_
     - Buffers UART TX data
     - 0x00000000
   * - 0xC
     - `UART_CH2_TX_SEND_POKE`_
     - Enables UART transmission of FIFO data
     - 0x00000000
   * - 0x10
     - `UART_CH2_RX_FIFO_PEEK`_
     - Buffers UART RX data
     - 0x00000000

|

UART_CH2_EN_POKE
~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:1]
     - RESERVED
   * - [0]
     - | '1' : Enable UART's LVDS IC
       | '0' : Disable UART's LVDS IC

UART_CH2_RATE_POKE
~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:3]
     - RESERVED
   * - [2:0]
     - | '000' : 115.2k
       | '001' : 57.6k
       | '010' : 19.2k (Default)
       | '011' : 9600
       | '100' : 4800

UART_CH2_TX_FIFO_POKE
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:0]
     - Write data

UART_CH2_TX_SEND_POKE
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:1]
     - RESERVED
   * - [0]
     - | '1' : Start sending
       | '0' : Stop sending

UART_CH2_RX_FIFO_PEEK
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:0]
     - Read data
