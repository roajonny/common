Motivations
===========

Hi there,

I decided to put this wiki together in the interest of improving the
efficacy and quality-of-life of FPGA engineering.

*  It demonstrates a **"Docs-as-Code" philosophy**, which tightly couples design
   code with its documentation (as code) under the same version control system
*  It promotes a **scalable, Git-based FPGA workflow** that enables code
   maintainability and mitigates the potential for siloes, or tribal knowledge
*  It modernizes FPGA development practices by **leveraging SW tools and
   methodologies** that are effective, robust, and standard in the SW world
*  It provides a **convenient template as a starting point for new FPGA
   projects,** which is intended to be simple to understand and leverage

This is to say, simply, that it **establishes an infrastructure for effortless
collaboration, encouraging the de-centralization of knowledge and writing
high-quality documentation as part of the FPGA development process.**

Lots of love went into this - I hope you find it useful! 

*-JR*

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
