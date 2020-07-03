# Using Figures in _The Turing Way_

You are welcome to add relevant images and illustrations in the book chapters, however, please ensure that you attribute images fairly and avoid images that are either restricted from reuse or lack reproduction permissions.

To ensure that, please follow these simple recommendations:

- Please use public domain images or images licensed through appropriate Creative Commons terms and preferably [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.ast) (CC BY 4.0) license same as this book.
- If the image (on the internet), is not available under CC-By license, contact the original author of the image and seek permission to reproduce their image.
- If you are using your images, they will be by-default included in this book under CC-BY 4.0 License.
- Cite the image properly as directed by the image owners, “Image from the internet” is not enough.

## Location of image files:

Every image used in this book is located in the file `_figure-list.md` in the directory `book/website/figures` of our [GitHub Repository](https://github.com/alan-turing-institute/the-turing-way/tree/master/book/website/figures).
If you use a new image in any chapter, please add the file in the `figures` directory, and add details in the `_figure-list.md`.

All our chapters are written in markdown files.
You can use the following Markdown syntax, where the relative path of the image is provided inside thew round brackets '()':

`![](../../figures/file-collection.jpg)`

This is rendered in an online book (this page), like below:

![](../../figures/file-collection.jpg)

## Alternative text:

Alternative text or Alt text are used for describing the appearance and function of an image on an HTML page.

Adding alternative text to images is one of the first principles of web accessibility.
Screen reader software can read an alt text that can help visually impaired users to better understand the content with images.

In Markdown, the alt text for the image can be written inside the square brackets `[]`:

```![Two folks happily looking in a drawer of documents and looking at different files.](../../figures/file-collection.jpg)```

If an image file cannot be loaded in a browser, or the link to the image breaks, alt text is displayed in place of an image like shown below:

![Two folks happily looking in a drawer of documents and looking at different files.](../figures/file-collection.jpg)

## Title:

Titles should be short and concise and hold a reference to the source where they are taken from.
For example, we can use "*_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300*" under the image as the title.

## Style for including image in a chapter:

All the components of your figure (image, alt text and title) can be encapsulated in a table within a markdown file using the following directive:

```
| ![Two folks happily looking in a drawer of documents and looking at different files.](../figures/file-collection.jpg)        |
| ------------------------------------------------------------------------------------ |
| _The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300. |
```
**When you include a figure in a chapter you are writing, please add the details in the `book/content/figures` directory.**

## Using figures that can be referenced

The current version of Jupyterbook uses Markedly Structured Tex (MyST) that allows to include figures, which can be referenced in other chapters in a similar manner as defined in {ref}`ch-style-crossref`.

There is another advantage of resizing your figures using the "height" (takes value in px, for example, 400px) or "scale" (takes value in percentage, for example, 50%) parameters, especially if your original image is large.

To include a figure, use this pattern:

````
```{figure} ../figures/file-collection.jpg
---
height: 500px
name: file-collection
alt: Two people happily looking in a drawer of documents and looking at different files.
---
_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300.
```
````

This figure can be referred in other files using the {ref} role like:

```
{ref}`file-collection`
```

For more advanced parameters, please see the [JupyterBook Documentation](https://jupyterbook.org/content/figures.html).
