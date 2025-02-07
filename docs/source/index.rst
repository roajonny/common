A HW-as-SW Template
===================

I decided to put this together for a few reasons, largely driven by
frustrations towards development practices I've observed in various work
environments:

#. It shows the power of **tightly coupling a codebase w/ its documentation and
   requirements,** creating a **Single-Source-of-Truth (SSOT)**
#. It's presented in a tutorial format promoting a **modern, Git-based FPGA workflow**
   that fosters collaboration by encouraging code scalability and readability
#. HW world **lacks the robust practices that are standard and commonplace in SW...**
   this is an attempt to bridge that gap and push FPGA development practices
   forward

Lastly, this serves as a convenient starting point template for new FPGA projects, 
which others can easily leverage. 

Hope this piques an interest, and thanks for reading!

**-JR**

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
