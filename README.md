## The Turing Way Book
*For the main repo (where most of the issues live, check out [this one](https://github.com/alan-turing-institute/the-turing-way)*

All the text for each chapter lives inside it's own folder in the `content/` directory.

Everything else is in the `website/`. Importantly this includes the figures, which are in the `website/assets/figures/` directory.

### Configuration
- To change the table of contents (order of the chapters) see the `website/_data/toc.yml` file. Documentation can be found on the [jupyter book website](https://jupyter.org/jupyter-book/intro.html).
- Same applies for more general configuration using `website/_config.yml`

### Deploying
The site is built automatically using these two directories. All of the requirements are specificied in `website/requirements.txt`. 

#### Locally
If you want to see your local changes on your own computer you'll have to go in the website directory and enter `make serve` (type `make` on it's own to see the other options).

#### On Netlify
You'll just need the following settings:
- Base directory: `website`
- Build command: `make site`
- Publish directory: `_site`
