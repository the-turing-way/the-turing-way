(ch-consistency-language)=
# Language

Language is concerned with the way concepts and ideas in _The Turing Way_ are expressed.
A consistent language ensures that _The Turing Way_ is clear and understandable.

(ch-consistency-language-hr)=
## Hard Requirements

The hard checks that deal with _The Turing Way's_ language include:

(ch-consistency-language-hr-grammar)=
### Check 1: Ensure correct grammar and a consistent tone across the book

Correct grammar and consistent tone would help readers of all backgrounds, knowledge, and skill levels to better understand _The Turing Way_'s content.

Aside from being distracting, incorrect grammar might take away what a piece of text is trying to communicate.

Tools such as [Grammarly](https://grammarly.com), [Ginger Grammar](https://gingersoftware.com/grammarcheck), and [Reverso Speller](https://reverso.net/spell-checker/english-spelling-grammar/) can help catch grammatical errors present in a piece of text.
These tools can be used to assess grammar in new contributions and existing content of _The Turing Way_.
Furthermore, when raising PRs for new content, invite reviewers to check for grammar as well.
This could help minimize the number of grammatical errors that make it to the final version of _The Turing Way_.

With respect to tone, ensure that chapters adhere to a formal style of writing and that sentences are easy to digest.
One rule of thumb to consider is that if a sentence needs to be read more than once to be understood, then it likely needs to be rephrased.

#### Demo

<div class="video-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/Prv23kGekVY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

(ch-consistency-language-hr-language)=
### Check 2: Ensure chapters use a consistent language

```{note} Language, in this context, refers to the American and British variants of the English language.
```

With contributors from around the world, _The Turing Way_ does not restrict the language used to write chapters.
This makes it easier for contributors to bring in their perspectives as they write content for _The Turing Way_.
Rather, the recommendation is that if a chapter is written in one style (for example, British English), then it should remain consistent throughout.
This makes _The Turing Way_ less distracting and easier to read.

(ch-consistency-language-hr-abbreviations)=
### Check 3: Ensure Latin abbreviations are not used in writing chapters

When writing content for _The Turing Way_, the use of Latin abbreviations is discouraged.
This is because screen readers may read them aloud in a manner that is confusing to those who rely on such devices.

Furthermore, as described in the {ref}`style guide<ch-style>`, contributions that contain Latin abbreviations will fail the _The Turing Way_ repository's continuous integration workflow.

Please refer to the {ref}`style guide<ch-style>` for recommendations on how to avoid common Latin abbreviations in your writing.
