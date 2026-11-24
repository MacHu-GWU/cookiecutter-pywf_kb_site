# -*- coding: utf-8 -*-

"""
Convert the seed repo into a cookiecutter template.

Input: the git-visible files of the seed repo (``CCTPL_SEED_DIR``).
Output: ``tmp/cctpl/template/``, a complete cookiecutter template root.

Rules: ``.claude/skills/cctpl-base-cn/references/03-parameterization.md``.
"""

import sys
import json
import tomllib

from cookiecutter_maker.api import Parameter, Maker

import cctpl

try:
    dir_seed = cctpl.get_seed_dir()
except cctpl.TaskError as e:
    print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)

with open(dir_seed / "pyproject.toml", "rb") as f:
    _pyproject = tomllib.load(f)
with open(dir_seed / "mise.toml", "rb") as f:
    _mise_config = tomllib.load(f)


class SeedValues:
    """Concrete values in the seed repo that become cookiecutter variables."""

    # --- identity
    package_name = "cookiecutter_pywf_kb_site_demo"
    # Also KB_SUBDOMAIN in mise.toml: the site's subdomain and the Cloudflare
    # Pages project name are the package name as a slug.
    package_name_slug = "cookiecutter-pywf-kb-site-demo"
    github_username = "MacHu-GWU"
    # Not a parameter: only scanned for leaks (UNIQUE_SEED_VALUES).
    pypi_username = "machugwu"

    # --- license
    license = "MIT"

    # --- author
    author = "Sanhe Hu"
    author_email = "husanhe@gmail.com"

    # --- versioning (read from the seed)
    version = _pyproject["project"]["version"]
    dev_python_version = _mise_config["tools"]["python"]

    # --- knowledge base site
    kb_site_title = "KB Site Demo"
    kb_domain = "sanhe.me"  # KB_DOMAIN in mise.toml
    kb_docs_port = _mise_config["env"]["KB_DOCS_PORT"]  # read from the seed

    # --- secret token fields
    github_token_field = "github.accounts.sh.users.sh.secrets.dev.value"
    codecov_token_field = "codecov_io.accounts.sh.users.sh.secrets.dev.value"
    pypi_token_field = "pypi.accounts.sh.token"
    cloudflare_account_id_field = "cloudflare.accounts.sh.account_id"
    cloudflare_pages_upload_token_field = (
        "cloudflare.accounts.sh.users.sh.secrets.cloudflare_pages_upload.value"
    )


_parts = SeedValues.version.split(".")
assert len(_parts) == 3 and all(v.isdigit() for v in _parts), (
    f"Invalid version: {SeedValues.version}"
)

_HOME_SECRET_HELP = (
    "Read https://github.com/MacHu-GWU/home_secret_toml-project to learn how to "
    "set up your tokens using home_secret.toml"
)

