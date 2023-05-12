## The Turing Way Book

This is the README file for _The Turing Way_ book hosted online at https://the-turing-way.netlify.app/.
For the README file of the main repository please [follow this link](https://github.com/alan-turing-institute/the-turing-way/blob/main/README.md).

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

#### Locally (Windows)

The following workflow should succeed using a miniconda powershell terminal on Windows 10:

1. conda install git
2. git clone https://github.com/alan-turing-institute/the-turing-way.git
3. cd quantecon-mini-example
4. git checkout windows
5. conda env create -f environment_win.yml
6. conda activate wintest
7. cd mini_book
8. runjb docs

For more information, Please refer to [Jupyter Book Documentations](https://jupyterbook.org/advanced/advanced.html#working-on-windows). 

#### Locally (Mac / Linux Only)

To install jupyter-book etc.
```
cd book/website
pip install -r requirements.txt
```

Finally, to build the book and preview your changes locally you can run the following command:
```
cd book/website
jupyter-book build .
```
Now you can open the path provided by jupyter-book as output in your terminal.

#### Clean up the recent build

When you test your edits by building the book multiple times, it is better to clean up the last build before generating a new one.
You can either manually delete the `book/website/_build` folder every time, or run this command:
```
cd book/website
jupyter-book clean .
```
More details on this process can be read on the [Jupyter Book's GitHub repository](https://github.com/executablebooks/jupyter-book/blob/master/docs/advanced/advanced.md#clean-your-books-generated-files).

#### Check external links in the book

When editing or reviewing this book locally, you can run the Sphinx link checker with Jupyter Book to check if the external links mentioned in the book are valid.
To run the link checker, use the following command:

```
cd book/website
jupyter-book build . --builder linkcheck
```

The link checker checks if the each link resolves and prints the status on your terminal so that you can check and resolve any incorrect links.
Read more about this on the [Jupyter Book's GitHub repository](https://github.com/executablebooks/jupyter-book/blob/master/docs/advanced/advanced.md#check-external-links-in-your-book).

#### Installing Dependencies in a virtual environment

Virtual environments are a great way of isolating project-related dependencies from you system-level python installation.
For more details on virtual environments in python see
[here](https://docs.python.org/3/tutorial/venv.html).
To use a virtual environment for building the book project, use

```
python3 -m venv the-turing-way
source the-turing-way/bin/activate
pip install -r book/website/requirements.txt
```

Now you can use the `jupyter-book build .` command inside `book/website` directory as explained above.

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
More details can be read in the [CONTRIBUTING.md](https://github.com/alan-turing-institute/the-turing-way/blob/main/CONTRIBUTING.md#referencing-and-citing) file.

## Content Templates

Templates for different types of content can be created in the [`templates` directory](./templates).

As of now, the template directory includes the following:
* `case-study-template`: a template for writing and/or revising case studies
* `chapter-template`: a template for writing new chapters or revising old ones

The template can be copied to create content relevant to a chapter in the `content` directory.
