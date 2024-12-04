(ch-local-build)=
# Build the Book Locally

## Why build locally

It is useful to preview changes you have been working on as you go on your local machine.
You can be confident that changes you have made are accurate and as intended and it will likely be quicker than waiting for a preview to be build from a pull request.
You can replicate the build process using [Make](rr-make) and [Jupyter Book](https://jupyterbook.org/en/stable/intro.html).

## Prerequisites

We will be using the command line throughout this guide.
You will need to use a terminal emulator to follow.

You will also need to install Python3.
You can check which specific version of Python3 the build uses in [netlify.toml](https://github.com/the-turing-way/the-turing-way/blob/main/netlify.toml).
However, versions close to that version are also likely to work.

Other command line tools you will need are,

- `git`
- `make`

## Step-by-step Guide

### Clone The Repository

```console
git clone https://github.com/the-turing-way/the-turing-way
```

````{note}
The repository is quite large and cloning may take a long time on slower internet connections.
You can use [partial clones](https://github.blog/2020-12-21-get-up-to-speed-with-partial-clone-and-shallow-clone/#).
Specifically, focusing on blobless clones, involves utilizing the `--filter=blob:none` option in the git clone command.

By using `--filter=blob:none`, the initial git clone operation downloads all reachable commits and trees, while blobs (file contents) for commits are only downloaded when performing a git checkout.

Here's the command to create a blobless clone of the book:

```console
git clone --filter=blob:none https://github.com/the-turing-way/the-turing-way.git
```
````

### Create a Virtual Environment

Navigate into the repository using the command `cd the-turing-way`; the `cd` command means change directory.
Create a virtual environment using Python,

```console
$ python3 -m venv ./venv
```

Next, active the virtual environment,

```console
$ source ./venv/bin/activate
```

Your prompt may now start with `(venv)`, for example `(venv) user@host$`.
Using the virtual environment means we can install _The Turing Way's_ dependencies without interfering with other packages or libraries you might be using.
That will be explained in more depth in [a later section](#why-we-recommend-using-a-virtual-environment).

### Install the Dependencies

The next steps use {term}`Makefile`.
The Makefile contains instructions to build a set of "targets".
That way we can easily run the same commands repeatedly, and in different environments, without needing to remember all the parameters.
It is easiest to change into the directory containing the Makefile,

```
$ cd book
```

Install the build dependencies into your virtual environment,

```console
$ make deps
```

### Build the Book

You are now ready to build the book.
You can build the book with,

```console
$ make book
```

The output of the build process will provide output such as below that demonstrate how you can view the book locally,

```text
===============================================================================

Finished generating HTML for book.
Your book's HTML pages are here:
    _build/html/
You can look at your book by opening this file in a browser:
    _build/html/index.html
Or paste this line directly into your browser bar:
    file:///<path to repository>/book/website/_build/html/index.html

===============================================================================
```

Open `index.html` in your web browser to look at your local build.

## Building Previews for Different Branches

The build process will use the source files from whatever branch you have checked out.
If you have just cloned the repository, that will be the `main` branch.

To build another branch, for example a feature branch you are working on you first switch to that branch,

```console
$ git switch mybranch
$ make book
```

## Clean Up After a Build

The build process generates a lot of files.
Clearing these files to force a build from scratch may reveal errors and warnings that wouldn't be raised otherwise.

To remove the outputs of builds use the `clean` target,

```console
$ make clean
```

### Other Targets

#### Strict Build

The `strict` target is useful for debugging.
It will make any warnings raise an error, but also continue the build.
That way, all warnings should be presented to you as errors.
Run the strict build with,

```console
$ make strict
```

#### Pathways Build

_The Turing Way_ has curated user pathways, collecting a series of recommended chapters for different reader types.
The [pathways program](https://github.com/the-turing-way/pathways) generates extra Markdown files to add the pathways to the book.
The `build` target does not generate these files, so a clean build (`make clean && make build`) will not have pathways.
To build the book with pathways, use the `pathways` target,

```console
$ make pathways
```

This will generate the pathways files then build the book.
This is the build of the book which is deployed to the website.

## Why We Recommend Using a Virtual Environment

In the [step-by-step guide](#step-by-step-guide), we used Jupyter Book to build the Turing Way.
For this program to work as intended you will need a Python installation and set of dependencies on your machine.

If you want to use other Python projects, they will also have their own dependencies.
You may encounter cases where the dependencies of two packages conflict with each other and it becomes difficult, or impossible, to satisfy both sets of dependencies simultaneously.

Using virtual environments minimises dependency problems.
It allows us to install Python packages and all their dependencies in separate, dedicated directories.
That way, packages with incompatible dependencies are not a problem because they each have a independent installations and do not share resources.

```{figure} https://imgs.xkcd.com/comics/python_environment.png
---
height: 487px
name: python-environment
alt: >
  A humorous, black and white flowchart from XKCD depicting the complexity of managing different Python environments on a computer.
  It shows a tangled web of arrows and lines connecting various versions of Python installed through different methods such as Homebrew, Anaconda, and binaries from Python.org.
  There are also references to different tools and paths like PIP, PYTHONPATH, and system PATH, that add to the confusion.
  The paths weave in and out of local folders on a computer.
  Some of them are noted to be owned by root, making them harder to manage.
  The illustration is annotated with bemused and perplexed comments about the state of the Python environment, concluding with a comic punchline at the bottom that reads, "My Python environment has become so degraded that my laptop has been declared a superfund site."
---
Illustration [from xkcd](https://xkcd.com/1987) describing the complexities of installing different versions of Python on your computer. Used under a [CC-BY-NC 2.5 licence](https://creativecommons.org/licenses/by-nc/2.5/deed.en).
```