PARAMETERS = [
    Parameter(
        selector=[SeedValues.package_name],
        name="package_name",
        default="your_package_name",
        prompt="Your Python package name, in snake case (e.g. my_package)",
    ),
    # Also the site's subdomain (KB_SUBDOMAIN) and the Pages project name.
    Parameter(
        selector=[SeedValues.package_name_slug],
        name="package_name_slug",
        custom_placeholder="{{ cookiecutter.package_name | slugify }}",
        in_cookiecutter_json=False,
    ),
    # The seed also links to the maintainer's own projects (plugin marketplace,
    # home_secret_toml, docfly) and credits the template's author in
    # AUTHORS.rst. Those must stay literal, so the files that only mention them
    # are excluded from this parameter.
    Parameter(
        selector=[SeedValues.github_username],
        name="github_username",
        default="your_github_username",
        prompt="Your GitHub username, the owner of the new repo",
        exclude=[
            ".claude/settings.local.json.example",
            ".claude/skills/pywf-oss-base/references/01-secrets.md",
            ".claude/skills/pywf-oss-base/references/14-docfly.md",
            "AUTHORS.rst",
        ],
    ),
    # Generic value: only the project license field in pyproject.toml.
    # That field is an SPDX expression (PEP 639) and setuptools refuses to
    # build with an invalid one, so every choice is a valid SPDX expression,
    # exactly the value written to pyproject.toml.
    Parameter(
        selector=[f'license = "{SeedValues.license}"', SeedValues.license],
        name="license",
        choice=["MIT", "AGPL-3.0-or-later", "LicenseRef-Proprietary"],
        prompt="Pick a license, as an SPDX expression for pyproject.toml, see https://choosealicense.com/ for details",
        include=["pyproject.toml"],
    ),
    # AUTHORS.rst is the template author's bio, kept as is (LEGAL_RESIDUES).
    Parameter(
        selector=[SeedValues.author],
        name="author",
        default="Firstname Lastname",
        prompt="Author name for pyproject.toml",
        exclude=["AUTHORS.rst"],
    ),
    Parameter(
        selector=[SeedValues.author_email],
        name="author_email",
        default="firstname.lastname@email.com",
        prompt="Author email for pyproject.toml",
    ),
    # Generic value: only the project version line in pyproject.toml.
    Parameter(
        selector=[f'version = "{SeedValues.version}"', SeedValues.version],
        name="version",
        default="0.1.1",
        prompt="Semantic Version, in {major}.{minor}.{micro} (e.g. 0.1.1)",
        include=["pyproject.toml"],
    ),
    # Generic value: the dev Python pin in mise.toml, which the deploy workflow
    # repeats in a comment ("Must match mise.toml `python = "3.12"`").
    Parameter(
        selector=[
            f'python = "{SeedValues.dev_python_version}"',
            SeedValues.dev_python_version,
        ],
        name="dev_python_version",
        default=SeedValues.dev_python_version,
        prompt=f"Python version for local development, in {{major}}.{{minor}} (e.g. {SeedValues.dev_python_version})",
        # Anchored: the skill examples hold their own mise.toml.
        include=["/mise.toml", ".github/workflows/deploy-doc.yml"],
    ),
    # The same version in the deploy workflow, which runs without mise: the
    # setup-python input and the step name.
    Parameter(
        selector=[
            f'python-version: "{SeedValues.dev_python_version}"',
            SeedValues.dev_python_version,
        ],
        name="dev_python_version_deploy_doc",
        custom_placeholder="{{ cookiecutter.dev_python_version }}",
        in_cookiecutter_json=False,
        include=[".github/workflows/deploy-doc.yml"],
    ),
    Parameter(
        selector=[
            f"name: Setup Python {SeedValues.dev_python_version}",
            SeedValues.dev_python_version,
        ],
        name="dev_python_version_deploy_doc_step",
        custom_placeholder="{{ cookiecutter.dev_python_version }}",
        in_cookiecutter_json=False,
        include=[".github/workflows/deploy-doc.yml"],
    ),
    # Sphinx project name, home page H1 and the title of _extra/404.html.
    Parameter(
        selector=[SeedValues.kb_site_title],
        name="kb_site_title",
        default="My Knowledge Base",
        prompt="Title of the knowledge base site (sidebar, browser tab, home page H1)",
    ),
    # The site lives at https://<package-name-slug>.<kb_domain>.
    Parameter(
        selector=[SeedValues.kb_domain],
        name="kb_domain",
        default="pages.dev",
        prompt=(
            "Domain of the knowledge base site, a zone in your Cloudflare account; "
            "the site is https://<package-name-slug>.<kb_domain>. Keep pages.dev for no custom domain"
        ),
    ),
    # Generic value: `mise run view-doc` frees this port first, so two sites
    # sharing one would stop each other's server.
    Parameter(
        selector=[f'KB_DOCS_PORT = "{SeedValues.kb_docs_port}"', SeedValues.kb_docs_port],
        name="kb_docs_port",
        default=SeedValues.kb_docs_port,
        prompt=f"Local port of `mise run view-doc`, a different one for each site (e.g. {SeedValues.kb_docs_port})",
        include=["/mise.toml"],
    ),
    Parameter(
        selector=[f"${{PORT:-{SeedValues.kb_docs_port}}}", SeedValues.kb_docs_port],
        name="kb_docs_port_launch_arg",
        custom_placeholder="{{ cookiecutter.kb_docs_port }}",
        in_cookiecutter_json=False,
        include=[".claude/launch.json"],
    ),
    Parameter(
        selector=[f'"port": {SeedValues.kb_docs_port}', SeedValues.kb_docs_port],
        name="kb_docs_port_launch_port",
        custom_placeholder="{{ cookiecutter.kb_docs_port }}",
        in_cookiecutter_json=False,
        include=[".claude/launch.json"],
    ),
    Parameter(
        selector=[SeedValues.github_token_field],
        name="github_token_field",
        default="your_github_token_field",
        prompt=f"GitHub token field. {_HOME_SECRET_HELP}",
    ),
    Parameter(
        selector=[SeedValues.codecov_token_field],
        name="codecov_token_field",
        default="your_codecov_token_field",
        prompt=f"Codecov.io token field. {_HOME_SECRET_HELP}",
    ),
    Parameter(
        selector=[SeedValues.pypi_token_field],
        name="pypi_token_field",
        default="your_pypi_token_field",
        prompt=f"PyPI token field. {_HOME_SECRET_HELP}",
    ),
    Parameter(
        selector=[SeedValues.cloudflare_account_id_field],
        name="cloudflare_account_id_field",
        default="your_cloudflare_account_id_field",
        prompt=f"Cloudflare account ID field. {_HOME_SECRET_HELP}",
    ),
    Parameter(
        selector=[SeedValues.cloudflare_pages_upload_token_field],
        name="cloudflare_pages_upload_token_field",
        default="your_cloudflare_pages_upload_token_field",
        prompt=f"Cloudflare API token field (permission: Cloudflare Pages Edit). {_HOME_SECRET_HELP}",
    ),
]

