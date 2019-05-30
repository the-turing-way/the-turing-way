# Writing Clear and (Human) Readable Code

## Introduction

Have you ever opened a syntax or script file two years after running an analysis to not only find that  you have no memory of the code, but you've forgotten the language too?
On top of this you may have a load of comments, such as "# Add support later", or "#WHAT WAS I THINKING???", and variables of "df_1_new", "new_dat_4_r". 
If you have a larger project, perhaps your filenames include "dat_analsis_1_FINAL_.R" and "data_analysis_2_FINAL_2.R"?

This is frustrating enough on personal projects, but imagine if a collaborator sent you those files, or you had cloned them from github, or the Open Science Framework.

Not only would you have no memory of what was meant, but you would have never known in the first place!

![https://xkcd.com/1513/](xkcd1513.png)

This chapter aims to introduce some principals of code hygine, otherwise known as *linting*.  Linting includes code formatting, naming conventions, and creating useful comments.  
Some integrated development environments (IDE) include automatic linting, and there are also packages in Python that will lint for you (e.g. [autopep8](https://pypi.org/project/autopep8/).

Keeping this advice in mind will help you create reusable, and easily adaptable code.  
Indeed, point 7 of the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) is:
>Readability Counts

## Code Styling

Style guidelines differ between organisations, languages, and over time ^[The Python style guide Python Enhancement Proposal (PEP) 8 has had numerous revisions since it was released in 2001.].
It is important that you work to a framework that is best for your purposes, bearing in mind that consistency makes for easier reading and understanding.

Style guidelines include advice for file naming, variable naming, comments, and the use of whitespace and brackets.
For examples of style guides, follow the following links:

* [PEP8](https://www.python.org/dev/peps/pep-0008/) for Python.
* [Hadley Wickham's](http://adv-r.had.co.nz/Style.html) style guide for R.
* [Google's](https://google.github.io/styleguide/Rguide.xml) style guide for R.
* [Microsoft's](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions) style guide for C#.
* [PEP7](https://www.python.org/dev/peps/pep-0007/) for C.

## File Naming

The [Centre for Open Science](http://help.osf.io/m/bestpractices/l/609932-file-naming) has some useful suggestions for naming of files, particularly ensuring that they readable both to humans and computers.
This includes avoiding the use of wildcard characters (@£$%) and using underscores ("\_") to delimit information, and dashes ("\-") to conjunct information or spaces.
They also suggest dating or numbering files, and avoiding words like FINAL (or FINAL-FINAL).
The dating suggestion is the long format `YYYY-MM-DD`, followed by the name of the file, and the version number.  This results in an automatic, chronological order. For example:

```
data <- read.csv("2019-05-17_Turing-Way_Book-Dash.csv")

```
The R style guide suggests keeping file names basic.  This might be appropriate for small compact projects, however over larger projects with lots of similar files, or if you are not using version control (see chapter /?) it may be more appropriate to use the COS guidelines.

## Variable Naming
Unlike in school maths projects where variables are unimaginatively called "x","y", and "z". This brevity is probably because teachers rightfully do not want to repeatedly write long variable names on the board.  In coding however, you have the freedom to name your variables anything you like. This can be useful for representing the flow of your script.

Be creative!

![https://xkcd.com/1695/](xkcd1695.png)

### Naming conventions
For clarity and readabiliy, choosing a set of naming conventions for your variables is useful.  There are a large number, including:
- CamelCase
- lowerCamelCase
- Underscore_Methods
- Kebab-Case
_ Mixed_Case_With_Underscores
- lowercase

The Kebab case will not work with some languages, such as R and Python since this will be interpreted as a subtraction sign.

```{r}
raw_data <- read.csv("data.csv") # Not very creative
rawData <- read.csv("data.csv")  #lowerCamelCase

```
OK, `raw_data` is not very creative, but it could easily have been `spam` or `eggs` if that makes sense in your script.  You may also have a function that recodes a variable:

```
rawDat <- recode(rawDat)
```
Reusing the variable name provides no information about the process that rawDat has been through.  Storing it as a separate variable lets us see what transformations have been carried out on the original variable:

```
rawDat_recoded <- recode(rawDat)
remove(rawDat)
```

If you like you can clear out the old variable using remove as above.  It is important to choose ones style and stick to it:

```
ThisIs Because_SwitchingbetweenDifferentformats is.difficult to read.
```

```
Where_as if_you stick_to one_style, your_code will_be easier_to_follow!
```

## Line Length
There is some agreement on the length of coding lines.
PEP8 suggests a maximum of 79 characters per line, and 80 by the R style guide.
This means that the lines can easily fit on a screen, and multiple coding windows can be opened.
It is argued that if your line is any longer than this then you should use separate stages.
This is the crux of the Tidy method of R programming, which even has a special operator `%>%` which passes the previous object to the next function, so fewer characters are required:

```
recoded_melt_dat <- read_csv('~/files/2019-05-17_dat.csv') %>%
recode() %>%
melt() #We now have a recoded, melted dataframe called recoded_melt_dat
```

## Commenting
Comments can be blocked or inline.  The PEP8 guidelines have firm suggestions that block comments should be full sentences, have two spaces following a period, and follow a dated style guide(Strunk and White)^[Fortunately the Elements of Style no longer 'requires' an unfair emphasis on masculine pronouns.], whereas inline comments should be used sparingly.
Comments have been described as "Love letters to your future self"^[Jon Peirce, creator of PsychoPy].
Keeping clear and concise comments not only allows you to keep track of the decisions you have made, what particular functions do, and what variables are used, it also allows other people to see your thought processes.
The syntax for comments varies with programming languages.
In R and Python, a hashtag is used, whereas in C and Java the brackets `/* /*` are used, and in C++/C# a double slash `//` comments single lines.

In Python:
```{python}
times = 10 # Set integer
my_variable = "my variable is %s times better than yours" %times #Set my_variable to a string
print(my_variable) #print the value
```

In R:
```{r}
my_func = function(number){ #R function

(number * 5) - 2
}
print(my_func(2))
```
In C:
```{c}
static int
{
int my_int = 57 ; /* C for completion */
}
```
For longer comments, information can be included above the code block. In Python you can use triple speech marks as parenthesis.  This will comment out anything in between.

```{python}
"""
The following function takes a number, multiplies it be 5, and subtracts 2.
This may seem pointless, but is simple for the purpose of demonstration.
"""
def myfunc(numb): #python function
      return((numb*5)-2)
print(myfunc(8))

```

Longer blocks of comments are not available in R.  There are ways around this, such as setting up a string, or an if(false) statement:

```

"1 - This is a string. It will not be evaluated by R, and will not raise
and exception"

if(false){
2 - All of your comment can go here and will never be evaluated.
It also means you keep to the 80 character line length suggestion.
Also, in RStudio you can fold away the comment using the arrow next to the 
line number of the if statement.
}
```

Or commenting out individual lines:

```{r}
#This is also a very long comment
#covering many lines.
```
Your IDE will probably have a keyboard shortcut for commenting out blocks though.

## Indentation
The R style guide suggests that lines should be separated:
```
by
  two spaces
```
And not a mixture of tabs and spaces.
Obviously, sometimes the arguments of a function can far expand 80 characters.
In this case, it is recommended that the second line be indented to the start of the arguments:

```
my_variable <- a_really_long_function(data = "2019-05-17_Long_File_Name_2",
                                      header = TRUE, verbose = TRUE)

```



These are of course just guidelines, and you should choose elements that suit your own coding style.
However, it is important to ensure that you are consistent when collaborating, and can agree on a common style.
It could be useful to create a readme file describing your coding style so collaborators or contributors can follow your lead.

# Tools
As mentioned earlier, there are some automatic tools that you can use to lint your code to existing guidelines.
These range from plugins for IDEs, packages that 'spell check' your style, and scripts that automatically lint for you.

## lintr
lintr is an R package that spell checks your code using a variety of style guidelines.  It can be installed from CRAN.
The function `lint` takes a filename as an argument, and a list of 'linters' that it should check your code against.
These range from whitespace conventions, to checking that curly braces do not have their own lines.

![](lintr_1.png)
![](lintr_2.png)

Lintr provides a list of markers with recommendations for changing the formatting of your code line-by-line, meaning it is besed used early and often in your project.

## Autopep8
Autopep8 is a Python module that can be run from the terminal and automatically formats a file to PEP8 guidelines.  It is available on [pypy](https://pypi.org/project/autopep8/), and can be installed using pip.
![](console.png)
![Before pep8](pre_pep.png)
![After pep8](pep.png)

To some extent, the module can also be used on R scripts!
![](pep8_R.png)
