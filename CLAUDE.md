# CLAUDE.md

This is the **tpl repo** of a cookiecutter template for knowledge base sites: a Python project whose Sphinx + MyST docs (one folder per document, stable `doc_id` links, `llms.txt` for AI agents, Pagefind search) deploy to Cloudflare Pages. The template is never edited directly: it is generated from a runnable **seed repo** (path: `CCTPL_SEED_DIR` in `mise.toml`) and published from here.

All maintenance rules live in the `cctpl-*-cn` skill family under `.claude/skills/`. Start with `cctpl-base-cn/SKILL.md`; it is the single source of truth and says which invoker fits which job:

| Job | Skill |
| :--- | :--- |
| Change the template (content or mechanism) | `/cctpl-change-cn` |
| Add, change, or remove a cookiecutter variable | `/cctpl-add-param-cn` |
| Regenerate the template from the seed and run all checks | `/cctpl-sync-cn` |
| Try a generated project locally | `/cctpl-try-cn` |
| Write this repo's changelog section for the current version | `/cctpl-changelog-cn` |
| Prepare a release (user only) | `/cctpl-release-cn` |
| Verify the published template (user only) | `/cctpl-verify-cn` |
| Copy this skill family to another tpl / seed repo pair, once (user only) | `/cctpl-fork-cn` |

Rules that hold even before a skill is loaded (details: `cctpl-base-cn/references/04-safety-rules.md`):

- Never run git write operations, `mise run publish-template` or `mise run publish-presets`; print the commands for the user instead.
- Never edit `cookiecutter.json`, `{{ cookiecutter.package_name }}-project/` or `README.rst` by hand; change the seed (or the parameterization) and run `mise run sync`.
- Never edit the version here: the seed and this repo share one version, its only source is the seed's `pyproject.toml`, and `mise run sync` copies it here.

## Current Status

Open items for this pair (keep this short; delete items when done):

- None yet.
