Motivations
===========

I had decided to put this together for a number of reasons, largely driven by
the desire to improve the efficacy and quality-of-life of the FPGA development
process:

#. It promotes a **modern, Git-based FPGA workflow** presented in a wiki-format
   that fosters collaboration by encouraging code scalability and readability
#. It demonstrates a **Single-Source-of-Truth (SSOT)** by tightly coupling a 
   codebase to its documentation and requirements lifecycle management via a 
   "Docs-as-Code" approach
#. It attempts to push FPGA development practices forward by **leveraging SW tools
   and methodology** that are effective, robust, and standard in the SW world
#. It serves as a **convenient starting point template** for new FPGA projects, 
   which is intended to be simple to understand and straightforward to leverage

If you've cared enough to read this far, let's get started!

*-JR*

.. toctree::
   :maxdepth: 2
   :caption: Example Project
   :hidden:

   project/synopsis
   project/scope_of_work

.. toctree::
   :maxdepth: 2
   :caption: Requirements
   :hidden:

   requirements/high_level_reqs
   requirements/low_level_reqs
   requirements/traceability
   requirements/closure_status
   requirements/coverage_schedule
   
.. toctree::
   :maxdepth: 2
   :caption: Architecture
   :hidden:

   architecture/register_map
   architecture/modules

.. toctree::
   :maxdepth: 2
   :caption: Onboarding
   :hidden:

   onboarding/how_to
