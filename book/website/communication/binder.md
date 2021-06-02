(binder)=
# Binder

In this chapter, we will discuss Project Binder as a means to transparently and interactively share research.

(binder-share)=
## Why should you share your work?

(binder-what)=
## What is Binder?

The Binder Project is an open community that makes it possible to create sharable, interactive, reproducible environments.
The technological output of this project is a {ref}`rr-binderhub`.
Binder is built upon a range of open source tools, including [JupyterHub](https://z2jh.jupyter.org), for providing cloud compute resources to users via a browser; and [`repo2docker`](https://repo2docker.readthedocs.io/), for building docker images from projects.
By automating the installation of the computing environment (as discussed in the {ref}`rr-renv` chapter), Binder transforms the overhead of sharing such an environment into the act of sharing a URL.

The cartoon below, by Juliette Taka, demonstrates one workflow a scientist using Binder might adopt.

```{figure} ../figures/binder_comic.png
---
name: binder_comic
alt: An illustration of the steps a person can take to create a binderized project.
---
Figure credit: [Juliette Taka, Logilab and the OpenDreamKit project](https://opendreamkit.org/2017/11/02/use-case-publishing-reproducible-notebooks/)
```

You can find out more about Project Binder and mybinder.org on their [About mybinder.org page](https://mybinder.readthedocs.io/en/latest/about/about.html).

(binder-disam)=
### Disambiguation

In this section, there are some related terms, which will be outlined here for clarity:

- **Binder**: A sharable version of a project that can be viewed and interacted within a reproducible computational environment running in the cloud via a web browser.
- **BinderHub**: A cloud-based infrastructure for generating Binders.
  The most widely-used is [mybinder.org](https://mybinder.org), which is maintained by the Project Binder team.
  It is possible to create other BinderHubs which can support more specialised configurations.
  One such configuration could include authentication to enable private repositories to be shared amongst close collaborators.
- **[mybinder.org](https://mybinder.org)**: A public and free BinderHub.
  Because it is public, you should not use it if your project requires any personal or sensitive information (such as passwords).
- **Binderize**: The process of making a Binder of a project.

(binder-appropriate)=
## When is it appropriate to use Binder?

(binder-faqs)=
## FAQs

(binder-segue)=
## How to create a Binder-ready project

The next chapter contains a [Zero-to-Binder tutorial](z2b) that will guide you through creating your first Binder-ready project on GitHub.
