(rr-code-reuse-packages)=
# Overview of writing packages

This section provides an overview of why software packages and libraries are useful for code reproducibility and why you might want to write your own packages. 
Packages are written to a high standard of reproducible code (see the guidelines for [publishing an R package on CRAN](https://cran.r-project.org/web/packages/policies.html)).
The {ref}`rr-code-reuse-details` and {ref}`rr-code-reuse-recommendations` sections of the Turing Way also provide useful guidelines that are applicable to writing software packages.

# What are packages?
A package -- sometimes called a library or a module -- is a basic unit of reproducible, and often efficient, code that aims to create or extend the functionality of a programming language.
Some packages, such as Python's `numpy` package, are so famous that they even [get published in scientific journals such as Nature](https://www.nature.com/articles/s41586-020-2649-2)!
Besides user-defined functions, every function that you call in any programming language is defined within a package, and anyone can write a package that can be shared and used within a standard install of a given programming language. 
In fact, all programming languages are simply comprised of many packages that provide certain functionality, even down to the simple `print` function that you can find in almost every programming language:

```python
# This Python program prints “Hello, world!”
print('Hello, world!')
```

When you install Python, the `print` function is already included as part of a package called `bltinmodule.c`: 2,843 lines of code written to define some core functionalities of the Python language... written in the C programming language! 
You can see the source code for yourself at the [Python Github Repository](https://github.com/python/cpython/blob/3.8/Python/bltinmodule.c#L1821). 
You might be asking "why is a Python library written in C?"
The answer is that compiled C code runs extremely fast compared to higher-level code such as Python code; this gives you another insight into good practices employed when writing code to be shared (via a package) with other users - try and optimize your code so that it runs efficiently. 
Many other languages will also write packages that aren't written using the language itself, instead written in languages such as C or Fortran. 

# Where / how can I get packages?
Programming languages can offer a central resource to download and install packages, such as [CRAN](https://cran.r-project.org/), [PyPi](https://pypi.org/) and [npm](https://www.npmjs.com/). 
The following table shows a list of popular languages and how many packages they contain (taken from https://github.com/breck7/pldb).

```{table} Central package resources
:name: central-resources
| Language          | Website                                             | Packages | Appeared |
| ------------ | ----------------------------------------------------- | -------- | -------- |
| javascript   | http://npmjs.org                                      | 901,025  | 1995     |
| java         | https://search.maven.org/                             | 266,776  | 1995     |
| php          | https://packagist.org/                                | 211,636  | 1995     |
| perl         | https://www.cpan.org/                                 | 176,876  | 1987     |
| python       | https://pypi.python.org/pypi                          | 167,097  | 1991     |
| csharp       | https://www.nuget.org/                                | 141,524  | 2000     |
| swift        | https://cocoapods.org/                                | 57,000   | 2014     |
| clojure      | https://clojars.org/                                  | 23,459   | 2007     |
| rust         | https://crates.io/                                    | 22,486   | 2010     |
| r            | https://cran.r-project.org/                           | 13,674   | 1993     |
| haskell      | https://hackage.haskell.org/                          | 13,487   | 1990     |
| ruby         | https://rubygems.org/                                 | 9,889    | 1995     |
| matlab       | https://www.mathworks.com/matlabcentral/fileexchange/ | 9,718    | 1984     |
| erlang       | https://hex.pm/                                       | 8,069    | 1986     |
| tex          | https://ctan.org/                                     | 5,649    | 1978     |
| stata        | https://www.stata.com/manuals/rssc.pdf                | 4,608    | 1985     |
| smalltalk    | http://smalltalkhub.com/                              | 4,534    | 1972     |
| powershell   | https://www.powershellgallery.com/                    | 4,382    | 2006     |
| emacs-editor | https://melpa.org/                                    | 4,079    | 1976     |
| dart         | https://pub.dartlang.org/                             | 2,751    | 2011     |
```
In addition to central package resources, many packages are often developed and accessible from repositories such as GitHub; you can however get a package from anywhere that you can download a zip or tar file with an internet connection.
Given the nature of reproducible code, of which a package is a fundamental unit, you will likely find that most packages that exist in a central resource also have their code published in a git repository.

# Why write software packages?
If you have written a set of functions that work together and are used to achieve something specific, writing a package is a great way of making it available for others to use. 
Some examples might include:

- A methodology described in a research paper that comes with code to implement it
- A new package that extends functionality when working with other packages such as those that are part of R’s tidyverse
- An extension to an existing software package
- A package created just for fun!

As fundamental units of reproducibile code, packages can be useful to share publicly even if they’re packages that you use just for yourself. 
One such package that started out as a personal library is [HMisc](https://cran.r-project.org/web/packages/Hmisc/index.html) (Harrell Miscellaneous): a statistics package with a collection of useful functions maintained by Professor Frank Harrell that is now widely used amongst R users. 

## What standards should be adhered to when writing a package?
If you plan on writing a package for others to use, there are numerous considerations to make. 
You will want to ensure your code will work reliably, and do so on systems other than your own.
Some recommendations would be:

- {ref}`Unit Testing <rr-testing-unittest>` and {ref}`Intergration Testing <rr-testing-types-integrationtest>` to ensure code within the package is robust and provides useful feedback to the end user while using it (warnings, errors).
- {ref}`Version Control <rr-vcs>` of the codebase to track development and fix bugs.
- {ref}`Documentation <rr-rdm-metadata>`. This might be in the form of a website or a wiki. There are even language specific packages that aim to provide project templates that will render the template into a website or other form of documentation (see [packagedown](https://pkgdown.r-lib.org/) for R, [Sphinx](https://www.sphinx-doc.org/) for Python or [Doxygen](https://www.doxygen.nl/) for C++).
- Host your versioned codebase somewhere accessible. There are a whole range of places to host code depending on your use case. Public GitHub/GitLab repositories are extremely common especially in open source, whereas private repositories can be used for proprietary packages (think Matlab). Even just a local git repository might be enough for your use-case. 
- Use Continuous Integration /  Continuous Development principles and pipelines such as GitHub Actions, Jenkins, Travis or GitLab Runners to help with a range of testing procedures.
 - Consider submitting your package to a central resource such as those listed above ([](central-resources)). There are usually strict requirements needed as your code is more likely to be distributed and used (more on this later on). Often GitHub repositories are used to store both stable and "daily"/"nightly" builds of a package in addition to a central resource so that users can submit bugs an contribute to the current version, while testing experimental versions as a preview. 
 - Write a publication. This could be in the form of a journal submission such as Numpy (in Nature!), or an abstract/paper in a conference proceeding. This allows your package to be peer-reviewed by experts in the field of intended use and might give more confidence to potential users that the package is robust.
 - Publicize your package. If you have gotten as far as hosting and publishing your package for others to use, you can publicize it in a variety of ways to let people know about it. It used to be that getting your package into a central resource provided ample opportunity for your package to be shared, but as these resources grow this is not necessarily the case anymore. Aside from publications in journals, use social media such as Twitter, Discord and Slack, as well as Medium articles and blog posts. 
 - Build a community. Hopefully a few collaborators will have worked together to build a package, and by thinking about how the initial developers of the packages interact with future users you might be able to build a strong community that will help improve and maintain the package going forward.

## Get Started - use a template
With so many existing packages across many languages, it should be pretty easy to find good examples of packages and their published code on software repositories such as GitHub.
Looking at the codebase can give you an idea of how to structure your own packages, but they can be a little daunting especially if they are well-established, widely used packages. 

As mentioned previously, there are packages that are specifically meant to help you create your own packages.
These work by creating the underlying structure of a package or even simulated toy repositories that you can then customize as you see fit.
Such templates will often factor in locations for documentation, code commenting conventions and built-in code linting, and sub-directories for header files like you might find in the C programming language. 

## Walkthrough of creating a package in R
Let's walk through creating a basic package in R using with some help from some specialized packages, particularly `usethis` and `roxygen2`.
Begin by loading some go-to libraries that help package development in R

```r
library(devtools)   # various developer tools
library(usethis)    # create templates for repetitve tasks
library(roxygen2)   # automatically render documentation files from commented code
library(assertthat) # unit testing within functions
```
Create a skeleton directory template commonly used for R packages - will include a Description file, sub-directory for R function files, a NAMESPACE file for global package information and an .Rproj file to easily share and load local project directories.

```r
usethis::create_package("/RDemoPackage")
```

```
├── DESCRIPTION
├── NAMESPACE
├── R
└── RDemoPackage.Rproj
```

Create a `.R` file in the R/ subdirectory and write a function to convert from degrees Celsius to Kelvin.
Notice that we have some code comments in the preamble that will get used to render a markdown file for the documentation (we use `roxygen2` for this).

```bash

# create a function to convert degrees C to Kelvin

#' Converts degrees C to Kelvin
#'
#' Allows the user to input temperature in degrees C and return the corresponding value in degrees Kelvin
#'
#' @param print_statement a logical value indicating
#' whether to print the statement (default is \code{TRUE})
#'
#' @import dplyr
#'
#' @export
#'
#' @return \code{my_function} prints a declaration
#' announcing itself if the parameter is \code{TRUE}
#'
#' @examples
#' celsius_to_kelvin(12)
#'

celsius_to_kelvin <- function(temp_C) {
  # assert value in degrees C greater than a certain amount
  assert_that(temp_C > -89.2,
              msg = "The temperature in degrees C entered is lower
              than the lowest recorded ground temperature on earth at
              −89.2 °C (−128.6 °F; 184.0 K) at the then-Soviet Vostok Station
              in Antarctica on 21 July 1983. It is likely you have entered an incorrect temperature.")
  # make the calculation
  temp_K <- temp_C + 273.15
  return(temp_K)
}
```

We also used the `assert_that()` function from the `assertthat` package that allows us to unit test within functions in R. In this case we don't allow the user to input a temperature of below -89.2 degrees C. We then use the document() function from the `roxygen2` package to automatically render documentation in the form of a markdown file based on the comments at the top of the function file.

```r
document()
```

We can then install and load our new package in our local environment

```r
install()
library(TempConvert)
```


Finally - if we push our code up to GitHub, anyone can install it using the following:


```r
install_github("pinkpanther/TempConvert")
library(TempConvert)
```


