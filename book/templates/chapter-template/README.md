# Welcome

Well done on taking the first steps towards writing a chapter for _The Turing Way_  book!

In order to standardise the book's content and maintain consistency throughout, we have created this template to guide you as you write the content for your chapter.

## Before You Begin

_The Turing Way_ book is made up of Guides which span several chapters.
This means that when your chapter is added to the book, it will belong to one of its Guides.

Structurally, a Guide in _The Turing Way_ Github repository is a folder and your chapter is a sub-folder within it.
All Guides in _The Turing Way_ live in the `book/website` directory.

If your chapter belonged to Guide 1, for example, then the file structure could resemble the following:

```
book\website
│
└───Guide 1
│   │   Guide 1's Landing Page.md
│   │   Your Chapter's Landing Page.md
│   │
│   └───Your Chapter
│       │   Your Chapter's Topic (1).md
|       |   Your Chapter's Topic (2).md
|       |   Your Chapter's Topic (3).md
|       |   ...
│       │   Your Chapter Checklist.md
│       │   Your Chapter Resources.md
│   
└───Guide 2
    │   Guide 2's Landing page.md
    │   ...
```

This new chapter template will guide you in creating content for all the files your chapter should contain.
Below, we explain what each file is and where they are located. 
We encourage you to use them to structure your content.

### `chapter-landing-page.md`:

At the top-level of the `chapter-template` folder, you will find the [`chapter-landing-page.md`](templates\chapter-template\chapter-landing-page.md) file where you can write content for your chapter's landing page.

The landing page is where your chapter begins, and where you should introduce and summarise the rest of your chapter's content.
The landing page should also inform readers why the chapter may be useful to them and what prior knowledge they should have to understand the chapter better.

When adding your chapter to _The Turing Way_ book, your landing page should live directly in the folder named after the Guide your chapter belongs to.

### `chapter-content.md`:

Inside the `chapter-content` folder, you will find the [`chapter-content.md`](templates\chapter-template\chapter-content\chapter-content.md) file where you can write about the individual topics that make up your chapter.
This can be referred to as subchapters.

For example, if you were writing a chapter on [Open Science](https://en.wikipedia.org/wiki/Open_science) with a focus on its different interpretations, this file is where you would individually write about the various schools of thought in Open Science (one of which could be The Infrastructure School of Thought, for example).
Feel free to make as many copies of this file as necessary.

This file should be included in the sub-folder named after your chapter.

### `chapter-checklist.md`:

You will find the [`chapter-checklist.md`](templates\chapter-template\chapter-content\chapter-checklist.md) file in the `chapter-content` folder.
This file should contain action points you want your readers to take based on the chapter's content.
Ideally, these action points should reinforce the key concepts of your chapter in a practical way.

Add this file to your chapter's sub-folder as well.

### `chapter-resources.md`:

This [file](templates\chapter-template\chapter-content\chapter-resources.md) can be found in the `chapter-content` folder.
Use `chapter-resources.md` to tell readers what topics to explore next and where to find more information about the concepts covered in your chapter.

`chapter-resources.md` should also be located in the sub-folder named after your chapter.

## Remember to..

### Name files/folders appropriately

Please follow _The Turing Way's_ conventions for naming files. 
This ensures that your chapter's files are named in a way that allows other people to easily identify their purpose.
This way, other contributors will find it easier to add to or improve your work.

- **Landing Page**: Name your landing page using a word that best describes your chapter's overarching concept.
For a chapter on Open-Science, the landing page could be named `open-science.md`.

- **Chapter Folder**: The subfolder where your chapter's content goes should have the same name as the chapter's Landing Page, for example `open-science`.

- **Chapter Content**: Every sub-topic in your chapter should have its own file.
These should be named by combining the landing page's name with a word that best describes the sub-topic.
For example, if a sub-topic of the Open Science chapter is about the Infrastructure School of Thought, then its file name could be `open-science-infrastructure.md`

- **Chapter Checklist and Resources**: Like the files that make up the chapter's content, name your chapter's Checklist and Resources files by combining the Landing Page's name with a word that best describes the file.
This could be `open-science-checklist.md` or `open-science-resources.md` for Checklist and Resources Respectively.

### Add your new files to the book's table of contents

The book-wide table of contents lives in the `_toc.yml` [file](book\website\_toc.yml).
This file structures _The Turing Way_ and defines the order in which chapters appear.
Your chapter's files should be added to the `_toc.yml` as appropriate.

To add the chapter on Open Science to Guide 1 in the table of contents, you could do the following:

```
- file: path/to/Guide 1
  sections:
  - title: Open Science
    file: path/to/open-science
    sections:
    - title: Infrastructure School of Thought
      file: path/to/open-science-infrastructure
    - title: Checklist
      file: path/to/open-science-checklist
    - title: Resources
      file: path/to/open-science-resources
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