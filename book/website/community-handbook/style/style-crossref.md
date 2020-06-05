### Cross-referencing within the book

We recommend using the cross-referencing style as described in the [JupyterBook](https://jupyterbook.org/content/citations.html) for chapters or files, and different contents of chapters such as sections and figures.

Labels are a way to add tags to parts of your content or a file that you can reference later on.
This is helpful because you can quickly insert labels to other parts of your book.

#### Labels in JupyterBook

To add a label for a section or a chapter/subchapter, use a syntax of the following pattern before the element you wish to label:
```
(my-label-name)=
# The thing that I want to label
```
You can insert cross-references to the labels of sections in your file with the following syntax:

```
{ref}`my-label-name`.

```

Similarly, you can use labels for cross referencing chapters or subchapters.

Please see details in the examples given below.

### _The Turing Way_ naming convention for the labels

We recommend using the following naming standard for labels, which will allow different authors and contributors of _The Turing Way_ to intuitively identify the locations of the files where these labels have been created.

The following naming convention for the labels for different chapters:

```
(sectioninitials-filename=)
```
 Here, the first placeholder `sectioninitials` should be replaced by the initials for different sections in the book and the second placeholder `filename` should be replaced by the name of file where the label is being created.

For the different sections of the book, we will use the following `sectioninitials`:

- Reproducible Research: `rr`
- Project Design: `pd`
- Collaboration: `clb`
- Contribution: `cnt`
- Ethical Research: `er`
- Community Handbook: `ch`

For example, `rr-overview` will be the label name for the `overview` chapter in the section `reproducible research`.

Similarly, for different sections we recommend extending the label name with a third placeholder for `section` which should be replaced with a short yet sensible name for the section where the label is being creates:
```
(sectioninitials-filename-section=)
```
For example, `rr-overview-definitions` will be the label name for the section `Definitions` within the `Overview` chapter in the section `Reproducible Research`.

**After a label is created, please update the information in the central table called [labels.md](../../crossref/labels.md) file located in `book/website/crossref/` directory.**

### Examples of cross-referencing

**Examples for cross-referencing sections of chapters and subchapters**

We will use examples for the chapters in "Reproducible Research" guide located in the `book/website` directory.

***Case 1***: When you cross-reference a section of the chapter within the same file *before* a label has been created.

In the subchapter "Resources" of the "Overview" chapter, we have created a label `rr-overview-resources-addmaterial` for the section "Additional Material" by using the following directive:

```
(rr-overview-resources-addmaterial)=
## Additional Material
```
We can cross-reference it in an earlier section "Further Reading" within the same file using the following:
```
{ref}`rr-overview-resources-addmaterial`
```
 This will appear in the online book like so: {ref}`rr-overview-resources-addmaterial`.

***Case 2***: When you cross-reference a section of the chapter within the same file *after* a label has been created.

In the same subchapter "Resources", we have created a label `rr-overview-resources-reading` for the section "Further Reading". 
We can cross-reference it in a later section "Additional Material" within the same file using the following:
```
{ref}`rr-overview-resources-reading`
```

***Case 3***: When you cross-reference a section of a chapter in a different file (chapter) before or after a label has been created.

In the subchapter "Definitions" of the "Overview" chapter, we have created a label
`(rr-overview-definitions)` for the section "The Turing Way definition of reproducibility". 

We can cross-reference it in a different subchapter or chapter. 
In this case, let's cross-reference it in the landing (main) page of the "Overview" chapter by using the following:

```
{ref}`rr-overview-definitions`
```

Though we are demonstrating this example for subchapters within the same chapter ("Overview"), the similar syntaxes can be used for cross-referencing in other chapters within the book.

**Examples for Cross referencing chapters and subchapters**

***Case 4***: Cross-referencing a chapter or subchapter in a different file (chapter/subchapter) before or after a label has been created.

For example, in the landing page of the chapter "Open Research", we have created a label `rr-open`. 
We can cross-reference it in the section "What to learn next?" in a different subchapter "Resources" of the "Overview" chapter by using the following:

```
{ref}`rr-open`
```

It will appear in your chapter like this: {ref}`rr-open`.

Though we are demonstrating this example for cross-referencing chapters and subchapters across the book, the same syntax can be used for cross-referencing subchapters within the same chapter.