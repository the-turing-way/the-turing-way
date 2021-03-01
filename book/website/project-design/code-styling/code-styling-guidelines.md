(pd-code-styling-guidelines)=
# Guidelines for Code Styling

Style guidelines differ between organisations, languages, and over time. 
Even, the Python style guide Python Enhancement Proposal 8 (PEP 8) has had numerous revisions since it was released in 2001.
You must choose a framework that is best for your purposes: be they for your benefit or the benefit of others.
It is also important to remain consistent (and not consistently inconsistent)!

Style guidelines include advice for file naming, variable naming, use of comments, and whitespace and bracketing.

The following are links to existing style guides that may be of use when deciding how to format your code:

* [PEP8](https://www.python.org/dev/peps/pep-0008/) for Python.
* [Hadley Wickham's](http://adv-r.had.co.nz/Style.html) style guide for R.
* [Google's](https://google.github.io/styleguide/Rguide.xml) style guide for R.
* [Microsoft's](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions) style guide for C#.
* [PEP7](https://www.python.org/dev/peps/pep-0007/) for C.

However, to get started quickly, the following sections present some advice for code style.

## File Naming

The [Centre for Open Science](http://help.osf.io/m/bestpractices/l/609932-file-naming) has some useful suggestions for the naming of files, particularly ensuring that they are readable for both humans and machines.
This includes avoiding the use of wildcard characters (@£$%) and using underscores ("\_") to delimit information, and dashes ("\-") to conjunct information or spaces.
They also suggest dating or numbering files and avoiding words like FINAL (or FINAL-FINAL).
The dating suggestion is the long format `YYYY-MM-DD`, followed by the name of the file, and the version number.
This results in automatic, chronological order. For example:

```r
data <- read.csv("2019-05-17_Turing-Way_Book-Dash.csv")

```
The R style guide suggests keeping file names basic.
This might be appropriate for small compact projects, however over larger projects with lots of similar files, or if you are not using version control (see chapter /?) it may be more appropriate to use the COS guidelines.
For more details please see the chapter on {ref}`File Naming<pd-filenaming>`.

### Versioning

An extra consideration to file-naming is versioning your software.
Using versioning guidelines will help avoid using words like `_FINAL.R`.
A typical convention is the MajorMinorPatch (or MajorMinorRevision) approach.
In this, your first attempt at a package or library might look like this:
```
my-package_1_0_0.py
```
This indicates that the software is in the unrevised/patched alpha stage (0) of the first major release.

## Variable Naming

In maths projects at school,  variables are often unimaginatively named "x", "y", and "z".
This brevity is probably because teachers (understandably) do not want to repeatedly write long variable names on the board.
In coding, however, you have the freedom to name your variables anything you like.
This can be useful for representing the flow of your script.

Be creative!

### Naming conventions

For clarity and readability, choosing a set of naming conventions for your variables is useful.
There is a large variety, and some people can be quite vocal about which one is 'correct' (pick one that is right for you!).
These include:

- CamelCase
- lowerCamelCase
- Underscore_Methods
- Mixed_Case_With_Underscores
- lowercase

For example:

```r
raw_data <- read.csv("data.csv") # Not very creative
rawData <- read.csv("data.csv")  #lowerCamelCase
```

OK, `raw_data` is not very creative, but it could easily have been `spam` or `eggs` if that makes sense in your script.
You may also have a function that recodes a variable:

```r
rawDat <- recode(rawDat)
```

Reusing the variable name provides no information about the process that rawDat has been through.
Storing it as a separate variable lets us see what transformations have been carried out on the original variable:

```
rawDat_recoded <- recode(rawDat)
```

If you like you can clear out the old variable using remove as above.  

```
remove(rawDat) #In R
del(rawDat) # In Python
```

It is important to choose one style and stick to it:

```
ThisIs Because_SwitchingbetweenDifferentformats is.difficult to read.
```

```
Where_as if_you stick_to one_style, your_code will_be easier_to_follow!
```
