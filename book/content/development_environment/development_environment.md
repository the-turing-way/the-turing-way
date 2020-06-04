# Development Environment
<!--
NATALIE's TO-DO list:
* Add an issue about making screenshots of different IDEs/editors and labelling the different parts (e.g. outputs there etc). Decide size of images?.
* REMINDER: Ask my questions in the Gitter channel.
*  How do I link to other bits of the Turing Way? Labels maybe -- add the add labels issue label after it's merged 
* Add IDE to glossary
* Toolkit for new datascientists (in the Po

NATALIE's Questions before I PR:

- What's the format for table of contents? Or does that come after?


## Prerequisites / recommended skill level

<!-- add pre-requisites here -->
<!--
| Prerequisite | Importance | Notes |
| -------------|----------|------|
| Chapter/topic | How important it is | Any notes |
| Command line | 
-->

## Table of contents

<!-- table of contents here -->

<a name="Summary"></a>
## Summary
This chapter is about the environment in which you write and edit your code, this is called your development environment. There are three broad categories: text editors, IDEs (Integrated Development Environments), and notebooks. Within those categories, there are many specific pieces of software (for example vim, sublime text, RStudio, jupyter notebooks). The Turing Way won't tell you which IDE or editor to use (there is no "right" answer), but it will highlight some things that you might want to consider when you're making your choice.

## How this will help you/ why this is useful
The development environment that you choose to program in will contribute to:
* how quick and enjoyable it is to program 
* how quick and easy it is to share your code with different people.
* how quick and easy it is for you to debug<!--link-to-chapter--> your code, to use version control<!--link-to-chapter-->, or use virtual environments<!--link-to-chapter-->.

## The anatomy of an development environment
Before we discuss the differences between the different types of development environments (IDEs, editors, and notebooks), let's take a look at some of their constituent parts. 

### Text editor pane
All development environments will have some form of text editor window. This is where we write the majority of our code: any piece that we would like to save and be able to run again. 

The text editor will tend to have many features which make writing code easier, such as line numbers, multi-line editing, code completion, spell and style checking, and code navigation (see [Features to know about](#features-to-know-about)).

### Output pane
Some code can be run directly from the text editor window, usually by clicking `run`, or using the relevant [keyboard shortcut](#keyboard-shortcuts). In this case, there will be an output window that will show the results of running the saved code. This is where you will see useful messages about (such as error messages, or print statements). 

Sometimes there will also be a separate window within the development environment which allows you to look at image outputs.
 
### Terminal
<!--

Using Git for version control in the terminal.

A lot of code is also designed to be run from the command line with additional arguments.
 -->
 
### The console
In the console, we can type some code and immediately see the output. For example, we can check the value stored in a variable by typing it's name, or we could do a quick sum (`13*24`). The console immediately throws us back the answer: `312`. 

This makes the console useful for experimenting or quickly checking something. For example, checking if a library is loading, crafting a regular expression, or making sure that you remember the syntax of a particular library. 

### File/directory navigation

### Other windows



## What's the difference: IDEs, editors, and notebooks?

### IDEs
IDEs (Integrated Development Environments) *integrate* many [features](#features-to-know-about) that programmers find useful into one place. Rather than being only the place that you write your code, IDEs can also manage [virtual environments](#integrated-virtual-environments), streamline using [version control](#integrated-version-control), or help you to conform to style conventions. While they can provide a lot of useful tools, these tools can require additional computational resources (which can make some IDEs a little slow), and skills to make the most of them. Some IDEs may provide features that you know you won't need (for example, for managing deployment of websites).
Examples of IDEs: RStudio, PyCharm, Visual Studio

<!-- TODO: Maybe put an image of an IDE here, with some different panes labelled -->

### Text editors
Text editors offer a bare-bones code-writing environment. The only feature that they will definitely have is allowing you to write the text. You will probably want one, however, that will also allow you to run the code from the editor and show you the output, which rules out something like TextEdit or wordpad (code *can* be written on those, too, but few people would choose to). Editors take up less space on your machine than a big IDE, and can sometimes be faster to write in compared to IDEs. They are often customisable, allowing you to add new [features](#features-to-know-about) over time as they become useful to you. 
Examples of Text editors: Sublime Text, Visual Studio Code, Emacs

<!-- TODO: Maybe put an image of an editor here, with the fact that there is only the editor pane labelled -->

### Notebook editors
Notebooks (like Jupyter Notebooks, or R Markdown Notebooks for example) are a popular file format for data science, which put code and the outputs they produce close to one another. For example RMarkdown Notebook `.Rmd` files are written inside RStudio (an IDE with the aforementioned benefits of an [IDE](#IDEs)), but plus some extra functionality ([code chunks!](#code-chunks)<!--TODO: put in link-->). On the other hand Jupyter Notebook `.ipynb` files are usually written inside a Jupyter Notebook or JuptyterLab environment. Some multi-purpose IDEs also support writing in these notebook formats.

<!--picture of chunks-->

The benefit of writing in a notebook is the ability to write your code alongside notes about what you are doing, and run different chunks (often called cells or blocks) of your code separately. The output (such as graphs or tables) of a chunk of code is displayed under each chunk, and will remain visible until you rerun that chunk. This helps you to create a document of your work  to record process and results, much like a lab notebook. Many people also prefer the process of using notebooks for their analysis. You can save the mixture of code, notes, and outputs to share with others.

:::info
#### Notes on notebooks

**Default notebook editors don't have some useful features.**
As mentioned, notebooks have some benefits above writing regular scripts. However, some people find that the Jupyter Notebook environment is missing some of their favourite features. This can particularly come into play when writing bigger pieces of software or analysis pipelines.

**Moving and editing code chunks out of order can create problems.**
In notebooks, the code is divided into chunks which can be run independently. This can be great if you only want to re-run one section of the notebook. However, forgetting to run a cell or changing the order of the cells can create problems. For example, thinking you have an up to date figure when you don't, or the notebook throwing error messages when all cells are run from top to bottom.

**Notebooks integrate with some other useful technology**
<!--TODO: fill in/link-->
:::

## Literate programming
<!-- Does this comes up somewhere else in the Turing Way?? - link it?) -->

## Features to know about

### Debuggers
<!-- TODO: This should be a chapter with stuff like: print statements, assert statements, how to use debuggers, etc.-->
Debuggers lets you find mistakes in your code more easily<!--LINK TO THE DEBUGGING CHAPTER-->. You can step through code a line at a time (or at specific "breakpoints") and check the contents of variables to find where your code is doing something different than you were expecting.

Many IDEs contain visual debuggers - the debugger is part of the graphical user interface of the editor, so you can see how breakpoints and the current position of the debugger in the code relates to the code you are writing. For example, you can click to place breakpoints next to the code you have written. Visual debuggers aren't the only option for debugging, there interactive text-based debuggers, too (for example in the form of Python modules), which allow you to do the same thing by writing code instead of visually.

### Auto-complete
A really useful feature is being able to write variable and function names, file paths, etc, with far fewer key strokes. Many IDEs will allow you to do<!--format?-->

### Shortcuts for common manipulations of code text
IDEs and editors allow you to do a lot of common maniplulations of code text much more easily.

Here are some of my favourites:
* Comment or uncomment a section of code.
* Changing all instances of a variable (to rename it).
* Moving a block of code up or down.

I really recommend learning some of the [keyboard shortcut](#Keyboard-shortcuts) for these in your chosen IDE!

### Integrated version control
You can read more about version control <!--[here](LINK)-->. 

### Syntax and style highlighting

### Virtual environments
<!-- Presumably this comes up somewhere else in the Turing Way - link it?) -->

## How to choose?
- Ask your friends and colleagues what they would recommend. Knowing who you can ask questions to can be helpful when you're getting used to a new environment. 
- Decide which features you care about and choose an editor, IDE, or notebook that has those features.
- Try one out, you might cycle through a few until you find one you like.
- Consider interoperability with other tools which you might want to use (e.g. BinderHub)
<!-- Mention Open Source? -->
<!-- TODO: ask for ome stories other than mine-->

> "My ideal editor has changed over time. When I started my PhD, I tried PyCharm (a fairly substantial IDE for Python) and I *hated* it at first. It had too many features I didn't need or want. Instead, I happily used a much more basic editor for many years (Sublime Text), before moving on to notebooks. Years later, I tried PyCharm again and now I absolutely love it!" - Natalie Thurlby

### Table of features and some popular editors/IDEs.
<!--Yes tick, No tick, Possible with upgrades cog emoji-->

## Tips for getting the most out of IDEs

### Using `TODO:`
<!--TODO: Think about how this could be made into a case study?-->
Features of IDEs veer beyond software development into project management and productivity.

If you need to remind yourself about a small task that you need to do in a script, you can write notes for yourself in a `TODO` comment. For example, this would look like: `# TODO: Write a test for this function.` in Python, or `<!-- TODO: Add an example.--> ` in markdown. 

Some IDEs will let you look at all `TODO` comments in a project, organised by directory and script. These shouldn't replace other good practices (like using GitHub issues) <!--link-->, but can be especially handy for projects that you work on infrequently as just by opening the file, you have the notes about what to work on next. I also find it handy to link to GitHub issues in the comments.

### Keyboard shortcuts:
Getting to know the keyboard shortcuts for your chosen IDE can save a lot of time. These can be for manipulating text

<!--
## Checklist
> this can be done at the end or maybe as a separate checklist exercise, but please do note things down here as you go
-->

<!--
## What to learn next
> recommended next chapters that are a good next step up
-->

<!--
## Further reading
> top 3/5 resources to read on this topic (if they weren't licensed so we could include them above already) at the top, maybe in their own box/in bold.
> less relevant/favourite resources in case someone wants to dig into this in detail
-->

<!--
## Definitions/glossary
> Link to the glossary here or copy in key concepts/definitions that readers should be aware of to get the most out of this chapter
-->

<!--
## Bibliography
> Credit/urls for any materials that form part of the chapter's text.
-->