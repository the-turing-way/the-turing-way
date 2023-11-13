(ch-style-crossref)=

# Cross-Referencing Sections and Chapters

We recommend using the cross-referencing style as described in the [Jupyter Book](https://jupyterbook.org/content/citations.html) for chapters or files, and different contents of chapters such as sections and figures.

In Jupyter Book, labels are a way to add tags to parts of your content or a file that you can reference later on.
This is very helpful because you can insert labels to other parts of your book without worrying about the relative or absolute paths of the file.

In this document, we have provided examples to describe how you can use labels for different chapters or part of chapters within the book.
We have also defined a naming convention for labels for _The Turing Way_ to ensure that the locations of these labels in the book are identifiable by their name.

## Labels in Jupyter Book

To add a label for a section or a chapter/subchapter, use a syntax of the following pattern before the element you wish to label:

```
(my-label-name)=
# The thing that I want to label
```

You can insert cross-references to the labels of sections in your file with the following syntax:

```
{ref}`my-label-name`

```

Similarly, you can use labels for cross referencing chapters or subchapters.

Please see details in the examples given below.

### _The Turing Way_ naming convention for the labels

We recommend using the following naming standard for labels, which will allow different authors and contributors of _The Turing Way_ to intuitively identify the locations of the files where these labels have been created.

The following naming convention for the labels for different chapters:

```
(sectioninitials-filename)=
```

Here, the first placeholder `sectioninitials` should be replaced by the initials for different sections in the book and the second placeholder `filename` should be replaced by the name of file where the label is being created.

For the different Guides of the book, we will use the following `sectioninitials`:

- Reproducible Research: `rr`
- Project Design: `pd`
- Collaboration: `cl`
- Communication: `cm`
- Ethical Research: `er`
- Community Handbook: `ch`

For example, in the guide `Reproducible Research`, we have a chapter called `Overview`.
We have created a label for that chapter called `rr-overview` by adding the label on the top of the header by using the following directive

```
(rr-overview)=
# Overview
```

Similarly, for different subchapters we recommend extending the label name with another placeholder for the subchapter's name.
For example, `rr-overview-resources` is a label in the guide "Reproducible Research" (rr) for the subchapter "Resources" for the "Overview" chapter (overview-resources).
This label can be created by using the following directive in the corresponding file:

```
(rr-overview-resources)=
# Resources
```

In the same manner, for different sections in a subchapter we recommend extending the label name with another placeholder.
This can be chosen by the authors, which should be a short yet sensible name for the section where the label is being created.
For example, `rr-overview-resources-addmaterial` is a label in the guide "Reproducible Research" (rr) for the subchapter "Resources" for the "Overview" chapter (overview-resources) for the section for "Additional Materials" (addmaterial).
This label can be created in the corresponding file for the suggested section name using the following directive:

```
(rr-overview-resources-addmaterial)=
## Additional Material
```

### Examples of cross-referencing

**Examples for cross-referencing sections of chapters and subchapters**

We will use examples for the chapters in the "Reproducible Research" guide located in the `book/website` directory.

**_Case 1_**: When you cross-reference a section of the chapter within the same file _before_ a label has been created.

Taking the previous example of `rr-overview-resources-addmaterial`, we can use this label to cross-reference
it in an earlier section within the same file using the following:

```
{ref}`rr-overview-resources-addmaterial`
```

This will appear in the online book like so: {ref}`rr-overview-resources-addmaterial`.

**_Case 2_**: When you cross-reference a section of the chapter within the same file _after_ a label has been created.

In the same subchapter "Resources", we have created a label `rr-overview-resources-reading` for the section "Further Reading".
We can cross-reference it in a later section within the same file using the following:

```
{ref}`rr-overview-resources-reading`
```

It will appear in your chapter like this: {ref}`rr-overview-resources-reading`.

**_Case 3_**: When you cross-reference a section of a chapter in a different file (chapter) before or after a label has been created.

In the subchapter "Definitions" of the "Overview" chapter, we have created a label
`rr-overview-definitions` for the section "Table of definitions for reproducibility".

We can cross-reference it in a different subchapter or chapter.
In this case, let's cross-reference it in the landing (main) page of the "Overview" chapter by using the following:

```
{ref}`rr-overview-definitions`
```

It will appear in your chapter like this: {ref}`rr-overview-definitions`.

Though we are demonstrating this example for subchapters within the same chapter ("Overview"), the similar syntaxes can be used for cross-referencing in other chapters within the book.

**Examples for Cross referencing chapters and subchapters**

**_Case 4_**: Cross-referencing a chapter or subchapter in a different file (chapter/subchapter) before or after a label has been created.

For example, in the landing page of the chapter "Open Research", we have created a label `rr-open`.
We can cross-reference it in the section "What to learn next?" in a different subchapter "Resources" of the "Overview" chapter by using the following:

```
{ref}`rr-open`
```

It will appear in your chapter like this: {ref}`rr-open`.

Though we are demonstrating this example for cross-referencing chapters and subchapters across the book, the same syntax can be used for cross-referencing subchapters within the same chapter.

### Providing an alternative title for the references

For any of the above mentioned references, you can provide an alternative title while cross referencing by adding the title before the label as shown in this example:

```
{ref}`Chapter on Open Research<rr-open>`
```

here we are giving an alternative title to the 'Open Research chapter', which will appear in your file like this: {ref}`Chapter on Open Research <rr-open>`
