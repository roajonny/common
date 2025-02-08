Motivations
===========

I had decided to put this together for a number of reasons, largely driven 
by the desire to improve the efficacy and quality-of-life of the FPGA development 
process:

#. It promotes a **modern, Git-based FPGA workflow** presented in a wiki-format
   that fosters collaboration by encouraging code scalability and readability
#. It demonstrates a **Single-Source-of-Truth (SSOT)** by tightly coupling a 
   codebase to its documentation and requirements lifecycle management via a 
   "Docs-as-Code" approach
#. It attempts to push FPGA development practices forward by **leveraging SW tools
   and methodology** that are robust, commonplace, and effective in the SW world
#. It serves as a **convenient starting point template** for new FPGA projects, 
   which is intended to be simple to understand and straightforward to leverage

If this piques your interest, let's get started!

*-JR*

.. toctree::
   :maxdepth: 2
   :caption: Project
   :hidden:

   project/introduction

.. toctree::
   :maxdepth: 2
   :caption: Requirements
   :hidden:

   requirements/key_reqs
   requirements/derived_reqs
   
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
