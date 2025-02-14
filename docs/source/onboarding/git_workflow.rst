Git Workflow
============

Here's a fun `Git tutorial <://learngitbranching.js.org/>`_, as this guide
assumes reasonable familiarity.

Branching Model
---------------

This workflow is somewhere between legacy-`Gitflow
<https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_
and the more modern `trunk-based development
<https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development>`_,
consisting of three "core" branches, two of which are build targets for
a `CI/CD <https://www.redhat.com/en/topics/devops/what-is-ci-cd>`_ pipeline:

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

The CI/CD pipeline is configured to generate the FPGA image, the documentation,
and run any self-checking testbench simulations (if they exist) upon merges to
``develop`` or ``main``.

|

Naming developer branches
~~~~~~~~~~~~~~~~~~~~~~~~~

To encourage consistency that scales with team size, developer branches should
adhere to the following convention for naming their branches:
``<feature/debug>-<description>_<developer initials>``

|

Visualizing the workflow
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
      merge feature-my_feature_jr id: "CICD_build_1" type: HIGHLIGHT
      branch debug-made_mistake_jr
      commit
      checkout develop
      merge debug-made_mistake_jr id: "CICD_build_2" type: HIGHLIGHT
      checkout main
      merge develop tag:"v1.0" id: "CICD_build_3" type: HIGHLIGHT

.. note::

   Naturally, every merge junction on ``develop`` would be buildable
   from an FPGA image/documentation standpoint, which makes those commits
   stable ground to "roll back" to in the event of a debug effort

|

Staying up-to-date
~~~~~~~~~~~~~~~~~~

Feature branches are relatively long-lived, so developers should be pulling
from ``develop`` into their ``feature`` / ``debug`` branches once a day
(ideally in the morning) to make sure their branches stay up-to-date with
remote, reducing the likelihood of `merge conflicts
<https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts>`_.

|

Making a pull request
~~~~~~~~~~~~~~~~~~~~~

When a developer is ready, they initiate a pull request to the lead, and the
lead merges their ``feature`` branch into ``develop`` if the following
conditions are met:

#. Developer ensured the FPGA design is in a buildable state (team lead can
   checkout the developer's branch and confirm by running the build script for the synthesis
   tool)
#. Developer updated the documentation and can point to it (team lead can
   build and view it from the developer's branch)
