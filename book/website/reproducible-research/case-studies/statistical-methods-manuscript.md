(rr:cs:statistical-methods-manuscript)=
## A Statistical Methods Manuscript


### Version control

The git repository 
[https://github.com/kkmann/sample-size-calculation-under-uncertainty](https://github.com/kkmann/sample-size-calculation-under-uncertainty)
contains all code required to produce the manuscript 
[arXiv:2006.15715](https://arxiv.org/abs/2006.15715)
from scratch.
For an in-depth explanation of the importanc eof version control for 
reproducible research, see {ref}`rr-vcs`.


### Research data management

In this particular case, 
{ref}`rr-rdm` data management aspects are not an issue since the 
the manuscript is exclusively based on hypothetical examples and no
external, protected data is required. 


### Literate programming

The manuscript itself is built using [LaTeX](https://www.latex-project.org/)
from sources contained in the subfolder `latex/`. 
Plain TeX files were prefered over literate programming solutions like 
[knitr](https://github.com/rstudio/rmarkdown) for [R](https://www.r-project.org/)
to facilitate the use of dedicated LaTeX editors like [Overleaf](https://www.overleaf.com/project).
This means, however, that all figures used in the manuscript need to be 
created separately. 
A dedicated [Jupyter notebook](https://jupyter.org/)
`notebooks/figures-for-manuscript.ipynb` combining code and rudimentary 
descriptions is provided to that end. 


### Reproducible software environment

Although this means that all code required to compile the manuscript from scratch
is available,
it is not yet sufficient for true reproducibility.
The just installing LaTeX, Jupyter, and R with the exact same specification 
needed to run all code can be challenging. 
To avoid this from keeping interested readers from experimenting with the code,
a combination of the python package 
[repo2docker](https://github.com/jupyter/repo2docker) and the free 
[mybinderhub.org]() hosting service is used. 
For details on these techniques, see the chapters on {ref}`rr-binder` and {ref}`rr-binderhub`.
This allows interested individuals to start an interacitve version of the 
repository with all required software preinstalled - in exactly the right
versions!
Note that it is possible to provide *version stable* binder links

[![badge](https://img.shields.io/badge/Jupyter%20lab-0.2.1-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/kkmann/sample-size-calculation-under-uncertainty/0.2.1?urlpath=lab/tree/notebooks/figures-for-manuscript.ipynb) [![badge](https://img.shields.io/badge/Shiny-0.2.1-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/kkmann/sample-size-calculation-under-uncertainty/0.2.1?urlpath=shiny/apps/sample-size-calculation-under-uncertainty/)

that point to the state of the repository at a specific point in time (via
th git tagging feature). 
This means tha the links will remain valid and unchanged even if there are 
later corrections to the contents of the repository!
Binder supports multiple user interfaces. 
This is leveraged to provide and Jupyter lab Integrated Development Environment
view on the repository to explore file, the notebook, or to open a shell for
further commands. 
The second badge, directly opens an interactive Shiny app that illustrates 
some of the points discussed in the manuscript and requires no familiarity with
programming at all.


### Workflow management via snakemake

Since Jupyterlab also allows to open a shell in the repository instance opended
via a binder link, 
another feature of the repository can be used to reproduce the *entire manuscript from scratch*.
The python workflow manager [snakemake](https://snakemake.readthedocs.io/en/stable/)
was used to define all required steps in a `Snakefile`.
To execute this workflow,
simply open a shell in the online version of Jupyterhub (via the binderlink)
and type
```
snakemake -F --cores 1  manuscript
```
This will execute all required steps in turn, namely: first create all plots 
and then compiling the actual `latex/main.pdf` file from the LaTeX sources.
All relevant configurations for binder ate located in `.binder`.



### Support for local instantiation of the software environment

The python package repo2docker can also be used locally to reproduce the exact 
same computing environment.
To this end you will need to have python and docker installed. 
For details on docker and container technologies in general, see {ref}`rr:renv:containers`.
Then simply clone the repository on your local machine via
```
git clone git@github.com:kkmann/sample-size-calculation-under-uncertainty.git
cd sample-size-calculation-under-uncertainty
```
and  build a docker container from the configuration files in `.binder/` via
```
jupyter-repo2docker -E .
```
after cloning the repository.
The container is started automatically after the build completes and you can
use the usual Jupyter interface in you browser (via the link printed by repo2docker)
to explore the repository locally.


### Use of cntinuous integration

Although not absolutely necessary from a reproducibility perspective,
the repository also makes use of continuous integration (CE, see {ref}`rr:ci`)
via [GitHub actions](https://github.com/features/actions).
GitHub actions are similar in sprit to {ref}`rr:ci:travis` but the runners are
provided directly via GitHub.
The repository defines two workflows in `.github/workflows`.
The first one, [`.github/workflows/build_and_run.yml`](https://github.com/kkmann/sample-size-calculation-under-uncertainty/blob/master/.github/workflows/build_and_run.yml),
is activated whenever the master branch of the repository is updated and the specifications ins `.binder` are changed,
builds the container, pushes it to a public container repository [docker hub](https://hub.docker.com/repository/docker/kkmann/sample-size-calculation-under-uncertainty) and then checks that the snakemake workflow runs through without problems.
The second one, [`.github/workflows/run.yml`](https://github.com/kkmann/sample-size-calculation-under-uncertainty/blob/master/.github/workflows/run.yml),
runs when `.binder` was not changed and uses the prebuild docker container
to run the snakemake workflow.
The latter saves a lot of computing time (and this trees) since the comoutational
environment will change much less often than the contents of the repository. 
The use of CI thus facilitates checking contributions via pull requests for
technical integrity and makes the respective latest version of the required container 
available for direct download. 
I.e., instead of building the container locally via repo2docker you could just 
download it directly and execute the workflow via 
```
docker run -d --name mycontainer kkmann/sample-size-calculation-under-uncertainty
docker exec --name mycontainer /
    snakemake -F --cores 1  manuscript
```


### Long term archiving and citeability

The GitHub repository is also linked with [zenodo.org]() to ensure long-term
archinving, see {ref}`rr:credit:make-software-citeable`. 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3899943.svg)](https://doi.org/10.5281/zenodo.3899943)

Note that a zenodo DOI can also be used with binderhub to turn a repository snapshot
backed up on zenodo in an interactive environment [see this blog post](https://blog.jupyter.org/binder-with-zenodo-af68ed6648a6).
