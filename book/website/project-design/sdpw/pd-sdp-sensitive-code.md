(pd-sdpw-sensitive-code)=
# Sharing your Jupyter notebook

One neat way of sharing your research workflow - whether that is your data cleaning process, the statistical modelling that you have applied to your data set, or how you have visualised your results  - is through [Jupyter notebooks](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).

Working with sensitive data may, however, create barriers to sharing your Jupyter notebook: you do not want to commit a Jupyter notebook containing sensitive data to GitHub.

You can get around this hurdle by manually clearing your notebook's output before each Git commit you do. 
This process is, however, time-consuming, cumbersome and - most importantly - extremely error-prone. 
You only need to forget to clear the output once to inadvertently expose your data. 
Another, much more efficient (and failsafe!) way of doing this is by using `nbstripout`.

## `nbstripout`

[`nbstripout`](https://pypi.org/project/nbstripout/)is a utility that - when used as a [git filter](https://git-scm.com/docs/gitattributes#_filter) or [pre-commit hook](https://git-scm.com/docs/githooks#_pre_commit) - automatically strips the Jupyter (or IPython/Zeppelin) notebook output before Git even gets the chance to see it.
In other words, it simulates the *Clear All Output* procedure in the Jupyter notebook user interface.

### Installing `nbstripout`

The latest version of `nbstripout` can be installed from [PyPI (The Python Package Index)](https://pypi.org) using the command `pip install --upgrade nbstripout`.
If you are using Anaconda, you can install `nbstripout` via the conda package manager: `conda install -c conda-forge nbstripout`.

### Setting up the git filter and attributes

Once `nbstripout` is installed, you need to add it to your local Git repository.
Start by creating a new repository or navigating to one that you are already using. Once there, add `nbstripout` using the command `nbstripout --install`.

You can check that `nbstripout` has successfully been applied as a filter by running the command `cat .git/config`, or checking git attributes by running the command`cat .git/info/attributes`.

### Removing the git filter and attributes

If you decide that you would like to remove `nbstripout`, simply run `nbstripout --uninstall` whilst in the repository.

### Installing `nbstripout` globally

`nbstripout` is generally installed in one local Git repository at a time, so that you can control when it is applied as a filter.

However, if all of your notebooks deal with sensitive data, it might be a good idea to  install `nbstripout` globally across all of your Git repositories.
This way, no notebooks risk slipping under the radar. 

To install `nbstripout` globally, run the command: `nbstripout --install --global`
