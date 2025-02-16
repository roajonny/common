Design Modules
==============

UART
----

This section describes the generic UART module which is re-used for both
channels 1 & 2.

|

Block Diagram
~~~~~~~~~~~~~

.. image:: ./images/uart_arch.svg
   :align: center

|

TX State Machine
~~~~~~~~~~~~~~~~

.. mermaid::

   stateDiagram-v2
       direction LR
       [*] --> IDLE: POR
       IDLE --> TX_RUNNING: i_tx_wr_en = '1'
       TX_RUNNING --> DONE: w_tx_done = '1'
       DONE --> IDLE

|

RX State Machine
~~~~~~~~~~~~~~~~

.. mermaid::

   stateDiagram-v2
       direction LR
       [*] --> IDLE: POR
       IDLE --> RX_RUNNING: w_start_bit_detected = '1'
       RX_RUNNING --> DONE: w_rx_done = '1'
       DONE --> IDLE
