Motivations
===========

Hi there!

I decided to put this together largely driven by the desire to improve the
efficacy and quality-of-life of the FPGA development process, for the following
reasons (in no particular order of importance):

*  It promotes a **modern, Git-based FPGA workflow** presented in a wiki-format
   that fosters collaboration by encouraging code maintainability, readability,
   and scalability

*  It demonstrates a "Docs-as-Code" philosophy, which tightly couples design
   code with its documentation (as code) under the same version control system
   to create a **single source of truth**

*  It attempts to push FPGA development practices forward by **leveraging SW tools
   and methodology** that are effective, robust, and standard in the SW world
*  It serves as a **convenient starting point template** for new FPGA projects, 
   which is intended to be simple to understand and straightforward to leverage

If you've cared enough to read this far, let's jump to the learning
:doc:`overview/objectives` to get started.

*-JR*

.. toctree::
   :maxdepth: 2
   :caption: Overview
   :hidden:

   overview/objectives

.. toctree::
   :maxdepth: 2
   :caption: Example Project
   :hidden:

   project/synopsis
   project/scope_of_work

.. toctree::
   :maxdepth: 2
   :caption: Example Requirements
   :hidden:

   requirements/high_level_reqs
   requirements/low_level_reqs
   requirements/traceability
   requirements/closure_status
   requirements/functional_coverage
   
.. toctree::
   :maxdepth: 2
   :caption: Example Architecture
   :hidden:

   architecture/memory_map
   architecture/modules

.. toctree::
   :maxdepth: 2
   :caption: Onboarding
   :hidden:

   onboarding/tools_used
   onboarding/getting_started
   onboarding/required_tutorials
   onboarding/git_workflow
