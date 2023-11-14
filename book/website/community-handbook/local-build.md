(ch-local-build)=
# Build the Turing Way Book Locally

## But why build locally?
It's always handy to be able to preview any changes you have been working on as you go - you can be confident that changes you have made are accurate and as intended. 
A nice way to do this is to use the underlying [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) tool to build the book locally.

This is useful because it allows you to preview any changes you have made on your local machine *before* you push your changes to a remote branch. 
You can then decide if you are happy with the result and push your changes to the remote branch thus helping to keep Pull Request conversations and commit histories a bit cleaner.

## Step-by-step guide

We will be using the command line throughout this guide.
You will need to locate your "terminal" or "prompt" application on your machine.

1. Install miniconda by following the instructions for your Operating System (Windows, MacOS, Linux) at this link: https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation
2. Open your terminal app and run the `conda init` command in your terminal. You should see `(base)` in your prompt indicating that conda was successfully installed and you are now in its base environment.
    - Note that if you are using Windows, you will need to open a program called `Anaconda prompt` instead of using `cmd`. 
3. Create a new environment and install a modern version of Python into it:
   ```
   conda create --name the-turing-way python=3.10
   ```
4. Activate the environment with `conda activate the-turing-way`. Any commands we run with Python or pip from now on will use the versions of Python and pip installed into _this_ conda env, not any others
5. Clone _The Turing Way_ repository from GitHub to your machine using the command `git clone https://github.com/the-turing-way/the-turing-way`
6. Navigate into the cloned repository folder using the command `cd the-turing-way`, where the `cd` command means `change directory`
7. Then change into the sub-directory the website is built from using `cd book/website`
8. The Turing Way book is built using multiple python libraries. We can install these dependencies _into your conda environment_ using the following command
   ```
   pip install -r requirements.txt
   ```
   where the `requirements.txt` file contains a list of python libraries
9. And now build the book:
   ```
   jupyter-book build .
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
   ```
   git checkout mybranch
   jupyter-book build .
   ```
Follow the link as before and you will see changes specific to that branch rendered.

## Why did we recommend using (mini)conda?
In the step-by-step guide above, we made use of the `jupyter-book` command to build the Turing Way book. For this command to work as intended you will need a Python installation on your machine. 
As with any other programming language such as R or Julia, any given Python installation might look different from another due to the different packages or libraries that come with the installation.
Over time you will likely install even more packages, or update packages to newer versions. Some packages also depend on the presence of specific versions of other packages to function, and so to ensure your local build works smoothly you will want to minimize as much mismatched dependencies as possible.

But this can be difficult! Even with an organized, concerted effort, package management for programming languages naturally throws up dependency issues. Python packages, for reasons not discussed here, tend to suffer from dependency issues a bit more than other languages (note that all languages do!) and one guaranteed way to come across such an issue by trying to maintain all of your Python projects using just one, large set of packages, each at a specific version. You simply can't cater to the needs of all package dependencies this way. https://xkcd.com/1987/   
![](https://imgs.xkcd.com/comics/python_environment.png)

The most relevant feature for us here is *virtual environments*. 

conda is a package manager designed to easily create language agnostic virtual environments, where each environment contains their own separate set of packages that don't interfere with each other. 
In fact it is best practice to create a virtual environment for each project you work on.
We *could* just use Python's built in virtualenv tool to do this, but it doesn't extend into a multi-language env like conda offers.

By creating a separate environment on your local machine just for _The Turing Way_, this is a great way to minimize those dependency issues. 
conda also has community run channels that dedicate their time to providing you with a certain pool of packages that may be relevant to a specific project, for example the [Bioconda channel](https://github.com/bioconda/bioconda-recipes) that contains packages relevant for bioinformatics projects, and packages not necessarily found on the default channel. Other example channels are:
- r
- conda-forge
- tensorflow-macos

These carefully curated channels also help to ensure your virtual environments contain the most appropriate packages for each of your projects. 
