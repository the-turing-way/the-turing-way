(ch-local-build)=
# How to build Jupyter Book locally

## But why build locally?
It's always handy to be able to preview any changes you have been working on as you go - you can be confident that changes you have made are accurate and as intended. 
A nice way to do this is to use the underlying Jupyter Book tool to build the book locally.

This is useful because it allows you to preview any changes you have made on your local machine *before* you push your changes to a remote branch. 
You can then decide if you are happy with the result and push your changes to the remote branch thus helping to keep Pull Request conversations and commit histories a bit cleaner.

## Step-by-step guide
1. Install miniconda https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation
2. Run `conda init` in your terminal. You should see `(base)` in your prompt indicating that conda was successfully installed and you are now in it's base environment.
3. Create a new environment and install a modern version of python into it
   ```
   conda create --name the-turing-way python=3.10
   ```
4. Activate the environment with `conda activate the-turing-way`. Any commands we run with Python or pip from now on will use the versions of Python and pip installed into _this_ conda env, not any others.
5. Clone the repository from GitHub to your machine using the command `git clone https://github.com/alan-turing-institute/the-turing-way`
6. Change into the repo: `cd the-turing-way`
7. Change into the correct folder `cd book/website`
8. Install the dependencies _into your conda environment_
   ```
   pip install -r requirements.txt
   ```
9. And now build the book:
   ```
   jupyter-book build .
   ```
10. The output of the build process will provide output such as below that demonstrate how you can view the book locally:
    ```
    ===============================================================================

    Finished generating HTML for book.
    Your book's HTML pages are here:
        _build/html/
    You can look at your book by opening this file in a browser:
        _build/html/index.html
    Or paste this line directly into your browser bar:
        file:///Users/sgibson/source/github/alan-turing-institute/the-turing-way/book/website/_build/html/index.html

    ===============================================================================
    ```
    
### Build the book while working on a Pull Request
If you would like to preview a version of the book from a certain branch (perhaps to render the book while working on a PR) then simply switch to the required branch and rebuild the book as in step 10:
   ```
   git checkout mybranch
   jupyter-book build .
   ```
Follow the link as before and you will see changes specific to that branch rendered.

## Why did we recommend using miniconda?
- Running the `juypter-book` command to build the Turing Way book relies on having a python installation on your machine. As with any other programming language such as R or Julia, any given python installation might look different from another due to the packages or libraries that come with the installation. 
- In particular, some packages depend on the presence of specific versions of other packages to function, and so to ensure your local build works smoothly you will want to minimize as much mismatched dependencies as possible.
- But this can be difficult! Even with an organized, concerted effort, package management for programming languages naturally throws up dependency issues. Python packages, for reasons not discussed here, tend to suffer from dependency issues a bit more than other languages (note that all languages do!) and one guaranteed way to come across such an issue by trying to maintain all of your python projects using just one, large set of packages, each at a specific version. You simply cant cater to the needs of all package dependencies this way. https://xkcd.com/1987/   
![](https://imgs.xkcd.com/comics/python_environment.png)
- Anaconda is package manager that can install Python, R and Julia distributions. *Miniconda* is just a smaller package manager that by default installs a smaller set of packages which means in terms of dependencies there are less things to go wrong.
- The most relevant feature for us here is *virtual environments*. Both anaconda and miniconda can easily create language agnostic virtual environments where each contains their own separate set of packages that don't interfere with each other. In fact it is best practice to create a virtual environment for each project you work on.
- We *could* just use python's built in virtualenv tool to do this, but it doesn't extend into a multi-language env like anaconda and miniconda offer.
- By creating a separate environment on your local machine just for The Turing Way, this is a great way to minimize those dependency issues. 
- Anaconda and miniconda also have community run channels that dedicate their time to providing you with a certain pool of packages that may be relevant to a specific project, for example the [Bioconda channel](https://github.com/bioconda/bioconda-recipes) that contains packages relevant for bioinformatics projects, and packages not necessarily found on the default channel. Other popular channels are:
    - r
    - conda-forge
    - tensorflow-macos

These carefully curated channels also help to ensure your virtual environments contain the most appropriate packages for each of your projects. 
