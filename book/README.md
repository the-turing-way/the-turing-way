## The Turing Way Book

This is the README file for _The Turing Way_ book hosted online at https://the-turing-way.netlify.app/.
For the README file of the main repository please [follow this link](https://github.com/alan-turing-institute/the-turing-way/blob/master/README.md).

All the text for each chapter of the `book` lives inside the folder `./content` directory.
All figures associated to the chapters are stored in and linked from the `./content/figures` directory.
Everything else is in the `website/` directory.

### Configuration

- The table of contents (TOC) defines the order of chapters as they appear in the book.
To change the TOC, please edit the `website/data/_toc.yml` file with correct information on filenames and their relative locations in this repository. 
Documentation on controlling the TOC structure can be found on the [jupyter book website](https://jupyterbook.org/customize/toc.html).
- Same applies for more general configuration using `website/_config.yml`. 
Documentation on configuring book settings can be found on the [jupyter book website](https://jupyterbook.org/customize/config.html).

### Deploying

The site is built automatically using these two directories. All of the requirements are specificied in `website/requirements.txt`.

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

#### Installing Dependencies in  a  virtual environment

Virtual environments are a great way of isolating project-related dependencies from you system-level python installation.
For more details on virtual environments in python see
[here](https://docs.python.org/3/tutorial/venv.html).
To use a virtual environment for building the book project, use

```
cd book/website
virtualenv the-turing-way
source the-turing-way/bin/activate
pip install -r requirements.txt
```

In case you want to use a specific python interpreter, specify the path as
```
virtualenv -p /usr/bin/python3.7 the-turing-way
```

Now you can use the `jupyter-book build .` command inside `book/website` directory as explained above.

#### On Netlify

_The Turing Way_ book is built and deployed online using [Netlify](https://www.netlify.com/).

If you want to deploy the book on Netlify, you'll just need the following settings:

- Base directory: `book/website`
- Build command: `pip install -r requirements.txt && jupyter-book build .`
- Publish directory: `book/website/_build/html`

Netlify is smart and will find your requirements.txt to do the install for you. :slightly_smiling_face: 

You can find the build history or logs for _The Turing Way_ at https://app.netlify.com/sites/the-turing-way/deploys.

## Content Templates

Templates for different types of content can be created in the `templates` directory.

Templates include:
* `case-study-template.ipynb` a template for including interactive case studies in the book

The template can be copied to create content relevant to a chapter in the `content` directory.
