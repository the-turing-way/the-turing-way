(pd-code-styling)=
# Code Styling

Have you ever opened a code file two years after running an analysis only to find that you have no immediate memory of what it does?
Have you received analysis files from a collaborator with meaningless file names like `analysis_1final_FINAL.R`, or variables named `x1`, `x2`, `temp`?

Consistent code styling makes your research code easier to read, maintain, and share with collaborators.
Well-formatted code reduces errors and makes it easier for others (including your future self) to understand your work.
This is an important aspect of information management in collaborative research projects.

For comprehensive guidance on code styling, including:
- Why coding style matters for code quality and reproducibility
- File and variable naming conventions
- Writing readable code (comments, indentation, line length)
- Style guides for various programming languages (PEP8, Google Style Guide, and others)
- Automatic formatting and linting tools (Black, autopep8, lintr, and more)
- Static code analysis tools
- Online code quality services

See the {ref}`Code Quality<rr-code-quality>` chapter in the Reproducible Research guide.

<!-- (pd-code-styling)=
# Code Styling and Linting

Have you ever opened a syntax or script file two years after running an analysis only to find that you have no immediate memory of the code?
Have you received analysis files from a collaborator, or downloaded them from an online repository that you have never used before?
Now imagine that these files are very hard to read, or there are lots of variables being passed to arcane functions, or worse, you can't find useful code as they are saved with meaningless file names such as `analysis_1final_FINAL.R`, or `onlyusethisoneforanalysis_onamonday2a.py`.

If you have not - then you are one of the lucky ones!
But if you have experienced it then you might know how frustrating it is to work with those files.

This chapter will highlight ways to avoid such challenges in your projects by introducing some principals of 'code hygiene', otherwise known as *linting*.

```{figure} ../../../figures/linting-no.jpeg
---
height: 500px
name: linting-no
alt: A lint roller cleaning up code, symbolizing the transformation of messy, disorganised information into a clean and readable format.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.13882307](https://doi.org/10.5281/zenodo.13882307).
```

## Overview

Linting includes {ref}`guidelines for styling<pd-code-styling-guidelines>` such as for naming, and ensuring that {ref}`code is human readable<pd-code-styling-readability>` such as by using useful formatting, and writing comments.  
Some integrated development environments (IDEs) include automatic linting, but there are free {ref}`packages and tools for linting<pd-code-styling-tools>` that will lint code for you (for example, [autopep8](https://pypi.org/project/autopep8/)).

By keeping the following advice in mind while coding, your code will be more reusable, adaptable, and clear.

```{figure} ../../../figures/zen-of-python.png
---
height: 500px
name: zen-of-python
alt: The Zen of Python, by Tim Peters. Listing all aphorisms for coding design in Python.
---
*Point 7 of the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) is "Readability Counts". (This can be printed with the python command `>>> import this`)*
``` -->
