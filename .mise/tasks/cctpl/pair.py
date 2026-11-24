# -*- coding: utf-8 -*-

"""
Facts that belong to this tpl repo + seed repo pair, for the generic task code.

Everything else under ``.mise/tasks/`` works for any pair, except the
parameterization declarations in ``make_template.py``. When this family is
forked to another pair (/cctpl-fork-cn), this file is rewritten as a whole.

Where every pair-specific fact lives:
``.claude/skills/cctpl-base-cn/references/02-repo-layout.md``, "Where Facts Live".
"""

# --- GitHub coordinates of the tpl repo (publish, verify, README)
GITHUB_OWNER = "MacHu-GWU"
GITHUB_REPO = "cookiecutter-pywf_kb_site"

# --- the template dir: the project folder name inside the template
TEMPLATE_DIR_NAME = "{{ cookiecutter.package_name }}-project"

# --- generated projects (06-verification.md, L4, L5 and Local Trial)

# The cookiecutter variable holding the Python version a generated project uses.
PYTHON_VERSION_VARIABLE = "dev_python_version"

# How L4 / L5 install a generated project and run its tests, without mise.
# Run in the project dir after "uv venv --python <version>".
INSTALL_COMMAND = ["uv", "sync", "--all-extras"]
# The sphinx-myst-kb-site skill ships tests of its scripts; the seed runs them too.
TEST_COMMAND = [".venv/bin/pytest", "tests", ".claude/skills/sphinx-myst-kb-site/tests", "-q"]

# The generated project's own mise tasks that the Local Trial runs, in order.
# build-doc runs lint-doc, Sphinx and Pagefind (npm install, no secret). Not
# lint: its example check looks for the nearest .git, and the trial project
# has none, so it would find this tpl repo instead.
PROJECT_TASKS = ["venv-create", "inst", "cov", "build-doc"]
