Git Workflow
============

Here's a fun `Git tutorial <://learngitbranching.js.org/>`_ - this guide
assumes familiarity.

Branching Model
---------------

This workflow is somewhere between legacy-`Gitflow
<https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_
and the more modern `trunk-based development
<https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development>`_,
consisting of three "core" branches, two of which are build targets for
a `CI/CD <https://www.redhat.com/en/topics/devops/what-is-ci-cd>`_ pipeline.

|

Core branches summarized
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 20 50 50 20
   :header-rows: 1

   * - Branch Name
     - Managed By
     - Description
     - Branch Protections
     - CI/CD Build Target
   * - ``main``
     - Team Lead
     - Used for releases; all commits are merged from "develop" and tagged
     - Only team lead can merge ``develop`` into ``main``
     - Yes
   * - ``develop``
     - Team Lead
     - Branched off ``main`` at conception; primary merge target for ``feature``
       / ``debug`` branches
     - All ``feature`` or ``debug`` merges gated behind pull requests to team
       lead
     - Yes
   * - ``feature`` or ``debug``
     - Developers
     - Branched off ``develop`` for adding new logic or debugging logic that finds its
       way into ``develop`` 
     - None
     - No

|

Naming developer branches
~~~~~~~~~~~~~~~~~~~~~~~~~

Developers should adhere to the following convention when naming their
branches: 

``<feature/debug>-<description>_<developer initials>``

This convention ensures the workflow's consistency and scales with team size.

|

Staying up-to-date
~~~~~~~~~~~~~~~~~~

Feature branches are relatively long-lived, so developers should be ``git
pull``/``git fetch``-ing the latest changes from ``origin/develop`` to their
local ``develop`` and merging it into their ``feature``/``debug`` branches at
least once a day (ideally in the morning), to reduce the likelihood of `merge
conflicts
<https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts>`_.

|

Making a pull request
~~~~~~~~~~~~~~~~~~~~~

When a developer is ready, they initiate a pull request to the lead, and the
lead merges their ``feature`` branch into ``develop`` if the following
conditions are met:

#. The developer ensured the FPGA design is in a buildable state (team lead can
   checkout the developer's branch and confirm by running the build script for the synthesis
   tool)
#. The developer updated the documentation and can point to it (team lead can
   build and view it from the developer's branch)

|

Visualizing the topology
~~~~~~~~~~~~~~~~~~~~~~~~

.. mermaid::

   gitGraph
      commit
      branch develop
      checkout develop
      branch feature-my_feature_jr
      commit
      commit
      checkout develop
      merge feature-my_feature_jr id: "dev_CICD_build_1" type: HIGHLIGHT
      branch debug-made_mistake_jr
      commit
      checkout develop
      merge debug-made_mistake_jr id: "dev_CICD_build_2" type: HIGHLIGHT
      checkout main
      merge develop tag:"v1.0" id: "main_CICD_build_1" type: HIGHLIGHT

The CI/CD pipeline is configured to carry out the following tasks upon merges to
``develop`` or ``main``:

#. Invokes the synthesis tool to run the FPGA design's build script
#. Invokes Sphinx to generate the documentation
#. Invokes the simulator to run self-checking simulations (if any)

.. note::

   Naturally, every merge junction on ``develop`` is guaranteed to be buildable as
   a result of this model, which makes those commits stable ground to "roll back"
   to in the event of a debug effort
