# FDRI Cookiecutter Templates

This repo provides [Cookiecutter](https://cookiecutter.readthedocs.io/) templates for starting new Python projects at
UKCEH/FDRI.

## What is a Cookiecutter template?

[Cookiecutter](https://cookiecutter.readthedocs.io/) is a tool that generates a new project from a template. You run one
command, answer a few prompts (project name, author, etc.), and it produces a fully-structured project directory - ready
to use, with all the boilerplate already in place.

These templates encode the tooling choices, CI pipelines, and project conventions agreed on for
FDRI Python projects. The goal is that every new project starts from the same solid foundation, so you spend time
writing code rather than configuring tools.

## What do the templates give you?

Both templates come with:

- **`uv`** for dependency management and packaging
- **`ruff`** for linting and formatting
- **`pytest`** and **`coverage`** for testing
- **`pyright`** for type checking
- **`make`** targets to run all of the above with one command
- **GitHub Actions** CI that runs on every PR
- A standard project layout, changelog, and citation metadata

## Which template should I use?

Two templates live in this repo. Choose based on what you're building:

| Template                          | Use when                                                                                 | Quick start                                                                      |
|-----------------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [`pypackage`](pypackage/usage.md) | Building a Python library - something other projects import, or a tool published to PyPI | `uvx cookiecutter gh:NERC-CEH/fdri-cookiecutter-templates --directory=pypackage` |
| [`pyservice`](pyservice/usage.md) | Building a Python service deployed to FDRI AWS - runs as a container                     | `uvx cookiecutter gh:NERC-CEH/fdri-cookiecutter-templates --directory=pyservice` |

If you are unsure, ask!

## Shared guides

- [Prerequisites](prerequisites.md) - uv, Python 3.12+, make, and git (required by both templates)
- [After template generation](after-generation.md) - standard setup steps, citation metadata, writing docs

## pypackage docs

- [Usage](pypackage/usage.md) - prerequisites, prompts, post-generation steps
- [GitHub setup](pypackage/usage-github.md) - `gh` CLI, account auth, PyPI publishing
- [Codeberg setup](pypackage/usage-codeberg.md) - `CODEBERG_TOKEN`, account setup
- [Git flows and branch protection](pypackage/git-flows.md) - picking a branching strategy
- [Releasing](pypackage/releasing.md) - bumping versions, tagging, publishing to PyPI
- [Troubleshooting](pypackage/troubleshooting.md) - common issues and fixes

## pyservice docs

- [Usage](pyservice/usage.md) - prerequisites, prompts, post-generation steps
- [GitHub and AWS setup](pyservice/usage-github.md) - `gh` CLI, AWS OIDC secrets
- [Git flow](pyservice/git-flows.md) - `staging -> production` model
- [Releasing](pyservice/releasing.md) - bumping versions, deploying to production

## Repo notes

- [Design decisions](design_decisions.md) - why we made the choices we did
