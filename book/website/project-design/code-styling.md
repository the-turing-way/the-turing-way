(pd-code-styling)=
# Code Styling and Linting

Have you ever opened a syntax or script file two years after running an analysis only to find that you have no immediate memory of the code?
Have you received analysis files from a collaborator, or downloaded them from an online repository that you have never used before?
Now imagine that these files are very hard to read, or there are lots of variables being passed to arcane functions, or worse, you can't find useful code as they are saved with meaningless file names such as `analysis_1final_FINAL.R`, or `onlyusethisoneforanalysis_onamonday2a.py`.

If you have not - then you are one of the lucky ones!
But if you have experienced it then you might know how frustrating it is to work with those files.

This chapter will highlight ways to avoid such challenges in your projects by introducing some principals of 'code hygiene', otherwise known as *linting*.

```{figure} ../figures/linting-no.*
---
height: 500px
name: linting-no
alt: A lint roller cleaning up code, symbolizing the transformation of messy, disorganised information into a clean and readable format.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

## Overview

Linting includes {ref}`guidelines for styling<pd-code-styling-guidelines>` such as for naming, and ensuring that {ref}`code is human readable<pd-code-styling-readability>` such as by using useful formatting, and writing comments.  
Some integrated development environments (IDEs) include automatic linting, but there are free {ref}`packages and tools for linting<pd-code-styling-tools>` that will lint code for you (for example, [autopep8](https://pypi.org/project/autopep8/)).

By keeping the following advice in mind while coding, your code will be more reusable, adaptable, and clear.

```{figure} ../figures/zen-of-python.*
---
height: 500px
name: zen-of-python
alt: The Zen of Python, by Tim Peters. Listing all aphorisms for coding design in Python.
---
*Point 7 of the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) is "Readability Counts". (This can be printed with the python command `>>> import this`)*
```
