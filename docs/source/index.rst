A HW-as-SW Template
===================

I decided to put this together for a few reasons, largely driven by the desire
to improve the efficacy and quality-of-life of the FPGA development process:

#. It promotes a **modern, Git-based FPGA workflow** presented in tutorial-format
   that fosters collaboration by encouraging code scalability and readability
#. It shows the power of a **Single-Source-of-Truth (SSOT)** by tightly coupling a 
   codebase to its documentation/requirements via a "Docs-as-Code" approach
#. It attempts to push FPGA development practices forward by **leveraging SW tools
   and methodology** that are standard, commonplace, and effective in the SW world

Lastly, this serves as a convenient starting point template for new FPGA projects, 
which others can easily leverage. 

Hope this piques your interest, and thanks for reading!

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
