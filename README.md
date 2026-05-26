# FDRI Cookiecutter Templates

A set of [Cookiecutter](https://cookiecutter.readthedocs.io/) templates for new Python projects at UKCEH/FDRI.
Two templates live in this repo; select one with the `--directory` flag.

| Template                   | Use when                                                                                 |
|----------------------------|------------------------------------------------------------------------------------------|
| [`pypackage/`](pypackage/) | Building a Python library - something other projects import, or a tool published to PyPI |
| [`pyservice/`](pyservice/) | Building a Python service deployed to FDRI AWS - runs as a container                     |

## Quick start

Python package:

```bash
uvx cookiecutter gh:NERC-CEH/fdri-cookiecutter-templates --directory=pypackage
```

Python service:

```bash
uvx cookiecutter gh:NERC-CEH/fdri-cookiecutter-templates --directory=pyservice
```

## Documentation

Full documentation: https://nerc-ceh.github.io/fdri-cookiecutter-templates/

## Repo notes

- Shared files identical across templates live in [`_shared/`](_shared/) and are symlinked into each template.

## Releasing a new version

1. **On a branch** — bump the version and write the changelog:

   ```bash
   make bump-patch   # 1.0.0 → 1.0.1
   make bump-minor   # 1.0.0 → 1.1.0
   make bump-major   # 1.0.0 → 2.0.0
   ```

   This updates `pyproject.toml`, commits the version change, and creates a `CHANGELOG/<version>.md` stub. Fill in the changelog, commit, and open a PR as normal.

2. **After merging to `main`** — pull and create the release:

   ```bash
   git checkout main && git pull
   make release
   ```

   This tags the merged commit on `main`, pushes the tag, and creates a GitHub release using the changelog as release notes.
