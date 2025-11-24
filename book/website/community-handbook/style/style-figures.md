(ch-style-figures)=
# Using figures in _The Turing Way_

We encourage you to use images in _The Turing Way_ book chapters to help readers understand the concepts discussed in the chapter better.
This section of the style guide will explain how to use [MyST Markdown](xref:myst-guide) to add them to the book with appropriate {ref}`alt text<ch-style-figures-alttext>` and {ref}`captions<ch-style-figures-caption>`.
This is sometimes tricky, refer to the {ref}`ch-style-figures-advanced` section for troubleshooting.

We are very passionate about ensuring that the creators of the original image files (including you!) are {ref}`acknowledged appropriately<ch-style-figures-licence>`.
Please do not use images that are not licenced for reuse.

In this sub-chapter we have used the term **figure** to refer to an illustration that conveys information in the context of _The Turing Way_ chapters.
The term **image** is used to refer to the file object itself.

(ch-style-figures-licence)=
## Open licence

Please ensure that you attribute the image files fairly and avoid files that are either restricted from reuse or lack reproduction permissions.

The following recommendations will help you to check that you're using the images according to their licence permissions:

* You can source images in the public domain ([CC0 licence](https://creativecommons.org/share-your-work/public-domain/cc0)) or images shared under an appropriate permissive license.
  Images that are available under CC-BY 4.0 permissions are very easily interoperable with _The Turing Way_ as this is the same licence as the rest of the content for the book.
* If you are using your own images, they will be made available under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.ast) licence as with the rest of the book.
* If an image (for example that you have found on the internet) is not available under an open licence please contact the original author of the image and seek permission to reproduce their image.
  Make sure to ask them **how they would like to be credited** in the caption for the figure.

In general, make sure to always cite the image properly as directed by the image owners.
"Image from the internet" is not enough.

(ch-style-figures-image)=
## Image location, type, size and file name

Every image file used in this book should be located in the directory `book/website/figures` of our [GitHub Repository](https://github.com/the-turing-way/the-turing-way/tree/main/book/figures).
If you use a new image file, please add the file in the `figures` directory by either uploading via GitHub, or adding locally and pushing the change online when using git.

Please upload `.jpg`, `.png`, or `.svg` files that are under 1MB to allow them to load faster in the online book.
If your file is larger than 1MB, please use a local image editing tool, or online tool like [IMG2GO](https://www.img2go.com/compress-image) to compress your file.

To name your image file, please use all-lowercase and separate words with hyphens (-).

(ch-style-figures-alttext)=
## Alternative text

Alternative text or alt text are used for describing the appearance and function of an image on an HTML page for users who cannot see it. 
Alt text is often used by visually impaired people who use assistive technology such as screen readers.
Adding alt texts to figures is one of the first principles of web accessibility as it enables the screen reader software to read an alt text to its users helping them understand/explain the content.

If an image link breaks, alt texts are still functional and read as intended by the assistive technology.

For more, visit the {ref}`Alt text section<ch-accessibility-alttext>`

**Please note that a height of 500px works very well with _The Turing Way_ book, but this is only a suggestion.**

(ch-style-figures-caption)=
## Caption

Captions appear below the figure.
They should be short and concise and include a reference to the source where they are taken from.
In particular it is important to describe the licence under which the image is re-used.

For example, a caption might say:

> Making your first pull request on GitHub.  
> _The Turing Way_ project illustration by Scriberia.  
> Used under a CC-BY 4.0 licence.  
> DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).

The syntax for this image is as follows, and the way it appears in the book is below the code snippet.

````markdown
```{figure} ../../../figures/first-pull-request.*
---
height: 400px
label: first-pull-request
alt: >
  Cartoon-like sketch of two persons sitting across from each other working on their laptops.
  A straight arrow on the top indicates the main branch of the repository that they are working on,
  a pull request is shown by a branch coming out of the main arrow labelled as Clone,
  followed by a Pull Request with the changes that the first person made in the branch,
  and the final step labelled as Approved that indicates approval of the changes by the second person.
  This arrow then merges back to the main arrow/repository.
---
Making your first pull request on GitHub.
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).

```{figure} ../../../figures/first-pull-request.*
---
height: 400px
label: first-pull-request
alt: >
  Cartoon-like sketch of two persons sitting across from each other working on their laptops.
  A straight arrow on the top indicates the main branch of the repository that they are working on,
  a pull request is shown by a branch coming out of the main arrow labelled as Clone,
  followed by a Pull Request with the changes that the first person made in the branch,
  and the final step labelled as Approved that indicates approval of the changes by the second person.
  This arrow then merges back to the main arrow/repository.
---
Making your first pull request on GitHub.
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

(ch-style-figures-cross-referencing)=
## Cross-Referencing Figures in Other Chapters

After a figure is added in a chapter, it can be referenced using its label.
For example, we can reference the figure above like `[](#first-pull-request)`, which renders as [](#first-pull-request).

(ch-style-figures-embedding)=
## Embedding Figures from Other Chapters

In addition to cross-referencing, you can also **embed** a figure that already exists elsewhere in the book.  
Embedding allows you to reuse a figure — including its caption — without duplicating the image file or rewriting its code.

The `{embed}` directive pulls content (like figures, tables, or sections) directly from another Markdown file.  
If the original figure changes, all embedded copies update automatically.

Here’s an example of embedding a figure from another page:

```{embed} ../../community-handbook/acknowledging-contributors.md#theturingway-acknowledgement
:align: center
:width: 100%
```

In this example:
- `../../community-handbook/acknowledging-contributors.md` is the **relative path** to the file containing the original figure.
- `#theturingway-acknowledgement` is the **label** of that figure (defined in the original chapter).
- Optional fields such as `:align:` and `:width:` adjust the display on the page.

Embedding is especially helpful when the same figure is used across multiple chapters — for example, when a single illustration appears in both the *Community Handbook* and *Style Guide*.

> 💡 For more details on the `{embed}` directive, see the [MyST documentation](https://mystmd.org/guide/embed#docs-embed).

(ch-style-figures-advanced)=
## Advanced features and "gotchas"

For more advanced parameters, please visit the [MyST Markdown documentation](xref:myst-guide/figures).
That page includes information on how to scale and align the figures.

We've noticed a couple of "gotchas" from contributors to _The Turing Way_ and we'll try to keep this section of the guide up to date for anyone else learning the MyST syntax for figures.

* If things do not work, looking at the **deploy log** (visible at the beginning of your PR) might well give you hints about what the issues are.
* Figure paths are case-sensitive, make sure the name of the file is all lowercase.
* `label:` (or `name:`) is for including in reference links, it cannot have spaces.
* The path to the figure will depend on the position of the .md file in the repo (one or two folders away from `website` will give `../` or `../../` respectively).
* You can choose to include the file extension with your path, or you can use the format `path/filename.*` to allow Jupyter Book to decide which file to use in the case that multiple filetypes with the same name exist. Jupyter Book will [choose the one most appropriate to the intended output](https://jupyterbook.org/en/stable/content/figures.html#supported-image-formats). This is useful as it means that filetypes can be changed without breaking the pages that use those files.
* You cannot have line breaks in the alt text, but you can have it in the caption.
* Both `:` and `"` have syntactic meaning for Sphinx.
  That means it is important that you do not use these characters in your alt text.
```
