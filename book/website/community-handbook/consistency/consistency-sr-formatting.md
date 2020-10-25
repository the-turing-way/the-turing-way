(ch-consistency-sr-formatting)=
# Soft Requirements - Formatting

Soft requirements help improve the overall look and feel of _The Turing Way_.
When effected, these checks may go unnoticed, but they also make _The Turing Way_ a polished piece of work.
Soft requirements that deal with _The Turing Way's_ formatting include: 

(ch-consistency-sr-formatting-one)=
## Check 1: Ensure the titles of chapters\subchapters match the left ToC

The titles of some chapters and subchapters in _The Turing Way_ do not match their corresponding references in the ToC on the left of the webpage.
This may be confusing for some users, especially when the chapter\subchapter's reference in ToC significantly varies from the chapter\subchater's title.

```{figure} ../../figures/mismatched_title_toc.png
---
name: mismatched_title_toc
alt: A depiction of a subchapter whose title differs from its reference in the Table of Contents.
---
The title of this subchapter is 'Using Spreadsheets for Research Data', however the TOC refers to the same file as 'Data Organisation in Spreadsheets'.
```

In ensuring that _The Turing Way_ passes this check, one recommendation to follow is to keep the titles short.
If a chapter's title and ToC reference differ, make the shorter of the two the chapter's title, and update the `.toc.yml` if necessary. 
However, remember that the final title should adequately tell readers what to expect from a chapter.


(ch-consistency-sr-formatting-two)=
## Check 2: Ensure proper title-casing for headers

The titles of some chapters in _The Turing Way_ do not follow proper title-casing.
[Wikipedia](https://en.wikipedia.org/wiki/Title_case) describes title-casing as a capitalisation style used to format the titles and headings of published works.
Being a citeable reference for individuals seeking to carry out reproducible data science, titles and headings in _The Turing Way_ should be title-cased.

Although _The Turing Way_ does not follow a specific title capitalisation style, some general (non-exhaustive) rules to consider, include:
- Capitalise principal or important words
- Lowercase articles, conjunctions, and prepositions (unless when these are stressed)
- Capitalise the first and last words

There are helpful tools, such as [CapitalizeMyTitle](https://capitalizemytitle.com/), that help with title-casing.
Headers in _The Turing Way_ can be run through these tools to check if they follow title-casing conventions.
They can then be replaced within chapters and in the `_toc.yml` as appropriate.

For example, In {ref}`figure 1 <mismatched_title_toc>` above, **Using spreadsheets for research data** should be title-cased to **Using Spreadsheets for Research Data**.

Certain headers may not need to be title-cased depending on the context in which they are used.
For example, because some of the headers in this chapter make up a checklist, they do not need to be title-cased.