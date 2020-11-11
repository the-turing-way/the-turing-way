# Welcome

Thank you for deciding to write a case study for _The Turing Way_ book!

To standardise the book's content and maintain consistency throughout, we have created this case study template to guide you as you write your case study.

## Before You Begin

_The Turing Way_ is made up of Guides which span several chapters.
For every Guide, there is a `Case Studies` chapter that contains a collection of case studies that all explore how key concepts from the Guide relate to specific subjects (such as a project, person, organisation, or phenomenon).

Structurally, a Guide in _The Turing Way_ Github repository is a folder and your case study is a file in the `case-studies` sub-folder within it.
All Guides in _The Turing Way_ live in the `book/website` directory.

For example, if your case study belonged to Guide 1, then the file structure could resemble the following:

```
book/website
│
└───Guide 1
│   │   Guide 1's Landing Page.md
|   |   Chapter 1 Landing Page.md
│   │   Case Study Chapter Landing Page.md
│   │
│   └───Case Study Chapter
│       │   Case Study 1.md
|       |   Case Study 2.md
|       |   YOUR CASE STUDY 1.md
|       |   ...
│   
└───Guide 2
    │   Guide 2's Landing page.md
    │   ...
```

This case study template will guide you in writing the content for your case study.
We encourage you to use it to structure and format your content.

## Remember to..

### Name files/folders appropriately

Please follow _The Turing Way's_ conventions for naming files. 
This ensures that your chapter's files are named in a way that allows other people to easily identify their purpose.
Other contributors will also find it easier to add to or improve your work.


### Add your new files to the book's table of contents

The book-wide table of contents lives in the `_toc.yml` [file](book\website\_toc.yml).
This file structures _The Turing Way_ and defines the order in which chapters appear.
Your chapter's files should be added to the `_toc.yml` as appropriate.

To add the chapter on Open Science to Guide 1 in the table of contents, you could do the following:

```
- file: path/to/Guide 1
  sections:
  - title: Case Studies
    file: reproducible-research/case-studies
    sections:
    - title: A Statistical Methods Manuscript
      file: reproducible-research/case-studies/statistical-methods-manuscript
```

### Reference external sources appropriately

Ensure external sources are properly referenced and included in _The Turing Way's_ centralised bibtex file as recommended in the [style guide](https://deploy-preview-1459--the-turing-way.netlify.app/community-handbook/style/style-citing.html#ch-style-citing)

### Update the book-wide glossary

_The Turing Way_ maintains a book-wide glossary located in its [Afterword](https://the-turing-way.netlify.app/afterword/glossary.html).
When writing your chapter, update the book-wide glossary with the key terms in your chapter that readers should remember.
For each term, cross-reference to the subchapter/section where you explained it.


### Cross check your PR

The content of the templates are meant to guide and structure your writing.
Please remove all of the template's placeholders, tips, and suggestions from your chapter before you submit your PR for review.

### Follow the style and consistency guidelines

As you write your chapter, keep _The Turing Way's_ [style](https://the-turing-way.netlify.app/community-handbook/style.html) and [consistency](https://the-turing-way.netlify.app/community-handbook/consistency.html) recommendations in mind.
This ensures that your new content is accessible, and fits the overall style, structure, and formatting of _The Turing Way_ book.

Happy Writing!

