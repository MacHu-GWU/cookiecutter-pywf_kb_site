.. This file is the source of README.rst. Do not edit README.rst by hand:
   apply-template (mise run sync) renders it from this file.

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/cookiecutter-pywf_kb_site/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/cookiecutter-pywf_kb_site


``cookiecutter-pywf_kb_site``
==============================================================================


Overview
------------------------------------------------------------------------------
This template generates a knowledge base site as a Python project: write documents in Markdown, reStructuredText or Jupyter notebooks, and every push to ``main`` publishes them to `Cloudflare Pages <https://pages.cloudflare.com/>`_ at ``https://<package-name-slug>.<kb_domain>``.

**Key Features:**

- **Knowledge base site**: `Sphinx <https://www.sphinx-doc.org/>`_ with furo, MyST Markdown and MyST-NB notebooks, sphinx-design and mermaid; one folder per document
- **Stable links**: every document has a random ``doc_id`` and is linked only by it; ``/p/<doc_id>`` follows the document wherever its folder moves
- **Readable by AI agents**: each document's plain text at ``p/<doc_id>.md``, an ``llms.txt`` index, and an "AI Reader" link on every page
- **Search and hosting**: `Pagefind <https://pagefind.app/>`_ search, deployed to Cloudflare Pages by GitHub Actions (a custom domain or ``pages.dev``)
- **Modern tooling**: `mise-en-place <https://mise.jdx.dev/>`_ tasks and `uv <https://docs.astral.sh/uv/>`_, with GitHub Actions tests and Codecov for the Python side
- **AI ready**: ships Claude Code skills to plan, write and migrate documents, to maintain the site, and to answer questions from it


Disclaimer
------------------------------------------------------------------------------
The practices in this template come from the knowledge bases I write and maintain for myself, built on the toolchain behind `over 150 open source Python libraries <https://pypi.org/user/machugwu/>`_. They work well for me; please use them at your own discretion.


Usage
------------------------------------------------------------------------------
Enter the following command to use the latest template version:

.. code-block:: bash

    pip install "cookiecutter>=2.6.0,<3.0.0" && cookiecutter https://github.com/MacHu-GWU/cookiecutter-pywf_kb_site

To use a specific released version (see the `full list of releases <https://github.com/MacHu-GWU/cookiecutter-pywf_kb_site/releases>`_):

.. code-block:: bash

    cookiecutter https://github.com/MacHu-GWU/cookiecutter-pywf_kb_site --checkout tags/${version}

For example, to use ``1.0.0``, the latest version:

.. code-block:: bash

    cookiecutter https://github.com/MacHu-GWU/cookiecutter-pywf_kb_site --checkout tags/1.0.0

You'll then be prompted to provide the following information (defaults in parentheses):

.. code-block:: bash

    [1/15] Your Python package name, in snake case (e.g. my_package) (your_package_name): your_package_name
    [2/15] Your GitHub username, the owner of the new repo (your_github_username): your_github_username
    [3/15] Pick a license, as an SPDX expression for pyproject.toml, see https://choosealicense.com/ for details
      1 - MIT
      2 - AGPL-3.0-or-later
      3 - LicenseRef-Proprietary
      Choose from [1/2/3] (1): 1
    [4/15] Author name for pyproject.toml (Firstname Lastname): Firstname Lastname
    [5/15] Author email for pyproject.toml (firstname.lastname@email.com): firstname.lastname@email.com
    [6/15] Semantic Version, in {major}.{minor}.{micro} (e.g. 0.1.1) (0.1.1): 0.1.1
    [7/15] Python version for local development, in {major}.{minor} (e.g. 3.12) (3.12): 3.12
    [8/15] Title of the knowledge base site (sidebar, browser tab, home page H1) (My Knowledge Base): My Knowledge Base
    [9/15] Domain of the knowledge base site, a zone in your Cloudflare account; the site is https://<package-name-slug>.<kb_domain>. Keep pages.dev for no custom domain (pages.dev): pages.dev
    [10/15] Local port of `mise run view-doc`, a different one for each site (e.g. 47231) (47231): 47231
    [11/15] GitHub token field. Read https://github.com/MacHu-GWU/home_secret_toml-project to learn how to set up your tokens using home_secret.toml (your_github_token_field): your_github_token_field
    [12/15] Codecov.io token field. Read https://github.com/MacHu-GWU/home_secret_toml-project to learn how to set up your tokens using home_secret.toml (your_codecov_token_field): your_codecov_token_field
    [13/15] PyPI token field. Read https://github.com/MacHu-GWU/home_secret_toml-project to learn how to set up your tokens using home_secret.toml (your_pypi_token_field): your_pypi_token_field
    [14/15] Cloudflare account ID field. Read https://github.com/MacHu-GWU/home_secret_toml-project to learn how to set up your tokens using home_secret.toml (your_cloudflare_account_id_field): your_cloudflare_account_id_field
    [15/15] Cloudflare API token field (permission: Cloudflare Pages Edit). Read https://github.com/MacHu-GWU/home_secret_toml-project to learn how to set up your tokens using home_secret.toml (your_cloudflare_pages_upload_token_field): your_cloudflare_pages_upload_token_field

This will generate a repository structure similar to `cookiecutter_pywf_kb_site_demo-project <https://github.com/MacHu-GWU/cookiecutter_pywf_kb_site_demo-project>`_.

Once generated, navigate to your project directory and explore the available automation tasks:

.. code-block:: bash

    cd your_package_name-project
    mise tasks ls  # List all available tasks


Project Maintainer Note
------------------------------------------------------------------------------
**Project Architecture:**

- **Seed Repository**: `cookiecutter_pywf_kb_site_demo-project <https://github.com/MacHu-GWU/cookiecutter_pywf_kb_site_demo-project>`_ - A concrete, runnable project used as the source for template generation
- **Cookiecutter Template**: `cookiecutter-pywf_kb_site <https://github.com/MacHu-GWU/cookiecutter-pywf_kb_site>`_ - This repository

**Maintenance Workflow:**

This template is maintained using a "reverse engineering" approach, driven by Claude Code skills (``.claude/skills/cctpl-*-cn``):

1. Make changes in the Seed project (``cookiecutter_pywf_kb_site_demo-project``)
2. In the Seed, bump the version and record the changes in its own ``release-history-seed-repo.rst``. The Seed and this template share one version number, and the Seed's ``pyproject.toml`` is its only source
3. Run ``mise run e2e``: it converts the Seed into a template, checks it, applies it to this repo (version included), then generates a project and runs its tests and docs build
4. Commit and push the Seed, then tag it with ``mise run publish`` and ``mise run release`` in the Seed
5. Run ``/cctpl-release-cn`` to write this repo's changelog section, which links to the Seed's section of the same version, then ``mise run publish-template`` to publish the template to GitHub. A published version is never overwritten
6. Run ``/cctpl-verify-cn`` to verify the published template

**Toolchain:**

- **mise-en-place**: Task runner and tool version manager
- **uv**: Fast Python package installer and resolver
- **cookiecutter-maker**: Reverse-engineering tool that converts concrete projects into templates

For the full maintenance specification, see `cctpl-base-cn <./.claude/skills/cctpl-base-cn/SKILL.md>`_.
