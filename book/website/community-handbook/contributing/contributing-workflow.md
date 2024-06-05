(ch-contributing-workflow)=
# Contribution Workflow

Whether you are writing new content or reviewing existing content, contributing to _The Turing Way_ generally encompasses the steps discussed in this section.
You may refer to the recommendations here to ensure that you have adequately prepared your contribution for review.
Please note that the order of these recommendations is not strict and we encourage you to follow the approach that suits you best.

(ch-contributing-workflow-template)=
## Select a template

Once you have decided on the type of content you want to contribute to _The Turing Way_, use the relevant [template](https://github.com/the-turing-way/the-turing-way/tree/main/book/templates) to prepare your contribution.

```{note}
Please note that we welcome new template contributions.
If the chapter or case study templates do not suit your needs, please open a Pull Request with suggestions for improving them.
If you want to contribute content for which there is no corresponding template, you are also encouraged to create the missing template and add it to the template collection.
```

(ch-contributing-workflow-location)=
## Place new files and folders in appropriate locations

_The Turing Way_'s Github repository follows an overall file structure where Guides are folders and chapters are sub-folders within them.
Similarly, case studies are located inside a `case-studies` sub-folder within the Guide folders.
All folders are located inside the [`book/website`](https://github.com/the-turing-way/the-turing-way/tree/main/book/website) directory.

When writing new content, ensure that the new files and folders you create are placed appropriately to preserve _The Turing Way's_ file structure.

For example, the [Version Control](https://book.the-turing-way.org/reproducible-research/vcs.html) chapter in the Guide for Reproducible Research is placed as follows:

````{admonition} Adding new files and folders
:class: dropdown
```
book\website
│
└───reproducible-research <---- (folder for the Guide to Reproducible Research)
│   │   reproducible-research.md <---- (Guide's landing page)
│   │   vcs.md <---- (landing page for the Version Control chapter)
|   |   new-chapter <---- (landing page for a new chapter)
│   │
│   └───vcs (chapter folder)
│   |   │   vcs-workflow.md
|   |   |   vcs-git.md
|   |   |   vcs-git-commit.md
|   |   |   ...
|   |   |   vcs-personal-stories.md
│   |   │   vcs-checklist.md
│   |   │   vcs-resources.md
│   |
|   |
|   └───new-chapter (new chapter folder)
|   |   |   ...
|    
└───project-design <---- (folder for the Guide for Project Design)
    │   project-design.md
    │   ...
```
````

New chapters in the Guide for Reproducible Research should be added like `new-chapter` in the example above.

(ch-contributing-workflow-naming)=
## Name files/folders appropriately

Please follow _The Turing Way's_ conventions for naming files.
With proper file names, other contributors can easily identify the purpose and location of your files and add to or improve them if necessary.

(ch-contributing-workflow-guidelines)=
## Follow the style and consistency guidelines

As you write your chapter, keep _The Turing Way's_ [style](https://book.the-turing-way.org/community-handbook/style.html) and [consistency](https://book.the-turing-way.org/community-handbook/consistency.html) recommendations in mind.
This ensures that your new content is accessible, and fits the overall style, structure, and formatting of the book.

(ch-contributing-workflow-toc)=
## Add your new files to the book's table of contents

The book-wide table of contents lives in the `_toc.yml` [file](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/_toc.yml).
This file structures _The Turing Way_ and defines the order in which chapters appear.
Your chapter's files should be added to the `_toc.yml` as appropriate.

For example, because the [Statistical Methods Manuscript](https://book.the-turing-way.org/reproducible-research/case-studies/statistical-methods-manuscript.html) case study belongs to the Guide for Reproducible Research, it was added to the table of contents as follows:

````{admonition} Updating the book-wide table of contents
:class: dropdown
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

````

(ch-contributing-workflow-referencing)=
## Reference external sources appropriately

Ensure external sources are properly referenced and included in _The Turing Way's_ centralised BibTeX file as recommended in the [style guide](https://book.the-turing-way.org/community-handbook/style/style-citing.html).

(ch-contributing-workflow-glossary)=
## Update the book-wide glossary

_The Turing Way_ maintains a book-wide glossary located in its [Afterword](https://book.the-turing-way.org/afterword/glossary.html).
When writing your chapter, [update the book-wide glossary](https://book.the-turing-way.org/community-handbook/style/style-more-styling.html) with the key terms in your chapter that readers should remember.

(ch-contributing-workflow-crosschecking)=
## Cross check your Pull Request

The content of the templates are only meant to guide and structure your writing.
Please remove all of the template's placeholders, tips, and suggestions from your chapter before you submit your PR for review.
