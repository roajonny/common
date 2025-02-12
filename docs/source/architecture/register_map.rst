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
     - `RS422`_
     - Provides control and status for an RS422 UART
   * - 0x01000000
     - `LVDS`_
     - Provides control and status for an LVDS UART
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

RS422
-----

.. list-table::
   :align: left
   :widths: 20 30 50 30
   :header-rows: 1

   * - Offset
     - Register Name
     - Description
     - Default Value
   * - 0x0
     - `RS422_UART_EN_POKE`_
     - Enables UART channel
     - 0x00000000
   * - 0x4
     - `RS422_UART_RATE_POKE`_
     - Selects UART rate
     - 0x00000000
   * - 0x8
     - `RS422_UART_TX_FIFO_POKE`_
     - Buffers UART TX data
     - 0x00000000
   * - 0xC
     - `RS422_UART_TX_SEND_POKE`_
     - Enables UART transmission of FIFO data
     - 0x00000000
   * - 0x10
     - `RS422_UART_RX_FIFO_PEEK`_
     - Buffers UART RX data
     - 0x00000000

.. note::

   The registers in this template are either read-only/write-only and adopt the
   following naming convention, to be as descriptive as possible and intuitive
   to work with from an end-user perspective:

   **<BANK NAME>** _ **<FUNCTION>** _ **<POKE/PEEK>**

|

RS422_UART_EN_POKE
~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60                           
   :header-rows: 1

   * - Field
     - Description
   * - [31:1]
     - RESERVED
   * - [0]
     - | '1' : Enable channel
       | '0' : Disable channel

RS422_UART_RATE_POKE
~~~~~~~~~~~~~~~~~~~~

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

RS422_UART_TX_FIFO_POKE
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:0]
     - Write data

RS422_UART_TX_SEND_POKE
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:1]
     - RESERVED
   * - [1]
     - | '1' : Start sending
       | '0' : Stop sending

RS422_UART_RX_FIFO_PEEK
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:0]
     - Read data

LVDS
----

.. list-table::
   :align: left
   :widths: 20 30 50 30
   :header-rows: 1

   * - Offset
     - Register Name
     - Description
     - Default Value
   * - 0x0
     - `LVDS_UART_EN_POKE`_
     - Enables UART channel
     - 0x00000000
   * - 0x4
     - `LVDS_UART_RATE_POKE`_
     - Selects UART rate
     - 0x00000002
   * - 0x8
     - `LVDS_UART_TX_FIFO_POKE`_
     - Buffers UART TX data
     - 0x00000000
   * - 0xC
     - `LVDS_UART_TX_SEND_POKE`_
     - Enables UART transmission of FIFO data
     - 0x00000000
   * - 0x10
     - `LVDS_UART_RX_FIFO_PEEK`_
     - Buffers UART RX data
     - 0x00000000

|

LVDS_UART_EN_POKE
~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:1]
     - RESERVED
   * - [0]
     - | '1' : Enable channel
       | '0' : Disable channel

LVDS_UART_RATE_POKE
~~~~~~~~~~~~~~~~~~~~

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

LVDS_UART_TX_FIFO_POKE
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:0]
     - Write data

LVDS_UART_TX_SEND_POKE
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:1]
     - RESERVED
   * - [1]
     - | '1' : Start sending
       | '0' : Stop sending

LVDS_UART_RX_FIFO_PEEK
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 20 60
   :header-rows: 1

   * - Field
     - Description
   * - [31:0]
     - Read data
