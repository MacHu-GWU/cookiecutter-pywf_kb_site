
.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name | slugify }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name | slugify }}

.. image:: https://img.shields.io/pypi/l/{{ cookiecutter.package_name | slugify }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name | slugify }}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name | slugify }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name | slugify }}

.. image:: https://img.shields.io/badge/✍️_Release_History!--None.svg?style=social&logo=github
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/⭐_Star_me_on_GitHub!--None.svg?style=social&logo=github
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project

------

.. image:: https://img.shields.io/badge/Link-Docs-blue.svg
    :target: https://{{ cookiecutter.package_name | slugify }}.{{ cookiecutter.kb_domain }}/

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/{{ cookiecutter.package_name | slugify }}#files


Welcome to ``{{ cookiecutter.package_name }}`` Documentation
==============================================================================
.. image:: https://{{ cookiecutter.package_name | slugify }}.{{ cookiecutter.kb_domain }}/_static/{{ cookiecutter.package_name }}-logo.png
    :target: https://{{ cookiecutter.package_name | slugify }}.{{ cookiecutter.kb_domain }}/

A knowledge base site: Sphinx + furo + MyST Markdown + MyST-NB notebooks, one folder per document, documents linked by a stable random ``doc_id``, plain-text sources and ``llms.txt`` for AI agents, Pagefind search, deployed to Cloudflare Pages by GitHub Actions. The site: https://{{ cookiecutter.package_name | slugify }}.{{ cookiecutter.kb_domain }}/


.. _install:

Install
------------------------------------------------------------------------------

``{{ cookiecutter.package_name }}`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install {{ cookiecutter.package_name | slugify }}

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade {{ cookiecutter.package_name | slugify }}
