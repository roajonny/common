High-Level / Key
================

.. needtable::
   :columns: id; title; tags; status
   :tags: HL
   :show_filters:

|

.. note::
   
   *High-Level Requirements* are the customer requirements which serve as the
   "handshake" between the customer and the design team about what the product
   is unambiguously supposed to do

   *Key Requirements* could be requirements that are received from a system
   specification which need to be flowed down to FPGA requirements proper

   Regardless of what nomenclature convention is adopted for a project, both
   likely have flowdown to their respective complementary requirements in the
   :doc:`low_level_reqs` section

High-Level / Key (Full Descriptions)
------------------------------------

|

.. req:: UART over RS422
   :id: HL_001
   :status: open
   :links: T_HITL
   :tags: comms; HL

   .. tabs::

      .. tab:: Description
   
        The FPGA *shall* provide a UART w/ an additional frame-synchronization
        signal targeting an external RS422 IC which is controllable by software
        over PCI-Express

      .. tab:: Verification Method

        Traceable to *Low-Level / Derived* requirements verification

|

.. req:: UART over LVDS
   :id: HL_002
   :status: in-progress
   :links: T_HITL
   :tags: comms; HL

   .. tabs::

      .. tab:: Description
   
        The FPGA *shall* provide a UART w/ an additional frame-synchronization
        signal targeting an external LVDS IC which is controllable by software
        over PCI-Express

      .. tab:: Verification Method

        Traceable to *Low-Level / Derived* requirements verification
