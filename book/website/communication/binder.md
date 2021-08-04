(binder)=
# Binder

In this chapter, we will discuss Project Binder as a means to transparently and interactively share research.

(binder-share)=
## Why should you share your work?

(binder-what)=
## What is Binder?

We've discussed why it's important to share your work and we've reached a point where we've decided to publish some Jupyter Notebooks with analysis code on a collaboration platform, such as GitHub.

GitHub is a great platform for sharing code _statically_.
If the repository is public, anyone can navigate to your Notebook and read the contents.
However, _running_ code is a lot more complicated than just displaying it as GitHub does.
A lot of interdependent parts are required to run code, such as:

- a copy of the code itself;
- the appropriate software to execute it;
- any extra packages the code depends on that aren't shipped as part of the core software;
- any input data the analysis requires;
- and you also need some hardware (a computer!) to run it on as well.

On top of acquiring all those parts, you also have to install them correctly and in such a way that they are not influenced or come into conflict with other software that may be running on your machine.
It's a lot of work!

How much easier would it be if we could **run code in the browser**, similar to how it's currently displayed?
This is what Project Binder aims to achieve.

Project Binder provides a user with the following infrastructure:

- some hardware to execute code, usually a server hosted in the cloud but can be on-premise hardware too;
- a computational environment containing:
  - the approriate software,
  - any extra package dependencies,
  - any required input data,
  - and a copy of the code itself (Notebooks or scripts);
- a URL to where the environment is running so the code can be interacted with by you or your collaborators.

Binder has packaged together all of the moving parts that make sharing computational work challenging into a simple to use interface.
There is a **free and public** version of this interface running at [**mybinder.org**](https://mybinder.org).

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
