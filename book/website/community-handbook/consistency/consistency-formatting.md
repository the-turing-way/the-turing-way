(ch-consistency-formatting)=
# Formatting

Formatting refers to how _The Turing Way_ book is written and directly affects the book's appearance and presentation.

_The Turing Way_ is hosted online as a Jupyter Book and uses the formatting recommendations as described in their [documentation](https://jupyterbook.org/intro.html).
Proper formatting ensures that _The Turing Way_ is readable, accessible, and resembles a modular piece of work.


(ch-consistency-formatting-hr)=
## Hard Requirements

The hard requirements in the consistency checklist ensure that _The Turing Way_ prioritises accessibility, collaboration, readability and ease of use. 
The checks that deal with the _The Turing Way's_ formatting include: 

(ch-consistency-formatting-hr-one)=
### Check 1: Add labels to chapters, subchapters, sections and images to enable cross-referencing

Often, a chapter might refer to content from another chapter to explain a concept or expand on a point.
Cross-Referencing facilitates this by ensuring that the referred content is easy to find with a simple click.
Cross-Referencing helps make _The Turing Way_ easily navigable and accessible.

{ref}`Cross-Referencing <ch-style-crossref>` is discussed in detail in the {ref}`ch-style-guide`. The subchapter explains what labels are, provides a naming convention for labels in _The Turing Way_, and gives several useful examples for how cross-referencing should be done.

(ch-consistency-formatting-hr-two)=
### Check 2: Convert `HTML` formatting to Markdown

_The Turing Way_ is a [`jupyter-book`](https://jupyterbook.org/intro.html) and should be written in [Markdown](https://en.wikipedia.org/wiki/Markdown), where possible, so that it renders as intended. 

Some chapters in _The Turing Way_ are not entirely written in Markdown, making some of its content hard to read.
For example, in the {ref}`Licencing <rr-licensing>` chapter of the {ref}`rr`, the {ref}`Software Licences <rr-licensing-software>` subchapter contains a table that is written in `HTML`.

```{figure} ../../figures/html_to_markdown.png
---
name: html_to_markdown
alt: A screenshot of a poorly formatted table written in HTML. The table is squished together making it hard to decipher its meaning.
---
Content written in HTML may not render properly.
```

However, when converted to Markdown, the table becomes cleaner and easier to read.

```{figure} ../../figures/html_to_markdown2.png
---
name: html_to_markdown2
alt: A screenshot of a table converted to Markdown from HTML. The table becomes easier to read and understand when converted to Markdown.
---
Converting HTML to Markdown makes The Turing Way easier to read.
```
> A PR that addresses this check can be found [here](https://github.com/alan-turing-institute/the-turing-way/pull/1460).

Chapter content written in `HTML` are usually enclosed in tags which begin and end with angle brackets `<>`. [W3Schools](https://www.w3schools.com/html/html_elements.asp) is an excellent resource for understanding what these tags mean, and Markdown reference guides, such as [this](https://www.markdownguide.org/cheat-sheet/), can help in translating `HTML` formatting to Markdown.
There are also helpful [tools](https://jmalarcon.github.io/markdowntables/) that convert HTML to Markdown with a single click.

Please note that it may not always be possible to convert `HTML` to Markdown. 
In such cases, it is acceptable to leave the formatting as it is, if the content can still be read and understood. 
For example, superscripts and subscripts can not be written in Markdown.
They must be written in `HTML` with their [corresponding tags](https://support.squarespace.com/hc/en-us/articles/206543587-Markdown-cheat-sheet#toc-superscript-and-subscript).

(ch-consistency-formatting-hr-three)=
### Check 3: Convert image formatting from Markdown to `MyST`

Some figures and images in _The Turing Way_ are written using Markdown syntax.
While this works, it does not allow the images to adapt to the screen size of the device the book is read from. 

Markedly Structured Text (`MyST`) is a flavour of Markdown that addresses this and allows the inclusion of responsive images in the _The Turing Way_.

Converting images from Markdown to `MyST` is explained in {ref}`this <ch-style-figures>` subchapter of the {ref}`ch-style-guide`.

(ch-consistency-formatting-hr-four)=
### Check 4: Ensure chapters are consistent with the Turing Way Style Guide

Although the {ref}`ch-style-guide` contains suggestions to help keep _The Turing Way_ accessible and consistent, not all chapters follow these suggestions.

As _The Turing Way_ evolves and improves, the {ref}`Style Guide's <ch-style-guide>` recommendations will remain an essential point of reference. 
To ensure that accessibility and consistency in _The Turing Way_ can be retrospectively achieved, a suggestion is to read through the book keeping while keeping the {ref}`Style Guide's <ch-style-guide>` recommendations in mind. 

An overview of these recommendations are itemised below, and detailed explanations about each suggestion can be found in the {ref}`ch-style-guide`.

- Recommendations
    - Write each sentence in a new line
    - Avoid Latin abbreviation
    - Cite and reference external resources appropriately
    - Follow _The Turing Way_'s convention for cross-referencing
    - Follow _The Turing Way_'s convention for adding images to chapters


(ch-consistency-formatting-hr-five)=
### Check 5: Add ALT text to images

Alternative text (ALT text) are the invisible image descriptions that are read aloud to readers of _The Turing Way_ who use a screen reader.

If no ALT text is provided with an image, these users will be unable to understand the intended message of the image.

To maintain and promote accessibility in _The Turing Way_, ensure that all images in a chapter contain ALT text.

Adding ALT text to an image is discussed in {ref}`this <ch-style-figures>` subchapter of the {ref}`ch-style-guide`.

(ch-consistency-formatting-hr-six)=
### Check 6: Fix Markdown formatting of non-consecutive headers

Non-consecutive headers refer to an increase in header levels of more than one. 
For example:

```
# Heading
### Another Heading
```
Such an increase of two header levels results in warnings when building _The Turing Way_ locally.
Ideally, all Markdown files should start with a level 1 heading and increase sequentially as appropriate.

```
# Heading
## Another Heading
```

Several files in _The Turing Way_ do not follow this convention. 
A list of such files can be found in [this issue](https://github.com/alan-turing-institute/the-turing-way/issues/1321), and [this PR](https://github.com/alan-turing-institute/the-turing-way/pull/1451) demonstrates how to fix a file with non-consecutive headers.

(ch-consistency-formatting-sr)=
## Soft Requirements

Soft requirements help improve the overall look and feel of _The Turing Way_.
When effected, these checks may go unnoticed, but they also make _The Turing Way_ a polished piece of work.
Soft requirements that deal with _The Turing Way's_ formatting include: 

(ch-consistency-formatting-sr-one)=
### Check 1: Ensure the titles of chapters\subchapters match the left ToC

The titles of some chapters and subchapters in _The Turing Way_ do not match their corresponding references in the ToC on the left of the webpage.
This may be confusing for some users, especially when the chapter\subchapter's reference in ToC significantly varies from the chapter\subchater's title.

```{figure} ../../figures/mismatched_title_toc.png
---
name: mismatched_title_toc
alt: A depiction of a subchapter whose title differs from its reference in the Table of Contents. The title of the subchapter is 'Using Spreadsheets for Research Data', however in the Table of Contents, it is referred as 'Data Organisation in Spreadsheets'.
---
The title of this subchapter is 'Using Spreadsheets for Research Data', however the TOC refers to the same file as 'Data Organisation in Spreadsheets'.
```

In ensuring that _The Turing Way_ passes this check, one recommendation to follow is to keep the titles short.
If a chapter's title and ToC reference differ, make the shorter of the two the chapter's title, and update the `.toc.yml` if necessary. 
However, remember that the final title should adequately tell readers what to expect from a chapter.


(ch-consistency-formatting-sr-two)=
### Check 2: Ensure proper title-casing for headers

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

For example, In {ref}`<mismatched_title_toc>` above, **Using spreadsheets for research data** should be title-cased to **Using Spreadsheets for Research Data**.

Certain headers may not need to be title-cased depending on the context in which they are used.
For example, because some of the headers in this chapter make up a checklist, they do not need to be title-cased.
