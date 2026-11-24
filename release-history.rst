.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.0.0 (2026-11-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Seed repo changes: `1.0.0 (2026-11-22) <https://github.com/MacHu-GWU/cookiecutter_pywf_kb_site_demo-project/blob/1.0.0/release-history-seed-repo.rst#100-2026-11-22>`__

**Features and Improvements**

- First release of the knowledge base site template, generated from the seed repo ``cookiecutter_pywf_kb_site_demo-project``.
- Variables: ``package_name``, ``github_username``, ``license`` (``MIT``, ``AGPL-3.0-or-later``, ``LicenseRef-Proprietary``), ``author``, ``author_email``, ``version``, ``dev_python_version``, ``kb_site_title``, ``kb_domain``, ``kb_docs_port``, and the ``home_secret.toml`` fields ``github_token_field``, ``codecov_token_field``, ``pypi_token_field``, ``cloudflare_account_id_field``, ``cloudflare_pages_upload_token_field``.
- The site is served at ``https://<package-name-slug>.<kb_domain>``; keep the default ``kb_domain = pages.dev`` for no custom domain.
- ``hooks/pre_gen_project.py`` validates the input; ``hooks/post_gen_project.py`` writes the ``LICENSE.txt`` of the chosen license.
- Preset ``preset/sanhe``: personal defaults for the author, GitHub account, ``kb_domain = sanhe.me`` and the secret fields.
