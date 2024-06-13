(rr-documentation-code)=
# Code documentation

It is a good practice to document the source code of software regardless of how time consuming it may be. 
The goal of code documentation is to provide context and explanations for the source code. 
So that others can understand why a piece of sofware exists, how it was built and how to use it or re-use it. 

## Extended Software Documentation

Documenting software may require to prepare extensive descriptions of the key aspects of software, 
such as explanations about how to start using the software, or examples of how to use the sofware for particular tasks. 
What to document will be different for each software, and how to document it will be different for each audience.   
Below, there is guidance on how writing extended software documentation can be approached.

### Divio Documentation System
When extended documentation is necessary, common questions are: What to document? and 
How to organize documentation concisely?
To answer such questions, David Laing, proposed a [documentation system](https://docs.divio.com/documentation-system/) to organize software documentaton. 
The system distinguish between four types of documentation: tutorial, how-to guides, explanatios and reference guides.

* **Tutorials** aim to teach others how to use the software by descrbing things step by step.
For example, how to navigate the graphical interface of software X.
* **How-to guides** describe the specific steps required to solve particular problems with the software in question.
For example, how to find research dataset $A$ in the data archive $B$, using software $X$.
* **Explanations** aim to create understading by providing context to relevant topics for the software.
For example, if software $X$ implements a [quickSort algorithm](https://www.geeksforgeeks.org/quick-sort/) to find a value in a lists of integers,
it might be relevent to include an explanation about why that algorithm was chosen and how such algorithm operates.
* **Reference guides** describe the code and how to use it. 
They should include  descriptions of functions, fields, attributes, methods and APIs, and how to use them.
For example, if software $X$ includes a function $S$ that adds two numbers. 
A reference guide for $S$ should describe what inputs it expects, what outputs it produces and in which cases it can or cannot be used. 

### User's Documentation vs. Developer's Documentation

Another way to think about software documentation is to distinguish between the documentation for the end user of the software, 
and the documentation oriented to describe the insides of the software to other developers. 
This approach for organizing documentation is simpler than [Divios Documentation System](#divio-documentation-system), 
but it does not offer further guidence about how to distiguish which aspects of software documention are relevant for an end user and which are relevant for a developer. 
It is up to the developer's experience to decide what content is relevant and for who.
The table below offers some examples on what might be included as user and developer documentation.

| User Documentation | Developer Documentation |
|----------|----------|
| Installation instructions  | Development setup  |
| Default settings  | How to run tests  |s
| Tutorials | Development roadmap |

> Regardless of which approach is used to document software. The bottom line is 'some documentation is better than no documentation'

## Code Comments 

Some software documentation can be written directly as part of the source code using **code comments**.
Code comments can be included as *block comments* or *inline comments*. 
They are used to explain what some pieces of code do, or to explain why something in the code was done in a particular way. 
A good practice is to comment only what is necessary, and not to aim to comment each single line of code. 

How to write code comments depends on the programming language and the codinging styles that one wants to follow. These are some refereces relevant for writting code comments.

- [Best practices for writting code comments](https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/)
- [Docstrings Converntions for Python](https://peps.python.org/pep-0257/)
- [Creating docstrings in R](https://josephcrispell.github.io/2021/07/26/creating-R-docstring.html)
- [Writtig human readable code](./book/website/project-design/code-styling/code-styling-readability.md)
