(ch-infrastructure)=
# Infrastructure

The Turing Way consists of many parts which need to work together to make sure the book can be built, renders correctly and is available on the internet.
There are processes to build, deploy and ensure the quality of the book.
There is also configuration which may direct those processes or the site.
While infrastructure can be defined in many ways, collectively we call these things infrastructure.

Some examples include:

- Instructions to build the site from the source files, both {ref}`locally<ch-local-build>` and [for deployment](https://github.com/the-turing-way/the-turing-way/blob/main/netlify.toml)
- {term}`Continuous Integration` tasks to look for problems in the source
- Redirect rules to help site navigation and avoid '404 Not Found' errors
- {term}`Hosting` and {term}`DNS`

Some of this is controlled by data in the repository itself.
For example, quality control processes to ensure the book will build and help maintain accessibility standards are part of the {ref}`Continuous Integration<rr-ci>` process and described in the [.github/workflows/](https://github.com/the-turing-way/the-turing-way/tree/main/.github/workflows) directory.

Some aspects may not be declared in the repository.
For example, hosting is provided by Netlify which holds some of its own configuration.

This section of the book describes the infrastructure that _The Turing Way_ uses.
The aim is to demystify how things work, ensure that the infrastructure is described openly, and to help people contribute to infrastructure.
