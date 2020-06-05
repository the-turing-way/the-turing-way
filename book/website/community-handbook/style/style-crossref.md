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
