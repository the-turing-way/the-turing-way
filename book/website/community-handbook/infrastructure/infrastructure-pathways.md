(ch-infrastructure-pathways)=
# Pathways

The {ref}`ch-pathways` section of the book presents multiple curated sets of chapters to allow role and theme-based entry points to the book.
This feature provides a way for people to find information most relevant to them.

## Pathways package

The pathways feature is supported by the [pathways package](https://github.com/the-turing-way/pathways).
This Python package reads the book's table of contents from [`myst.yml`](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/myst.yml) and the pathways specified in [`profiles.yml`](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/profiles.yml).
It then generates injects Markdown into existing files, and generates new Markdown files to _add_ pathways pages and badges to the book.

## Building with pathways

Building the book with pathways is described in [](#ch-local-build-other-targets-pathways).

## CI and deploy

In the CI [build pathways check](https://github.com/the-turing-way/the-turing-way/blob/main/.github/workflows/ci.yml) and [Netlify build instructions](https://github.com/the-turing-way/the-turing-way/blob/main/netlify.toml) the sequence for building the book with pathways is `make deps && make pathways && make ci`.
