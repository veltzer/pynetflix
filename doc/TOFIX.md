# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pynetflix/main.py:15-18` - the only endpoint, `list_remove`, is a stub: it prints a hardcoded Netflix URL and `"POST"` and never sends a request; the `--id` it requires (`ConfigId`, `src/pynetflix/configs.py:9`) is never read. The package is published to PyPI as "Development Status :: 4 - Beta" (`pyproject.toml:25`) while doing nothing. Implement the request (cookies via `browser_cookie3`, the show id in the payload) or downgrade the classifier to `1 - Planning` and say so in the README.

## Medium

- `pyproject.toml:38` - `browser_cookie3` is a runtime dependency but is never imported anywhere in `src/`; drop it until the code uses it.
- `config/project.lua:3-8` - keywords `google`, `youtube`, `playlist`, `videos` are copied from a YouTube project and do not describe a Netflix toolkit (same list in `pyproject.toml:18-23`); replace with e.g. `netflix`, `streaming`, `cli`.
- `doc/design.txt`, `doc/links.txt`, `doc/quota.txt`, `doc/tests.txt`, `doc/TODO.txt` - all five files are about the YouTube Data API (quota, video ids, watch-later scraping) and have nothing to do with this package; they appear copied from a YouTube tool. Delete them or move them to the YouTube repo they belong to.

## Low

- `.yamllint.yaml` - the shared yamllint config is present but `rsconstruct.toml` has no `[processor.yamllint]`, so `.github/*.yml` is never yamllinted. Add `[processor.yamllint]` with `src_dirs = [".github"]` as in the repos that use it (e.g. `virtual-windows/rsconstruct.toml`).
- `src/pynetflix/main.py:16` - the endpoint URL embeds a build-specific Shakti API version (`v342de553`) that Netflix rotates; when implementing, discover it at run time instead of hardcoding it.
