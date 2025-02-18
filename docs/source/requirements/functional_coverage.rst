Functional Coverage
===================

.. mermaid::

   %%{init: {'theme':'dark'}}%%
   xychart-beta
       x-axis "Time" [t0, t1, t2, t3, t4]
       y-axis "Functional Coverage (%)" 0 --> 100
       bar [0, 20, 40, 60, 100]
       line [0, 20, 40, 60, 100]

|

.. note::

   Functional coverage graphs are useful for designers to estimate their design time,
   and help account for two situations:

   * "We didn't know about that"
   * "We didn't think about that"

   These two are, by definition, hard to time-box and conceptually malleable as
   management risks during project planning, and later materialize as technical
   risks during development

   Presenting estimates in such a fashion helps compartmentalize the
   development into phases, and buffers for these occasions
