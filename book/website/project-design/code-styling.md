(pd-code-styling)=
# Code Styling and Linting

Have you ever opened a syntax or script file two years after running an analysis only to find that you have no immediate memory of the code?
Have you received analysis files from a collaborators, or downloaded them from online repository that you have never used before?
Now imagine that these files are very hard to read, or there are lots of variables being passed to arcane functions, or worse, you can't find useful code as they are saved with meaningless file names such as `analysis_1final_FINAL.R`, or `onlyusethisoneforanalysis_onamonday2a.py`.

If you have not - then you are one of those who have already learned from your previous experience!
For everyone else, this chapter will highlight ways to avoid frustration of dealing with such challenges in personal projects.

Indeed, point 7 of the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) is "Readability Counts".

```{figure} ../figures/zen-of-python.png
---
height: 500px
name: zen-of-python
alt: The Zen of Python, by Tim Peters. Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!
---
*"Long time Pythoneer Tim Peters succinctly channels the BDFL's guiding principles for Python's design into 20 aphorisms, only 19 of which have been written down." (This can be printed with the python command `>>> import this`)*
```

## Overview

This chapter aims to introduce some principals of 'code hygiene', otherwise known as *linting*.
Linting includes guidelines for code formatting and naming conventions, and ensuring that code is human readable such as by using useful formatting, writing comments and creating documentation.  
Some integrated development environments (IDEs) include automatic linting, but there are free packages in Python that will lint code for you (for example, [autopep8](https://pypi.org/project/autopep8/).

By keeping the following advice in mind while coding, your code will be more reusable, adaptable, and clear.