# Git-visible seed files that must not enter the template.
EXCLUDE = [
    "LICENSE.txt",  # generated by hooks/post_gen_project.py
    "uv.lock",  # carries the seed's own package name; generated projects re-lock
    # Seed-only maintenance files: the seed's own changelog and the skill that
    # writes it (02-repo-layout.md, "seed repo").
    "release-history-seed-repo.rst",
    ".claude/skills/pywf-oss-changelog-seed-repo/",
]
# package-lock.json is rendered, not excluded: CI runs `npm ci` and keys its
# cache on it, and it only holds the package name as a slug.

# Seed files whose links pin the seed's own version tag (blob/<version>/...).
# check-version requires every pinned version to equal the seed version, so a
# version bump cannot leave them behind (08-versioning-and-release.md).
SEED_VERSION_PIN_FILES: list[str] = []

# Files copied byte for byte (no variable replacement).
NO_RENDER = [
    "*/vendor/**/*.*",
    "requirements.txt",
    "requirements-dev.txt",
    "requirements-doc.txt",
    "requirements-mise.txt",
    "requirements-test.txt",
    "*.jinja",
    "*.j2",
    # Sphinx HTML templates (the site's and the skill examples'). Not every
    # *.html: docs/source/_extra/404.html carries the site title.
    "**/_templates/**/*.html",
]

# Choice variables whose values send hooks or the template down different
# branches. test-template generates once per extra choice value
# (03-parameterization.md, "Choice Coverage").
CHOICE_COVERAGE = [
    "license",  # hooks/post_gen_project.py writes a different LICENSE.txt per value
]

