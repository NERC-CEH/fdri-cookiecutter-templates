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
