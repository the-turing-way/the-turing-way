(pd-code-styling-readability)=
# Writing Human Readable Code

Writing clear, well commented, readable and re-usable code benefits not only you but the community (or audience) that you are developing it for.
This may be your lab, external collaborators, stakeholders, or you might be writing open source software for global distribution!
Whatever scale you work at, readability counts!

Here are a few aspects to consider when making your code easy to read by others.

## Line Length

There is some agreement on the length of the coding lines.
PEP8 suggests a maximum of 79 characters per line and 80 by the R style guide.
This means that the lines can easily fit on a screen, and multiple coding windows can be opened.
It is argued that if your line is any longer than this then your function is too complex and should be separated!
This is the crux of the Tidy method of R programming, which even has a special operator `%>%` which passes the previous object to the next function, so fewer characters are required:

```r
recoded_melt_dat <- read_csv('~/files/2019-05-17_dat.csv') %>%
recode() %>%
melt() #We now have a recoded, melted dataframe called recoded_melt_dat
```

## Commenting

Comments have been described as "Love letters to your future self" by Jon Peirce, creator of PsychoPy.
Comments can be blocked or inline.  
The PEP8 guidelines have firm suggestions that block comments should be full sentences, have two spaces following a period, and follow a dated style guide (Strunk and White). 
Fortunately the Elements of Style no longer 'requires' an unfair emphasis on masculine pronouns.
Whereas inline comments should be used sparingly.
Keeping clear and concise comments not only allows you to keep track of the decisions you have made, what particular functions do, and what variables are used, it also allows other people to see your thought processes.
The syntax for comments varies with programming languages.
In R and Python, a hashtag is used, whereas in C and Java the brackets `/* /*` are used, and in C++/C# a double slash `//` comments single lines.

In Python:
```python
times = 10 # Set integer
my_variable = "my variable is %s times better than yours" %times #Set my_variable to a string
print(my_variable) #print the value
```

In R:
```r
my_func = function(number){ #R function

(number * 5) - 2
}
print(my_func(2))
```

For longer comments, information can be included above the code block.
In Python, you can use triple speech marks as a parenthesis.
This will comment out anything in between.

```python
"""
The following function takes a number, multiplies it by 5, and subtracts 2.
This may seem pointless but is simple for demonstration.
"""
def myfunc(numb): #python function
      return((numb*5)-2)
print(myfunc(8))
```
Longer blocks of comments are not available in R.
There are ways around this, such as setting up a string, or an if(false) statement:

```r
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

```r
#This is also a very long comment
#covering many lines.
```
Your IDE will probably have a keyboard shortcut for commenting out blocks.

## Indentation

The R style guide suggests that lines should be separated:
```r
by
  two spaces
```
And not
```r
 a mixture
   of
   	tabs
   	  and 	spaces.
```

Obviously, sometimes the arguments of a function can far expand 80 characters.
In this case, it is recommended that the second line be indented to the start of the arguments:

```r
my_variable <- a_really_long_function(data = "2019-05-17_Long_File_Name_2",
                                      header = TRUE, verbose = TRUE)

```

These are of course just guidelines, and you should choose elements that suit your coding style.
However, and again, it is important to ensure that you are consistent when collaborating, and can agree on a common style.
It could be useful to create a readme file describing your coding style so collaborators or contributors can follow your lead.

### ...end. ...end.  ...or end.\\n

If you are sharing text files or working collaboratively on manuals or documents, then there is a lot of controversy surrounding whether to use one or two spaces after a period.
When using Markdown, it can be clearer to include a new line after every sentence.
This chapter (and most, if not all, of this book) has a new line after every sentence that makes the raw text easier to read, review and solve the spacing issue.

```{figure} ../../figures/xkcd1285.*
---
height: 500px
name: xkcd1285
alt: Two groups holding different flags and fighting, one says "two spaces after a period" and other says "one space after a period". While a person stands with their flag that says "Line break after every sentence"
---
*Line break after each sentence makes it easy to review and comment - [XKCD Link](https://www.explainxkcd.com/wiki/index.php/1285:_Third_Way)*
```
