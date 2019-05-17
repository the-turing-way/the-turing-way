# Writing Clear and (Human) Readable Code
## Introduction
Have you ever opened a syntax or script file two years after running an analysis, only to find that not only have you no memory of the code, but you've forgotten the language too?
On top of this you have a load of comments, such as "# Add this later", or "# WHAT WAS I THINKING???", and variables of "df_1_new", "new_dat_4_r".  If you have a larger project, perhaps your filenames include "dat_analsis_1_FINAL_.R" and "data_analysis_2_FINAL_2.R"?

This is frustrating enough when it is just you reading back on it, but imagine cloning these files from github, or the Open Science Framework
Not only do you have no memory of what was meant, but you never knew in the first place!

This chapter aims to introduce some principals of code hygine, including style, naming conventions, creating useful comments, and will briefly discuss the concept of *linting*, which is a real time error checking process that many integrated development environments (IDE) include.  Keeping this advice in mind will help you create reusable, and easily adaptable code.

## Code Styling

Style guidelines differ between organisations, languages, and over time ^[The Python style guide (PEP) is now in its 8th edition.].
It is important that you work to a framework that is best for your purposes, bearing in mind that consistency makes for easier reading and understanding.

Style guidelines include advice for file naming, variable naming, comments, and the use of whitespace and brackets.
For examples of style guides, follow the following links:

* [PEP8](https://www.python.org/dev/peps/pep-0008/) for Python
* [Hadley Wickham's](http://adv-r.had.co.nz/Style.html) style guide for R
* [Google's](https://google.github.io/styleguide/Rguide.xml) style guide for R
* [Microsoft's](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions) style guide for C#.

## File Naming

The Centre for Open Science has some useful suggestions for naming of files, particularly ensuring that they readable both to humans and computers.  This includes avoiding the use of wildcard characters (@£$%) and using underscores ("_") to delimit information, and dashes ("-") to conjunct information or spaces.  They also suggest dating or numbering files, and avoiding words like FINAL (or FINAL-FINAL).  The dating suggestion is 

## Commenting
Comments has been described as "Love letter to your future self"^[Jon Peirce, developer of PsychoPy]. Keeping clear and concise comments not only allows you to keep track of the decisions you have made, what particular functions do, and what variables are used, it also allows other people to see your thought processes.
The syntax for comments varies with programming languages.  in R and Python, a hashtag is used, whereas in C#, double back-slash is used.

For shorter comments, you can keep them in-line:

```{r}
times = 10 # Set variable times to the integer 10
my_variable = "my variable is %s times better than yours" %times #Set my_variable to a string
print(my_variable) #prints the value
```

For longer comments, information can be included above the code block.

```{r}
#The following function takes a number, multiplies it be 5, and minuses 2.  This may seem pointless, but is simple for the purpose of demonstration.

my_func = function(number){ #R function

(number * 5) - 2
}
print(my_func(2))
```

```
def myfunc(numb): #python function
      return((numb*5)-2)
print(myfunc(8))

```
indent
line length

naming
- CamelCase
- lowerCamelCase
- Underscore_Methods
- Kebab-Case
_ Mixed_Case_With_Underscores
- lowercase

Kebab wont work with some languages, such as R and python since this will be interpreted as a subtraction sign. 



Obviously, these are just guidelines, and you should choose elements that suit your own coding style.  However, it is important to ensure that you are consistent when collaborating, and agree on a common style.  It could be useful to create a readme file describing your approach to coding style so other users can see your decisions.
Code formatting

When making code open, it is important to ensure that it is legible and easy to follow.

Much like writing prose, there are a number of methods available to help make your code clear.  These include use of whitespace, naming, commenting.

Correct naming has a two-fold benefit.  The first is that it allows you to communicate the purpose of a variable or object without additional commenting.  For example participant_data is more informative than df.  It can also let you see the flow of your code or script.  For instance  participant_data_no_outliers <- filter.outliers(participant_data) tells the reader something about the function that the 


The style that you use is down to preference, however it is important to stick to it, and to ensure that your collaborators are using the same style.  Style includes: variable naming; use of whitespace; 

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

Linting is often indicated using underlining of potential problems (much like a spell checker).  Until all of the underlining has disappeared, the code will not run.  The degree of linting will depend on the Integrated Development Environment that you are using (IDE). 

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
