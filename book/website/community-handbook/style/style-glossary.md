(ch-style-glossary)=
# Glossary

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
