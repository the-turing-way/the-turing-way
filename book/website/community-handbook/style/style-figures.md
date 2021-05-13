(ch-style-figures)=
# Using figures in _The Turing Way_

You are welcome to add relevant figures in the book chapters, however, please ensure that you attribute the image files fairly and avoid files that are either restricted from reuse or lack reproduction permissions.

To ensure that, please follow these simple recommendations:

- Please use public domain images or images licensed through appropriate Creative Commons terms and preferably [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.ast) (CC BY 4.0) license same as this book.
- If the image (on the internet), is not available under CC-By license, contact the original author of the image and seek permission to reproduce their image.
- If you are using your images, they will be by-default included in this book under CC-BY 4.0 License.
- Cite the image properly as directed by the image owners, “Image from the internet” is not enough.

*Please note that we have used the term 'figure' to refer to an illustration that conveys information in the context of _The Turing Way_ chapters and the term 'image' is used to refer to the file object.*

## Image type, file size and location:

Please upload .jpg or .png files that are under 1MB to allow them to load faster in the online book.
If your file is larger than 1MB, please use a local image editing tools, or online tool like [IMG2GO](https://www.img2go.com/compress-image) to compress your file.

Every image file used in this book should be located in the file `_figure-list.md` in the directory `book/website/figures` of our [GitHub Repository](https://github.com/alan-turing-institute/the-turing-way/tree/master/book/website/figures).
If you use a new image file, please add the file in the `figures` directory, and add details in the `_figure-list.md`.

## Style for including figures in a chapter:

All our chapters are written in markdown files.
Therefore, using Markdown syntax to include a figure in a Markdown file will work fine, for example, `![](../../figures/file-collection.jpg)`, where the relative path of the image file is provided inside the round brackets '()'.

However, this formatting does not allow images to be responsive to screen sizes, making them inaccessible to read on small screens and smartphones.
Furthermore, this doesn't allow authors to resize figures in their chapters or cross reference them somewhere else in the book.

Therefore, our recommendation is to use Markedly Structured Tex (MyST) format available in the current version of Jupyter Book.

You can resize figures to adjust how they appear in our chapters using the parameters: `width` and `height` (takes value in px, for example, 400px) or `scale` (takes value in percentage, for example, 50%), especially if your original figure is large.
Using the parameter: `name`, you can reference figures in other chapters in a similar manner as defined in {ref}`ch-style-crossref`.

All the components of your figure (figures location, size and name) can be encapsulated in section within a markdown file using the following directive:

````
```{figure} ../../figures/file-collection.jpg
---
width: 500px
name: file-collection
---
```
````

This figure can be referred in other files using the {ref} role like:

```
{ref}`file-collection`
```

Please note that width of 500px works very well with _The Turing Way_ book, but this is only a suggestion.

## Title:

Titles should be short and concise and hold a reference to the source where they are taken from.
For example, we can write the title *_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300* below the figure.

## Alternative text:

Alternative text or Alt text are used for describing the appearance and function of an image on an HTML page.
Our example figure can be explained with this sentence: *Two people happily browsing files in a drawer of documents.*

Adding alternative text to figure is one of the first principles of web accessibility.
Screen reader software can read an alt text to better explain the content of the figure to its users.

All the components of your figure (image file location, size, name, alt text and title) can be encapsulated in section within a markdown file using the following directive:

````
```{figure} ../../figures/file-collection.jpg
---
height: 500px
name: file-collection
alt: Two people happily browsing files in a drawer of documents.
---
_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300.
```
````

Another advantage of using alt text is when an image cannot be loaded in a browser, or the link to the image breaks, it is displayed in place of an figure like shown below:

```{figure} ../../figures/alt-text-demo.png
---
name: file-broken-link
alt: Two people happily browsing files in a drawer of documents.
---
_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300.
```

When all these components are used correctly, a figure included in a file will be rendered in the online book like in this page:

```{figure} ../../figures/file-collection.jpg
---
height: 500px
name: file-collection
alt: Two people happily browsing files in a drawer of documents.
---
_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300.
```

For more advanced parameters, please see the [Jupyter Book Documentation](https://jupyterbook.org/content/figures.html).
