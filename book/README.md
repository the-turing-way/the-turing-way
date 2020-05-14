## The Turing Way Book

*For the main repo (where most of the issues live) please [follow this link](https://github.com/alan-turing-institute/the-turing-way).*

All the text for each chapter lives inside its own folder in the `content/` directory.
All figures associated to the chapters are stored in and linked from the `book/content/figures/` directory.
Everything else is in the `website/` directory.

### Configuration

- The table of contents (TOC) defines the order of chapters as they appear in the book.
To change the TOC, please edit the `website/_data/toc.yml` file with correct information on file names and their relative locations in this repository. 
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
If you want to see your local changes on your own computer you'll have to 
go in the website directory, install the relevant ruby plugins, and enter 
`make serve` (type `make` on it's own to see the other options).

#### Installing Dependencies in  a  virtualenv

Virtual environments are a great way of isolating project-related dependencies
from you system-level python installation.
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
You will also need to make sure that ruby is
[installed](https://www.ruby-lang.org/en/documentation/installation/).
Finally run 
```
make install
```
You are ready to build \& preview the book.

If you want to see your local changes on your own computer you'll have to go in
the website directory and enter `make serve`
(type `make` on its own to see the other options).

```
cd book/website
make install
make site && make serve
```

#### On Netlify

You'll need the following settings:
- Base directory: `website`
- Build command: `make site`
- Publish directory: `_site`

Netlify is smart and will find your requirements.txt to do the install for you :) (ruby and the jekyll are installed too)
You can find the build history / logs at - https://app.netlify.com/sites/the-turing-way/deploys

## Content Templates

Templates for certain types of content are kept in the `templates` directory.
Templates include:
* `case-study-template.ipynb` - a template for including interactive case studies in the book

The template should be edited accordingly and moved into its relevant chapter folder in the `content` directory.
