(ch-content)=
# Writing Content

As _The Turing Way_ project grows and evolves, we actively welcome and encourage continuous contributions from community members in the form of new chapters and case studies. 
However, these new contributions need to be consistent with the overall theme, purpose, format, and style of the book's existing content.

Since _The Turing Way_ is written asynchronously by multiple authors around the world, we have created several templates to guide future content contributions in order to preserve the book's consistency as it grows.

This chapter provides a brief overview of these templates. 
You can find each one in the `template` [directory](https://github.com/alan-turing-institute/the-turing-way/tree/master/book/templates) of the _The Turing Way's_ Github repository and we encourage you to use them if you wish to contribute to content to _The Turing Way_. 
Also, ensure that you read our [Contributor Guidelines](https://github.com/alan-turing-institute/the-turing-way/blob/master/CONTRIBUTING.md) in addition to our [style](https://the-turing-way.netlify.app/community-handbook/style.html) and [consistency](https://the-turing-way.netlify.app/community-handbook/consistency.html) recommendations before you write.

(ch-content-structure)=
## Book Structure

_The Turing Way_ is made up of Guides which span several chapters.
This means that when your content is added to the book, it will belong to one of these Guides.
Structurally, all Guides in _The Turing Way_ Github repository are folders and live within the `book/website` directory. 
Depending on the type of content you wish to contribute, the files you create should be added as recommended below:

### Case Studies

For every Guide, there is a `Case Studies` chapter that contains a collection of case studies that explore how key concepts from the Guide relate to specific subjects (such as a project, person, organisation, or phenomenon).

Case study files are located in the `case-studies` sub-folder within each Guide.

For example, the case study about the [Statistical Methods Manuscript](https://the-turing-way.netlify.app/reproducible-research/case-studies/statistical-methods-manuscript.html) in the Guide for Reproducible Research follows this file structure:

```
book/website
│
└───reproducible-research <---- (Folder for the Guide to Reproducible Research)
│   │
│   └───binderhub
│   │
│   └───case-studies <---- (folder containing subchapter for case studies the Guide to Reproducible Research)
│   |   │   statistical-methods-manuscript.md <---- (Statistical Manuscripts Case Study)
|   |   |   example-case-study.md
|   |   |   ...
|   |
|   |   ...
|   |   case-studies.md <---- (Landing page for Case Studies chapter)
|   |   ...
│   
└───project-design <---- (Folder for the Guide for Project Design)
    │   project-design.md
    │   ...
```

More case studies (such as `example-case-study-file.md`) for the Guide for Reproducible Research can be added in the same location as `statistical-methods-manuscript.md`.

### Chapters

Chapters are sub-folders within Guides.

For example, the [Version Control](https://the-turing-way.netlify.app/reproducible-research/vcs.html) chapter in the Guide for Reproducible Research has the following structure:

```
book\website
│
└───reproducible-research <---- (folder for the Guide to Reproducible Research)
│   │   reproducible-research.md ---- (Guide's Landing Page)
│   │   vcs.md <---- (Landing page for the Version Control chapter)
│   │   example-chapter.md (landing page for a new chapter)
|   |
│   └───vcs (chapter folder)
│   |   │   vcs-workflow.md
|   |   |   vcs-git.md
|   |   |   vcs-git-commit.md
|   |   |   ...
|   |   |   vcs-personal-stories.md
│   |   │   vcs-checklist.md
│   |   │   vcs-resources.md
|   └───example-chapter (new chapter folder)
│       │   example-subchapter.md
|       |   ...
|       |   example-personal-stories.md
│       │   example-checklist.md
│       │   example-resources.md
│   
└───project-design <---- (folder for the Guide for Project Design) 
    │   project-design.md
    │   ...
```

To add more chapters to the Guide for Reproducible Research, 
use the file locations of `example-chapter`'s constituent files for reference.

(ch-content-checklist)=
## Writing Checklist

### Follow the style and consistency guidelines

As you write your chapter, keep _The Turing Way's_ [style](https://the-turing-way.netlify.app/community-handbook/style.html) and [consistency](https://the-turing-way.netlify.app/community-handbook/consistency.html) recommendations in mind.
This ensures that your new content is accessible, and fits the overall style, structure, and formatting of the book.

### Name files/folders appropriately

Please follow _The Turing Way's_ conventions for naming files.
With proper file names, other contributors can easily identify the purpose of your files and add to or improve them if necessary. 


### Add your new files to the book's table of contents

The book-wide table of contents lives in the `_toc.yml` [file](https://github.com/alan-turing-institute/the-turing-way/blob/master/book/website/_toc.yml).
This file structures _The Turing Way_ and defines the order in which chapters appear.
Your chapter's files should be added to the `_toc.yml` as appropriate.

For example, because the [Statistical Methods Manuscript](https://the-turing-way.netlify.app/reproducible-research/case-studies/statistical-methods-manuscript.html) case study was written for the Guide for Reproducible Research, it was added to the table of contents as follows:


```
- file: reproducible-research/reproducible-research
  sections:
  ...
  - title: Case Studies
    file: reproducible-research/case-studies
    sections:
    - title: A Statistical Methods Manuscript
      file: reproducible-research/case-studies/statistical-methods-manuscript
```

### Reference external sources appropriately

Ensure external sources are properly referenced and included in _The Turing Way's_ centralised bibtex file as recommended in the [style guide](https://the-turing-way.netlify.app/community-handbook/style/style-citing.html)

### Update the book-wide glossary

_The Turing Way_ maintains a book-wide glossary located in its [Afterword](https://the-turing-way.netlify.app/afterword/glossary.html).
When writing your chapter, [update the book-wide glossary](https://the-turing-way.netlify.app/community-handbook/style/style-more-styling.html) with the key terms in your chapter that readers should remember.



### Cross check your PR

The content of the templates are meant to guide and structure your writing.
Please remove all of the template's placeholders, tips, and suggestions from your chapter before you submit your PR for review.

Happy Writing!
