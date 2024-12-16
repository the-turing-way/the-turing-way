## The Turing Way Book

This is the README file for _The Turing Way_ book hosted online at https://book.the-turing-way.org/.
For the README file of the main repository please [follow this link](https://github.com/the-turing-way/the-turing-way/blob/main/README.md).

All the text for each chapter of the `book` lives inside the folder `./website` directory.
All figures associated to the chapters are stored in and linked from the `./website/figures` directory.
Everything else is in the `website/` directory.

### Configuration

- The table of contents (TOC) defines the order of chapters as they appear in the book.
To change the TOC, please edit the `website/_toc.yml` file with correct information on filenames and their relative locations in this repository.
Documentation on controlling the TOC structure can be found on the [Jupyter Book website](https://jupyterbook.org/customize/toc.html).
- Same applies for more general configuration using `website/_config.yml`.
Documentation on configuring book settings can be found on the [Jupyter Book website](https://jupyterbook.org/customize/config.html).

### Deploying

The site is built automatically using these two directories. All of the requirements are specified in `website/requirements.txt`.

Instructions for how to build a Turing Way book locally can be found in [_The Turing Way_'s Community Handbook](https://book.the-turing-way.org/community-handbook/local-build).

#### On Netlify

_The Turing Way_ book is built and deployed online using [Netlify](https://www.netlify.com/).

If you want to deploy the book on Netlify, you'll need the following settings:

- Base directory: `book/website`
- Build command: `pip install -r requirements.txt && jupyter-book build .`
- Publish directory: `book/website/_build/html`

Netlify is smart and will find your requirements.txt to do the install for you. :slightly_smiling_face:

You can find the build history or logs for _The Turing Way_ at https://app.netlify.com/sites/the-turing-way/deploys.

## Bibliography

In the directory `./website/_bibliography` a collection of bibliography from all the chapters exist in the `references.bib` file.
More details can be read in the [CONTRIBUTING.md](https://github.com/the-turing-way/the-turing-way/blob/main/CONTRIBUTING.md#referencing-and-citing) file.

## Content Templates

Templates for different types of content can be created in the [`templates` directory](./templates).

As of now, the template directory includes the following:
* `case-study-template`: a template for writing and/or revising case studies
* `chapter-template`: a template for writing new chapters or revising old ones

The template can be copied to create content relevant to a chapter in the `content` directory.
