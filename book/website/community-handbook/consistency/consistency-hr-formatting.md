(ch-consistency-hr-formatting)=
# Hard Requirements - Formatting

The hard requirements in the consistency checklist ensure that _The Turing Way_ prioritises accessibility, collaboration, readability and ease of use. 
The requirements that deal with the _The Turing Way's_ formatting include: 

(ch-consistency-hr-formatting-one)=
## Check 1: Add labels to chapters, subchapters, sections and images to enable cross-referencing

Often, a chapter might refer to content from another chapter to explain a concept or expand on a point.
Cross-Referencing facilitates this by ensuring that the referred content is easy to find with a simple click.
This contributes to making _The Turing Way_ easily navigable and accessible.

{ref}`Cross-Referencing <ch-style-crossref>` is discussed in detail in the {ref}`ch-style-guide`. The subchapter explains what labels are, provides a naming convention for labels in _The Turing Way_, and gives several useful examples for how cross-referencing is done.

(ch-consistency-hr-formatting-two)=
## Check 2: Convert `HTML` formatting to Markdown

_The Turing Way_ is a [`jupyter-book`](https://jupyterbook.org/intro.html) and should be written in [Markdown](https://en.wikipedia.org/wiki/Markdown), where possible, so that it renders as intended. 

Some chapters in _The Turing Way_ are not entirely written in Markdown, making some of its content hard to read.
For example, in the {ref}`Licencing <rr-licensing>` chapter of the {ref}`rr`, the {ref}`Software Licences <rr-licensing-software>` subchapter contains a table that is written in `HTML`.

```{figure} ../../figures/html_to_markdown1.png
---
height: 189px
name: html_to_markdown1
alt: A screenshot of a poorly formatted table written in HTML.
---
Figure 1: A screenshot of a table converted to Markdown from HTML.
```

However, when converted to Markdown, the table becomes cleaner and easier to read.

```{figure} ../../figures/html_to_markdown2.png
---
height: 319px
name: html_to_markdown2
alt: A screenshot of a table converted to Markdown from HTML.
---
Figure 2: A screenshot of a table converted to Markdown from HTML.
```
> The PR that addresses this check can be found [here](https://github.com/alan-turing-institute/the-turing-way/pull/1460).

Chapter content written in `HTML` are usually enclosed in tags which begin and end with angle brackets `<>`. [W3Schools](https://www.w3schools.com/html/html_elements.asp) is an excellent resource for understanding what these tags mean, and Markdown reference guides, such as [this](https://www.markdownguide.org/cheat-sheet/), can help in translating them from `HTML` to Markdown.
There are also helpful [tools](https://jmalarcon.github.io/markdowntables/) that convert HTML to Markdown with a single click.

Please note that it may not always be possible to convert `HTML` to Markdown. 
In this case, it is acceptable to leave the formatting as it is if the content can still be read and understood. 
For example, superscripts and subscripts can not be written in Markdown.
They must be written in `HTML` with their [corresponding tags](https://support.squarespace.com/hc/en-us/articles/206543587-Markdown-cheat-sheet#toc-superscript-and-subscript).

(ch-consistency-hr-formatting-three)=
## Check 3: Convert image formatting from Markdown to `MyST`

Some figures and images in _The Turing Way_ are written using Markdown syntax.
While this works, it does not allow the images to adapt to the screen size of the device the book is read from. 

Markedly Structured Text (`MyST`) is a flavour of Markdown that addresses this and allows the inclusion of responsive images in the _The Turing Way_.

Converting images from Markdown to `MyST` is explained in {ref}`this <ch-style-figures>` subchapter of the {ref}`ch-style-guide`.

(ch-consistency-hr-formatting-four)=
## Check 4: Ensure chapters are consistent with the Turing Way Style Guide

Although the {ref}`ch-style-guide` contains suggestions to help keep _The Turing Way_ accessible and consistent, not all chapters follow these suggestions.

As _The Turing Way_ evolves and improves, the {ref}`Style Guide's <ch-style-guide>` recommendations will remain an essential point of reference. 
To ensure that accessibility and consistency in _The Turing Way_ can be retrospectively achieved, a suggestion is to read through the book keeping its recommendations in mind. 

An overview of these recommendations are itemised below, and detailed information about each suggestion can be found in the {ref}`ch-style-guide`.

- Recommendations
    - Write each sentence in a new line
    - Avoid Latin abbreviation
    - Cite and reference external resources appropriately
    - Follow _The Turing Way_'s convention for cross-referencing
    -  Follow _The Turing Way_'s convention for adding images to chapters


(ch-consistency-hr-formatting-five)=
## Check 5: Add ALT text to images

Alternative text (ALT text) are the invisible description of images that are read aloud to readers of _The Turing Way_ who use a screen reader.

If no ALT text is provided with an image, these users will be unable to understand the intended message of the image.

To maintain and promote accessibility in _The Turing Way_, ensure that all images in a chapter contain ALT text.

Adding ALT text to an image is discussed in {ref}`this <ch-style-figures>` subchapter of the {ref}`ch-style-guide`.

(ch-consistency-hr-formatting-six)=
## Check 6: Fix Markdown formatting of non-consecutive headers

Non-consecutive headers refer to an increase in header levels of more than one. 
For example:

```
# Heading
### Another Heading
```
This results in warnings when building _The Turing Way_ locally, as headers should be sequential.

```
# Heading
## Another Heading
```

Several files in _The Turing Way_ do not follow this convention. 
A list of such files can be found in [this issue](https://github.com/alan-turing-institute/the-turing-way/issues/1321) and [here](https://github.com/alan-turing-institute/the-turing-way/pull/1451) is a good PR that addresses it. 