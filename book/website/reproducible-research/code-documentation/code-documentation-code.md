# Code documentation

It is a good practice to document the source code of software regardless of how time consuming it may be. 
The goal is to provide context and explanations for the source code, so that other can understand why a piece o sofware was build, how it was build and how to use it or re-use it. 

## Code Comments 

Sofware can be documented by including comments direclty as part of the source code. 
Comments can be *block comments* or *inline comments*. 
They can be used to explain what some pieces of code  do, or to explain why something was done. 
A good practice is to comment only what is necessary, and not to aim to comment each single line of code. 

How to write comments depends on the programming language. These are some refereces:

- [Best practices for writting code comments](https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/)
- [Docstrings Converntions for Python](https://peps.python.org/pep-0257/)
- [Creating docstrings in R](https://josephcrispell.github.io/2021/07/26/creating-R-docstring.html)
- [Writtig human readable code](./book/website/project-design/code-styling/code-styling-readability.md)

## Extended Software Documentation

Use code comments is not enough to document all important aspects of software. 
Therefore, software may also require to prepare extensive descriptions of the key aspects of the software, 
and include guidence and exemples of how to use the sofware. 

### Divio Documentation System
When extended documentation is necessary, common questions are What to document? and 
How to organize documentation concisely?
To answer such questions, David Laing, proposed a [documentation system](https://docs.divio.com/documentation-system/) to organize software documentaton. 
The system distinguis between four types of documentation: tutorial, how-to guides, explanatios and reference guides.

**Tutorials** aim to teach other how to use the software by descrbing things step by step.
For example, how to navigate the graphical interface of software X.

**How-to guides** describe the steps required to solve particular problems with the software in question.
For example, how to find research dataset A in the data archive B, using software X.

**Explanations** aim to provide understading by providing context to relevant topics for the software.
For example, If software X implements a [quickSort algorithm](https://www.geeksforgeeks.org/quick-sort/) to find a value in a long lists of integers,
it might be relevent to include an explanation about why that algorithm was chosen.

**Reference guides** describe the code and how to use it. 
It should include  description of functions, fields, attributes, methods and APIs, and set out how to use them.
For example, if software X includes a function S that adds two numbers. 
A reference guide for S should describe what inputs it expects, what outputs it produces and in which cases it can be used. 


### User's Documentation vs. Developer's Documentation

Another way to thing about software documentation is distinguish between documentation for the end user of the softwared, 
and the documentation oriented to describe the insides of the software to other developers. 
This approach for organizing documentation is simpler than [Divios Documentation System], 
but it does not offer further guidence about how to distiguish which aspects of software documention are relevant for an end user and which are relevant for a developer. 
It is up to the developer's experience to decide what content is relevant and for who.
The table below offers some examples on what might be included as user and developer documentation.

| User Documentation | Developer Documentation |
|----------|----------|
| Installation instructions  | Development setup  |
| Default settings  | How to run tests  |s
| Tutorials | Development roadmap |

Regardless of which approach is used to document software. The bottom line is 'some documentation is better than no documentation'