# Files the hooks create or rewrite in a generated project. check-roundtrip
# allows them to differ from the seed.
HOOK_OUTPUTS = [
    "LICENSE.txt",  # hooks/post_gen_project.py writes it from the chosen license
]

# Seed values unique enough that any occurrence left in the template is a
# leak, scanned by check-seed-values. Generic values (license, version,
# dev_python_version, kb_docs_port) also appear legitimately elsewhere;
# check-roundtrip verifies them instead.
UNIQUE_SEED_VALUES = {
    "package_name": SeedValues.package_name,
    "package_name_slug": SeedValues.package_name_slug,
    "github_username": SeedValues.github_username,
    "pypi_username": SeedValues.pypi_username,
    "author": SeedValues.author,
    "author_email": SeedValues.author_email,
    "kb_site_title": SeedValues.kb_site_title,
    "kb_domain": SeedValues.kb_domain,
    "github_token_field": SeedValues.github_token_field,
    "codecov_token_field": SeedValues.codecov_token_field,
    "pypi_token_field": SeedValues.pypi_token_field,
    "cloudflare_account_id_field": SeedValues.cloudflare_account_id_field,
    "cloudflare_pages_upload_token_field": SeedValues.cloudflare_pages_upload_token_field,
}

_MAINTAINER_LINK = "links to the maintainer's own project, must stay literal"
_TEMPLATE_AUTHOR = "credits the template's author, not the generated project's"

# Unique seed values that may legally remain in the template, consumed by
# check-seed-values. Each entry: (seed value name, template-relative file, reason).
LEGAL_RESIDUES: list[tuple[str, str, str]] = [
    ("github_username", ".claude/settings.local.json.example", _MAINTAINER_LINK),
    ("github_username", ".claude/skills/pywf-oss-base/references/01-secrets.md", _MAINTAINER_LINK),
    ("github_username", ".claude/skills/pywf-oss-base/references/14-docfly.md", _MAINTAINER_LINK),
    ("github_username", "AUTHORS.rst", _TEMPLATE_AUTHOR),
    ("pypi_username", "AUTHORS.rst", _TEMPLATE_AUTHOR),
    ("author", "AUTHORS.rst", _TEMPLATE_AUTHOR),
]


def get_seed_context() -> dict[str, str]:
    """
    The cookiecutter context that renders the template back into the seed.
    """
    return {
        p.name: getattr(SeedValues, p.name)
        for p in PARAMETERS
        if p.in_cookiecutter_json
    }


def add_template_version(path_json) -> None:
    """
    Record the shared version (the seed's) as the private variable
    ``_template_version``: cookiecutter never prompts for it, but it is part of
    every generation's context. It goes right after the last prompted variable.
    """
    data = json.loads(path_json.read_text(encoding="utf-8"))
    result = {}
    for key, value in data.items():
        if key.startswith("_") and "_template_version" not in result:
            result["_template_version"] = cctpl.get_seed_version()
        result[key] = value
    path_json.write_text(json.dumps(result, indent=4, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    dir_stage_seed = cctpl.dir_stage / dir_seed.name
    cctpl.reset_dir(cctpl.dir_stage)
    n_files = cctpl.stage_git_visible_files(dir_seed, dir_stage_seed)
    print(f"Staged {n_files} git-visible files from {dir_seed}")

    if cctpl.dir_template.exists():
        cctpl.reset_dir(cctpl.dir_template)
        cctpl.dir_template.rmdir()
    maker = Maker(
        dir_input=dir_stage_seed,
        dir_output=cctpl.dir_template,
        parameters=PARAMETERS,
        exclude=EXCLUDE,
        no_render=NO_RENDER,
        dir_hooks=cctpl.dir_project_root / "hooks",
        verbose=False,
    )
    maker.make_template()
    add_template_version(maker.path_cookiecutter_json)
    print(f"Template written to {cctpl.dir_template}")
    return 0


if __name__ == "__main__":
    cctpl.run_task(main)
