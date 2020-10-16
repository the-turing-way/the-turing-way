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

## Style for including image in a chapter:

All our chapters are written in markdown files.
Therefore, using Markdown syntax to include an image in a Markdown file will work fine, for example, `![](../../figures/file-collection.jpg)`, where the relative path of the image is provided inside the round brackets '()'.

However, this formatting does not allow images to be responsive to screen sizes, making them inaccessible to read on small screens and smartphones.
Furthermore, this doesn't allow authors to resize images in their chapters or cross reference them somewhere else in the book.

Therefore, our recommendation is to use Markedly Structured Tex (MyST) format available in the current version of Jupyterbook.

You can resize figures using the parameters: "height" (takes value in px, for example, 400px) or "scale" (takes value in percentage, for example, 50%), especially if your original image is large.
Using the parameter" "name", you can reference figures in other chapters in a similar manner as defined in {ref}`ch-style-crossref`.

All the components of your figure (image location, size and name) can be encapsulated in section within a markdown file using the following directive:

````
```{figure} ../../figures/file-collection.jpg
---
height: 500px
name: file-collection
---
```
````

This figure can be referred in other files using the {ref} role like:

```
{ref}`file-collection`
```

## Title:

Titles should be short and concise and hold a reference to the source where they are taken from.
For example, we can write the title "*_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300*" below the image.

## Alternative text:

Alternative text or Alt text are used for describing the appearance and function of an image on an HTML page.
For example, the above image can be explained by: "Two people happily browsing files in a drawer of documents."

Adding alternative text to images is one of the first principles of web accessibility.
Screen reader software can read an alt text to better explain the content with images to its users.

All the components of your figure (image location, size, name, alt text and title) can be encapsulated in section within a markdown file using the following directive:

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

Another advantage of using alt text is when an image file cannot be loaded in a browser, or the link to the image breaks, it is displayed in place of an image like shown below:

````
```{figure} ../figures/file-collection.jpg
---
height: 500px
name: file-collection
alt: Two people happily browsing files in a drawer of documents.
---
_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300.
```
````

When all these components are used correctly, figures included in a file will be rendered in the online book like in this page:

```{figure} ../../figures/file-collection.jpg
---
height: 500px
name: file-collection
alt: Two people happily browsing files in a drawer of documents.
---
_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300.
```

For more advanced parameters, please see the [JupyterBook Documentation](https://jupyterbook.org/content/figures.html).
