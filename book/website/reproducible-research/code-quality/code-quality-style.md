
(rr-code-style)=
# Code Style and Formatting

A coding style is a set of conventions on how to format code.
For instance, what do you call your variables? Do you use spaces or tabs for indentation? Where do you put comments?
Consistently using the same style throughout your code makes it easier to read.
Code that is easy to read is easier to understand by you as well as by potential collaborators.
Therefore, adhering to a coding style reduces the risk of mistakes and makes it easier to work together on software.
[Why Coding Style Matters](http://coding.smashingmagazine.com/2012/10/25/why-coding-style-matters/) is a nice article on why coding styles matter and how they increase software quality.

```{figure} ../../../figures/linting-no.jpeg
---
height: 500px
name: linting-no
alt: A lint roller cleaning up code, symbolizing the transformation of messy, disorganised information into a clean and readable format.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.13882307](https://doi.org/10.5281/zenodo.13882307).
```

## Style Guides

Style guidelines differ between organisations, languages, and over time. 
Even the Python style guide Python Enhancement Proposal 8 (PEP 8) has had numerous revisions since it was released in 2001.
You must choose a framework that is best for your purposes: be they for your benefit or the benefit of others.
It is also important to remain consistent (and not consistently inconsistent)!

For example, [PEP8](https://www.python.org/dev/peps/pep-0008/) is the most widely used Python coding style and [ECMAScript 6](http://es6-features.org/) aka [ES6](http://es6-features.org/) is the scripting-language specification standardized by ECMA International for programming in Javascript.

For commonly used style guides for various programming languages see the [Language Guides](https://guide.esciencecenter.nl/#/best_practices/language_guides/languages_overview).
Google also has a [style guide](https://code.google.com/p/google-styleguide/) for many languages that are used in open source projects originating out of Google.

Here are links to existing style guides for various languages:

* [PEP8](https://www.python.org/dev/peps/pep-0008/) for Python.
* [Hadley Wickham's](http://adv-r.had.co.nz/Style.html) style guide for R.
* [Google's](https://google.github.io/styleguide/Rguide.xml) style guide for R.
* [Microsoft's](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions) style guide for C#.
* [PEP7](https://www.python.org/dev/peps/pep-0007/) for C.
* [Harvard Strategic Data Project](https://hwpi.harvard.edu/files/sdp/files/sdp-toolkit-coding-style-guide.pdf) coding style guide for Stata.
* [The Style Guide chapter](https://datamgmtinedresearch.com/style) in Data Management 
in Large-Scale Education Research provides examples for file naming, variable naming, and general code styling.

```{figure} ../../../figures/zen-of-python.png
---
height: 500px
name: zen-of-python
alt: The Zen of Python, by Tim Peters. Listing all aphorisms for coding design in Python.
---
*Point 7 of the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) is "Readability Counts". (This can be printed with the python command `>>> import this`)*
```