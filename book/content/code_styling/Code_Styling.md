# Writing Clear and (Human) Readable Code

## Introduction

Have you ever opened a syntax or script file two years after running an analysis to not only find that  you have no memory of the code, but you've forgotten the language too?
On top of this you may have a load of comments, such as "# Add support later", or "#WHAT WAS I THINKING???", and variables of "df_1_new", "new_dat_4_r".  If you have a larger project, perhaps your filenames include "dat_analsis_1_FINAL_.R" and "data_analysis_2_FINAL_2.R"?

This is frustrating enough when it is just you reading back on it, but imagine cloning these files from github, or the Open Science Framework.
Not only would you have no memory of what was meant, but you would have never known in the first place!

This chapter aims to introduce some principals of code hygine, otherwise known as *linting*, including style, naming conventions, and creating useful comments.  Some integrated development environments (IDE) include automatic linting, and there are also packages in Python that will lint for you (e.g. [autopep8](https://pypi.org/project/autopep8/).
Keeping this advice in mind will help you create reusable, and easily adaptable code.
Indeed, point 7 of the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) is:
>Readability Counts

## Code Styling

Style guidelines differ between organisations, languages, and over time ^[The Python style guide (Python Enhancement Proposal 8) has had numerous revisions since it was released in 2001.].
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
The R style guide suggests keeping file names basic.  This might be fine for small compact projects, however over larger projects with lots of similar files, or if you are not using version control (see chapter /?) it may be more appropriate to use the COS guidelines.

## Variable Naming
Unlike in school maths projects where variables are usually unimaginatively called "x","y", and "z". This brevity is probably because teachers rightfully do not want to repeatedly write long variable names on the board.  In coding however, you have the freedom to name your variables anything you like. This can be useful for representing the flow of your script.

Be creative!

### Naming conventions
For clarity and readabiliy, choosing a set of naming conventions for your variables is useful.  There are a large number available, including:
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

If you like you can clear out the old variable using remove as above.

## Line Length
There is some agreement on the length of coding lines.
PEP8 suggests a maximum of 79 characters per line, and 80 by the R style guide.
This means that the lines can easily fit on a screen, and multiple coding windows can be opened.  It is argued that if your line is any longer than this then you should use separate stages.  This is the crux of the Tidy method of R programming, which even has a special operator `%>%` which passes the previous object to the next function, so fewer characters are required:

```
recoded_melt_dat <- read_csv('~/files/2019-05-17_dat.csv') %>%
recode() %>%
melt() #We now have a recoded, melted dataframe called recoded_metl_dat
```

## Commenting
Comments can be blocked or inline.  The PEP8 guidelines have firm suggestions that block comments should be full sentences, have two spaces following a period, and follow a dated style guide(Strunk and White)^[Fortunately the Elements of Style no longer 'requires' an unfair emphasis on masculine pronouns.], whereas inline comments should be used sparingly.
Comments have been described as "Love letters to your future self"^[Jon Peirce, creator of PsychoPy].
Keeping clear and concise comments not only allows you to keep track of the decisions you have made, what particular functions do, and what variables are used, it also allows other people to see your thought processes.
The syntax for comments varies with programming languages.
In R and Python, a hashtag is used, whereas in C the brackets `/* /*` are used, and in C++/C# a double slash `//` comments single lines.

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

```{r}

"1 - This is a string, it will not be evaluated by R, and will not raise
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



Obviously, these are just guidelines, and you should choose elements that suit your own coding style. However, it is important to ensure that you are consistent when collaborating, and agree on a common style.
It could be useful to create a readme file describing your approach to coding style so other users can see your decisions.
Code formatting

When making code open, it is important to ensure that it is legible and easy to follow.

Much like writing prose, there are a number of methods available to help make your code clear.
These include use of whitespace, naming, commenting.

Correct naming has a two-fold benefit.
The first is that it allows you to communicate the purpose of a variable or object without additional commenting.
For example participant_data is more informative than df.
It can also let you see the flow of your code or script.
For instance the variable:

```
participant_data_no_outliers <- filter.outliers(participant_data)
```
tells the reader something about the transformation that the function has performed on the data.


The style that you use is down to preference, however it is important to stick to it, and to ensure that your collaborators are using the same style.
Style includes: variable naming; use of whitespace; 

```
ThisIs Because_SwitchingbetweenDifferentformats is.difficult to read.
```

```
Where_as if_you stick_to one_style, your_code will_be easier_to_follow!
```

## Variable Naming
There are a variety of naming styles that you can follow (not all will work with all languages).
The major ones include:
CamelCase

Commenting
Jon Peirce - "Comments are love-letters to your future self".

Linting?

Linting is error checking on the fly - it will check your syntax as you code and will show you where certain errors are, such as mismatched brackets, missing commas etc.

Linting is often indicated using underlining of potential problems (much like a spell checker).
Until all of the underlining has disappeared, the code will not run.
The degree of linting will depend on the Integrated Development Environment that you are using (IDE). 

Whitespace
The functional importance of whitespace depends on the programming language you use, however the importance for accessibility does not.  In langugages like Python, whitespace is used for nesting i.e. loops and if statements are bracketted by white space:

In R

```{r}
if(x==y){print("Hello world")}
```
However, adding whitespace to the R version makes the function easier to read:

```{r}
x = 1
y = 1

if(x == y){

print("Hello world")

}
```

In Python, there are no brackets, so you need to be aware of how much whitespace is used.

```{python}
if x == y:
	print "hello world"
```

Adding whitespace to your

Naming conventions
