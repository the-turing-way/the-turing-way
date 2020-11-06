(ch-consistencylanguage)=
# Language

Language is concerned with the style with which _The Turing Way_ is written.
A consistent language ensures that _The Turing Way_ is clear and understandable.

(ch-consistency-language-hr)=
## Hard Requirements

The hard checks that deal with _The Turing Way's_ language include: 

(ch-consistency-language-hr-grammar)=
### Check 1: Ensure correct grammar and a consistent tone across the book

For readers of all backgrounds, knowledge, and skill level to understand _The Turing Way_, correct grammar and a consistent tone is necessary.

Asides from being distracting, incorrect grammar may take away from the message a piece of text tries to communicate.

Tools such as [Grammarly](www.grammarly.com), [Ginger Grammar](https://www.gingersoftware.com/grammarcheck), and [Reverso Speller](https://www.reverso.net/spell-checker/english-spelling-grammar/) can help to catch any grammatical errors present in a piece of text. 
These tools can be used to grammatically assess new contributions and existing content of _The Turing Way_ chapters.
Furthermore, when raising PRs for new content, invite reviewers to check for grammar as well.
This helps to minimise the number of grammatical errors that make it to the final version of _The Turing Way_.

With regards tone, ensure that chapters adhere to a formal level of writing and that sentences are easy to digest.
One rule of thumb to think about is, if a sentence needs to be read more than once to be understood, then it needs to be rephrased.

(ch-consistency-language-hr-language)=
### Check 2: Ensure chapters use a consistent language

```{note} Language, in this context, refers to the American and British variants of the English language.
```

With contributors from around the world, _The Turing Way_ does not restrict the language used to write chapters.
This makes it easier for contributors to bring in their perspectives as they write content for _The Turing Way_.
Rather, the recommendation is that if a chapter is written in one style (for example, British English), then it should stay consistent throughout. 
This makes _The Turing Way_ less distracting and easier to read.

(ch-consistency-language-hr-abbreviations)=
### Check 3: Ensure chapters do not use any Latin abbreviation

When writing content for _The Turing Way_, the use of Latin abbreviations is discouraged. 
This is because screen readers may read them aloud in a manner that is confusing to readers who rely on such devices.

Furthermore, as described in the {ref}`style guide<ch-style-guide>`, contributions that contain Latin abbreviations will fail the _The Turing Way_ repository's continuous integration workflow.

Please refer to the {ref}`style guide<ch-style-guide>` for recommendations on how to avoid common Latin abbreviations in your writing.