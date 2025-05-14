(ch-infrastructure-pathways)=
# Pathways

The [#ch-pathways]() section of the book presents, for different roles, a set of curated sections of the book.
This provides a way for people to find information most relevant to them.

## Pathways package

The pathways feature is supported by the [pathways package](https://github.com/the-turing-way/pathways).
This Python package reads the book's table of contents from [`myst.yml`](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/myst.yml) and the pathways specified in [`profiles.yml`](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/profiles.yml).
It then generates injects Markdown into existing files, and generates new Markdown files to _add_ pathways pages and badges to the book.

## Building with pathways

Because the pathways package adds and modifies Markdown files, it must be run before building the book with `jupyter-book` for the pathways to feature.
Also, once run it does not need to be run again.
If the pathways have been changed it is best to clean the untracked files and run pathways again.

The [Makefile](https://github.com/the-turing-way/the-turing-way/blob/main/book/Makefile) has the `pathways` target which runs the pathways script.
To build the book with pathways you could therefore run

```console
$ make pathways
$ make serve
```

## CI and deploy

In the CI [build pathways check](https://github.com/the-turing-way/the-turing-way/blob/main/.github/workflows/ci.yml) and [Netlify build instructions](https://github.com/the-turing-way/the-turing-way/blob/main/netlify.toml) the sequence for building the book with pathways is `make deps && make pathways && make ci`.
