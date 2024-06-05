(ch-style-more-features)=
# Glossary, Special Blocks and More Styling

Jupyter Book offers more options for styling its chapters and creating a more comprehensive book.
In this subchapter, we discuss a few more features that we recommend using in _The Turing Way_.

(ch-style-more-features-glossary)=
## Glossary

_The Turing Way_ has a {ref}`glossary` file located in the Afterword of the book, which comprises of definitions of different terms in alphabetical order.
This file can be updated with the definitions of new terms, which can then be linked to any chapter in the book where this term occurs.

To add an entry for a new term, please jump to the right alphabetical section of the {ref}`glossary` file and use the following syntax:

```
New Term-1
  A short sentence defining the term. This sentence is indented below the term.
```

For example, [terms starting with 'A'](https://book.the-turing-way.org/afterword/afterword.html#a) are written in the same text-block as shown below:
```

## A

```{glossary}

Acceptance Testing
 A level of the software testing process where a system is tested for acceptability. The purpose of this test is to evaluate the system's compliance with the project requirements and assess whether it is acceptable for the purpose.

Add
 Command used to add files to the staging area. Allows the user to specify which files or directories to include in the next commit.

Authors
  Authors in this context are the contributors to _The Turing Way_ project who have made a substantial contribution to the project such as writing a subchapter, facilitating community interactions, maintaining project’s infrastructure and supporting the participation of others through mentored-contributions. All authors are named co-authors on the book as a whole.

```

To reference terms in your glossary, use the syntax ```[{term}`def<Term>`]```.

For example, to link the term 'Authors' to its definition in the glossary file, please use the syntax ```[{term}`def<Authors>`]``` next to where this term appears, which should render online like this: "*Authors [{term}`def<Authors>`] has been referenced here.*"

(ch-style-more-features-blocks)=
## Special Content Blocks

When writing a new chapter or revising an existing one, you may wish to add notes that do not fit in with the rest of the chapter's narrative but may be useful to the readers and help them understand the chapter better.

Jupyter Book allows the use of special content blocks to highlight a piece of text that needs to stand out from the rest the content on a page. 
This visually separates the block of text from the rest of the page, and ensures that it easily captures the reader's attention.

To add a special content block (note, warning or admonition) to your page, use the following directive:

````
```{note}
This is a sample note!
```
````

which renders as follows:

```{note}
This is a sample note!
```

You can give content blocks custom titles and styling to reinforce your intended message. 
For example, if you wanted to warn the reader about something, you may make a warning block using the following directive:

````
```{warning}
This is a stern warning!
```
````

Note the new title, icon, and colour scheme.

```{warning}
This is a stern warning!
```

There are many more ways to customise content blocks to suit your writing needs. 
Refer to the [Jupyter Book documentation](https://jupyterbook.org/content/content-blocks.html#notes-warnings-and-other-admonitions) and the [Admonition Demo page](https://sphinx-book-theme.readthedocs.io/en/latest/reference/kitchen-sink/admonitions.html) for more recommendations.
