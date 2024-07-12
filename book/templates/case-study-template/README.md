# Welcome

Thank you for contributing to _The Turing Way_ book by writing a case study!

_The Turing Way_ chapters are co-authored by people from different research backgrounds and domain expertise.
 We do not aim to create domain-specific resources but provide a central collection of best practices, tools and recommendations in data science that are transferable across different disciplines.
 Nevertheless, we recognise that to allow readers to gain an in-depth understanding of new topics we need to provide some examples and case studies that they can identify with.
Therefore, community-contributed case studies are highly beneficial for our community members who would like to see some relatable examples where these skills are applied.

To standardise the book's content and maintain consistency throughout, we have created this template to guide you as you write your case study.

## Before You Begin

_The Turing Way_ is made up of Guides which span several chapters.
For every Guide, there is a `Case Studies` chapter that contains a collection of case studies that explore how key concepts from the Guide relate to specific subjects (such as a project, person, organisation, or phenomenon).

Structurally, a Guide in _The Turing Way_ Github repository is a folder and your case study is a file in the `case-studies` sub-folder within it.
All Guides in _The Turing Way_ live in the `book/website` directory.

For example, if you wrote the case study about the [Statistical Methods Manuscript](https://book.the-turing-way.org/reproducible-research/case-studies/statistical-methods-manuscript.html) in the Guide for Reproducible Research, then the file structure could resemble the following:

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
This case study template will guide you in writing the content for your case study.
We encourage you to use it to structure and format your content.

## Remember to..

### Follow the style and consistency guidelines

As you write your chapter, keep _The Turing Way's_ [style](https://book.the-turing-way.org/community-handbook/style.html) and [consistency](https://book.the-turing-way.org/community-handbook/consistency.html) recommendations in mind.
This ensures that your new content is accessible, and fits the overall style, structure, and formatting of _The Turing Way_ book.

### Name files/folders appropriately

Please follow _The Turing Way's_ conventions for naming files.
With proper file names, other contributors can easily identify the purpose of your files and add to or improve them if necessary. 


### Add your new files to the book's table of contents

The book-wide table of contents lives in the `_toc.yml` [file](book/website/_toc.yml).
This file structures _The Turing Way_ and defines the order in which chapters appear.
Your chapter's files should be added to the `_toc.yml` as appropriate.

For example, because the [Statistical Methods Manuscript](https://book.the-turing-way.org/reproducible-research/case-studies/statistical-methods-manuscript.html) case study was written for the Guide for Reproducible Research, it was added to the table of contents as follows:


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

Ensure external sources are properly referenced and included in _The Turing Way's_ centralised bibtex file as recommended in the [style guide](https://deploy-preview-1459--book.the-turing-way.org/community-handbook/style/style-citing.html#ch-style-citing)

### Update the book-wide glossary

_The Turing Way_ maintains a book-wide glossary located in its [Afterword](https://book.the-turing-way.org/afterword/glossary.html).
When writing your chapter, update the book-wide glossary with the key terms in your chapter that readers should remember.
For each term, cross-reference to the subchapter/section where you explained it.


### Cross check your PR

The content of the templates are meant to guide and structure your writing.
Please remove all of the template's placeholders, tips, and suggestions from your chapter before you submit your PR for review.

Happy Writing!
