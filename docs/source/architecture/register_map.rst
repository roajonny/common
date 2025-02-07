Register Map
============

This section enumerates the design banks and specifies the base addresses

.. list-table::
   :align: left
   :widths: 10 30 50
   :header-rows: 1

   * - Base Address
     - Name
     - Description
   * - 0x00000000
     - BANK_0
     - Provides control registers for the discombobulator mechanism
   * - 0x01000000
     - BANK_1
     - Provides status registers for the discombobulator mechanism 

BANK_0
-------

This section enumerates all of the registers in BANK_0

.. list-table::
   :align: left
   :widths: 10 30 50
   :header-rows: 1

   * - Offset
     - Name
     - Description
   * - 0x0
     - REG_0_POKE
     - The first write register of BANK_0
   * - 0x4
     - REG_1_POKE
     - The second write register of BANK_0

BANK_0_REG_0_POKE
~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 10 50
   :header-rows: 1

   * - Field
     - Description
   * - [31:16]
     - RESERVED
   * - [15:0]
     - Reset

BANK_0_REG_1_POKE
~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 10 50
   :header-rows: 1

   * - Field
     - Description
   * - [31:16]
     - RESERVED
   * - [15:0]
     - Reset

BANK_1
-------

This section enumerates all of the registers in BANK_0

.. list-table::
   :align: left
   :widths: 10 30 50
   :header-rows: 1

   * - Offset
     - Name
     - Description
   * - 0x0
     - REG_0_PEEK
     - The first read register of BANK_1
   * - 0x4
     - REG_1_PEEK
     - The second read register of BANK_1

BANK_1_REG_0_PEEK
~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 10 50
   :header-rows: 1

   * - Field
     - Description
   * - [31:16]
     - RESERVED
   * - [15:0]
     - Payload data

BANK_1_REG_1_PEEK
~~~~~~~~~~~~~~~~~

.. list-table::
   :align: left
   :widths: 10 50
   :header-rows: 1

   * - Field
     - Description
   * - [31:16]
     - RESERVED
   * - [15:0]
     - Payload data
