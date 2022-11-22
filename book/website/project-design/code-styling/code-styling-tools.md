(pd-code-styling-tools)=
# Code Styling Tools

As mentioned earlier, there are some automatic tools that you can use to lint your code to existing guidelines.
These range from plugins for IDEs packages that 'spell-check' your style, and scripts that automatically lint for you.

## lintr

[lintr](https://cran.r-project.org/web/packages/lintr/lintr.pdf) is an R package that spell-checks your code using a variety of style guidelines.  It can be installed from CRAN.
The function `lint` takes a filename as an argument and a list of 'linters' that it should check your code against.
These range from whitespace conventions to checking that curly brackets do not have their lines.
The output provides a list of markers with recommendations for changing the formatting of your code line-by-line, meaning it is best used early and often in your project.

```{figure} ../../figures/lintr-output.*
---
height: 500px
name: lintr_output
alt: lintr output showing recommendations to add space, remove commented code, remove training whitespace, have character size per line less than 80 where needed in the input code.
---
An example of how the lintr output may look like for an input file with R code.
```

For more details, please visit the [GitHub repository](https://github.com/jimhester/lintr).

## Autopep8

[Autopep8](https://pypi.org/project/autopep8/) is a Python module that can be run from the terminal and automatically formats a file to [pycodestyle](https://github.com/PyCQA/pycodestyle) (formerly called pep8) guidelines.  
It is available on [pypy](https://pypi.org) and can be installed using pip.

```
# Install autopep8
$ pip install --upgrade autopep8
```

You can modify a file in place by running the following command:

```
$ autopep8 --in-place --aggressive --aggressive <filename>
```

To some extent, the module can also be used on R scripts!

## Auto formating by Black

[Black](https://black.readthedocs.io/en/stable/) is an auto-formating package for Python.
This means that it will automatically change your code to adhere to certain guidelines, like spaces around operators and removing unnecessary whitespace.
It is also consistent, so that the code that you and your collaborators work on, will look the same once black formats it.
It does not change what the code does.
This can reduce the time spent making the above changes to the code.
