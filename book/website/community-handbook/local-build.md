(ch-local-build)=
# Build the Turing Way Book Locally

## But why build locally?

It's always handy to be able to preview any changes you have been working on as you go - you can be confident that changes you have made are accurate and as intended.
A nice way to do this is to use the underlying [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) tool to build the book locally.

This is useful because it allows you to preview any changes you have made on your local machine before you push your changes to a remote branch.
You can then decide if you are happy with the result and push your changes to the remote branch thus helping to keep Pull Request conversations and commit histories a bit cleaner.

## Step-by-step guide

We will be using the command line throughout this guide.
You will need to locate your "terminal" or "prompt" application on your machine.

<!-- 1. Install miniconda by following the instructions for your Operating System (Windows, MacOS, Linux) at this link: https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation -->

<!-- 2. Open your terminal app and run the `conda init` command in your terminal. You should see `(base)` in your prompt indicating that conda was successfully installed and you are now in its base environment. -->
<!--     - Note that if you are using Windows, you will need to open a program called `Anaconda prompt` instead of using `cmd`. -->

<!-- 3. Create a new environment and install a modern version of Python into it: -->

<!--    ```console -->
<!--    conda create --name the-turing-way python=3.13 -->
<!--    ``` -->

<!-- 4. Activate the environment with: -->

<!--    ```console -->
<!--    conda activate the-turing-way -->
<!--    ``` -->

<!--    Any commands we run with Python or pip from now on will use the versions of Python and pip installed into _this_ conda env, not any others. -->

1. Install Python3 (which version)


5. Clone _The Turing Way_ repository from GitHub to your machine using the command: 

   ```console
   git clone https://github.com/the-turing-way/the-turing-way
   ```

   ````{note}
   To address potential barriers with slow internet connections due to the large size of this repository, you can use [partial clones](https://github.blog/2020-12-21-get-up-to-speed-with-partial-clone-and-shallow-clone/#). Specifically, focusing on blobless clones, which are efficient for developers, involves utilizing the `--filter=blob:none` option in the git clone command.

   By using `--filter=blob:none`, the initial git clone operation downloads all reachable commits and trees, while blobs (file contents) for commits are only downloaded when performing a git checkout

   Here's the command to use blobless clones:

   ```console
   git clone --filter=blob:none https://github.com/the-turing-way/the-turing-way.git
   ```
   ````

6. Navigate into the cloned repository folder using the command `cd the-turing-way`, where the `cd` command means `change directory`.

1. Create a virtual environment

  ```console
  $ python3 -m venv ./venv
  ```

1. Active the virtual environment

  ```console
  $ source ./venv/bin/activate
  ```

  Your prompt may now start with `(venv)` (?).
  Using the virtual environment means we can install _The Turing Way's_ dependencies without interfering with any other software.

7. Then change into the sub-directory the website is built from using `cd book/`

8. The Turing Way book is built using multiple python libraries. We can install these dependencies into your virtual environment using the following command

   ```console
   make deps
   ```
9. And now build the book:

   ```console
   make book
   ```

10. The output of the build process will provide output such as below that demonstrate how you can view the book locally:

    ```text
    ===============================================================================

    Finished generating HTML for book.
    Your book's HTML pages are here:
        _build/html/
    You can look at your book by opening this file in a browser:
        _build/html/index.html
    Or paste this line directly into your browser bar:
        file:///[...]/the-turing-way/the-turing-way/book/website/_build/html/index.html

    ===============================================================================
    ```

### Build the book while working on a Pull Request

If you would like to preview a version of the book from a certain branch (perhaps to render the book while working on a PR) then simply switch to the required branch and rebuild the book as in step 9:

   ```console
   $ git checkout mybranch
   $ make book
   ```

Follow the link as before and you will see changes specific to that branch rendered.

### Clean up a recent build

When you test your edits by building the book multiple times, it is better to clean up the last build before generating a new one.
You can either manually delete the `book/website/_build` folder every time, or run this command:

```console
$ cd book
$ make clean
```

More details on this process can be read in [Jupyter Book's documentation](https://jupyterbook.org/en/stable/basics/build.html?highlight=clean#clean-your-books-generated-files).

### Check external links in the book

When editing or reviewing this book locally, you can run the Sphinx link checker with Jupyter Book to check if the external links mentioned in the book are valid.
To run the link checker, use the following command:

```console
cd book/website
jupyter-book build . --builder linkcheck
```

The link checker checks if the each link resolves and prints the status on your terminal so that you can check and resolve any incorrect links.
Read more about this in [Jupyter Book's documentation](https://jupyterbook.org/en/stable/advanced/html.html?highlight=check%20external#check-external-links-in-your-book).

## Why we recommend using a virtual environment

In the step-by-step guide above, we made use of `jupyter-book` to build the Turing Way book.
For this program to work as intended you will need a Python installation on your machine.

As with any other programming language such as R or Julia, any given Python installation might look different from another due to the different packages or libraries that come with the installation.

Over time you will likely install even more packages, or update packages to newer versions.
Some packages also depend on the presence of specific versions of other packages to function, and so to ensure your local build works smoothly you will want to minimize as much mismatched dependencies as possible.

This can be difficult!
Even with an organized, concerted effort, package management for programming languages naturally throws up dependency issues.
Python packages, for reasons not discussed here, tend to suffer from dependency issues a bit more than other languages (note that all languages do!) and one guaranteed way to come across such an issue by trying to maintain all of your Python projects using just one, large set of packages, each at a specific version.
You simply can't cater to the needs of all package dependencies this way.
Creating an environment on your local machine for _The Turing Way_ is a great way to minimize dependency issues.

```{figure} https://imgs.xkcd.com/comics/python_environment.png
---
height: 487px
name: python-environment
alt: 'A humorous, black and white flowchart from XKCD depicting the complexity of managing different Python environments on a computer. It shows a tangled web of arrows and lines connecting various versions of Python installed through different methods such as Homebrew, Anaconda, and binaries from Python.org. There are also references to different tools and paths like PIP, PYTHONPATH, and system PATH, that add to the confusion. The paths weave in and out of local folders on a computer. Some of them are noted to be owned by root, making them harder to manage. The illustration is annotated with bemused and perplexed comments about the state of the Python environment, concluding with a comic punchline at the bottom that reads, "My Python environment has become so degraded that my laptop has been declared a superfund site."'
---
Illustration [from xkcd](https://xkcd.com/1987) describing the complexities of installing different versions of Python on your computer. Used under a [CC-BY-NC 2.5 licence](https://creativecommons.org/licenses/by-nc/2.5/deed.en).
```
