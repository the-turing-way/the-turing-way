(binder)=
# Binder

In this chapter, we will discuss Project Binder and mybinder.org as a means to transparently and interactively share research.

(binder-share)=
## Why should you share your work?

Motivation for sharing research outputs is more deeply explored in the {ref}`rr-open` chapter.

In short, sharing your research code can help provide context to the results you present by illustrating the process you went through to reach them.
By sharing code, we also avoid reinventing the wheel in order to make progress on a research topic since the previous tools are available to be built on top of.

However, the biggest barrier to sharing code is often installing packages and setting up the computational environment, as we will see in the next section.
By sharing your work via platforms such as mybinder.org:

- Installing software packages is no longer a challenge
- People using different operating systems have similar experiences since the computation is happening on the platform, not their local machine
- Your work can be distributed to a broader audience since the technical barrier has been lowered

(binder-what)=
## What is Project Binder?

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

How much easier would it be if we could **run code in the browser**, similar to how it's displayed?
This is what Project Binder aims to achieve.

Project Binder provides a user with the following infrastructure:

- some hardware to execute code, usually a server hosted in the cloud but can be on-premise hardware too;
- a computational environment containing:
  - the approriate software,
  - any extra package dependencies,
  - any required input data,
  - and a copy of the code itself (Notebooks or scripts);
- a URL to where the environment is running so the code can be interacted with by you or your collaborators.

Project Binder has packaged together all of the moving parts that make it challenging to share computational work into a simple to use interface.
There is a **free and public** version of this interface running at [**mybinder.org**](https://mybinder.org).

The cartoon below, by Juliette Taka, demonstrates one workflow a that scientist using Binder might adopt.

```{figure} ../figures/binder-comic.*
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

- **Project Binder**: An open community that makes it possible to create sharable, interactive, reproducible environments.
  The technological output of this project is a {ref}`rr-binderhub`.
- **BinderHub**: A cloud-based infrastructure for generating Binders.
  The most widely-used is [mybinder.org](https://mybinder.org), which is maintained by the Project Binder team.
  It is built upon a range of open source tools, including [JupyterHub](https://z2jh.jupyter.org), for providing cloud compute resources to users via a browser; and [`repo2docker`](https://repo2docker.readthedocs.io/), for building docker images from projects.
  Since it is an open project, it is possible to create other BinderHubs which can support more specialised configurations.
  One such configuration could include authentication to enable private repositories to be shared amongst close collaborators.
- **A Binder**: A sharable version of a project that can be viewed and interacted within a reproducible computational environment running in the cloud via a web browser.
  By automating the installation of the computing environment (as discussed in the {ref}`rr-renv` chapter), Project Binder transforms the overhead of sharing such an environment into the act of sharing a URL.
- **[mybinder.org](https://mybinder.org)**: A public and free BinderHub.
  Because it is public, you should not use it if your project requires any personal or sensitive information (such as passwords).
- **Binderize**: The process of making a Binder from a project.

(binder-appropriate)=
## When is it appropriate to use mybinder.org?

Maintaining a free, anonymous service in the cloud is a lot of voluntary work and costs a lot of money.
In order to reduce the running costs somewhat, mybinder.org places computational restrictions on each running Binder instance.
These restrictions are:

- 1 CPU, and
- 1 GB of RAM.

Hence, mybinder.org is **not** an appropriate place to perform end-to-end replications of Machine Learning workflows, for example!

And this is the primary reason why this chapter on Binder has been placed in the "Guide for Communication".
With these computational restrictions, mybinder.org lends itself very well to hosting interactive demonstrations and learning resources for software packages or research analyses.
In this scenario, the people clicking the Binder link probably want to learn something, and sitting through a time-consuming model-training process likely won't help them achieve that.
Instead, you could provide pre-trained models or instructions on how to train the models on their own hardware and _come back_ to the Binder for the remainder of the interactive tutorial.

So, when is it appropriate to use mybinder.org?

- When you want to _communicate_ something in an interactive manner, such as short analyses, tutorials, or even blogs!
  Check out [Achintya Rao's blog powered by mybinder.org](https://blog.achintyarao.in/about/)!
- When the code and associated data (if relevant) are publicly available
- When the code you want to run interactively does not require a lot of resource or specialist resources (for example, GPUs)

(binder-faqs)=
## FAQs

Many common questions are answered on the [About mybinder.org page](https://mybinder.readthedocs.io/en/latest/about/about.html).

### How do I save my changes back to my repository?

Unfortunately, you can't.
At least, not from the command line in a running Binder instance.

Writing back to a hosted repository, whether it be on GitHub or some other platform, will require a credential of some kind to authorise you to write to that repository.
And as has been mentioned, mybinder.org is a completely public service and you should not provide any sensitive information to a running Binder instance under any circumstances.

However, mybinder.org does run an add-on called [`jupyter-offlinenotebook`](https://github.com/manics/jupyter-offlinenotebook) which provides a download button to save your notebooks locally, _even if your browser has lost its connection with the cloud infrastructure that is providing the compute!_
This means you can save your progress locally, update your repository with your saved notebooks, and relaunch your Binder with the updated notebooks.

```{figure} ../figures/binder_notebook_banner.*
---
name: binder_notebook_banner
alt: A screenshot of the control panel of a Jupyter Notebook with a download button highlighted by a purple rectangle.
---
Using this "Download" button in a Jupyter Notebook running on mybinder.org will allow you to save your notebooks locally, even after the Binder instance has been disconnected from computational resources.
```

### How can I collaborate with my peers on mybinder.org?

It's not impossible, but there's definitely room to develop this feature in comparison to other "free cloud compute" services available.

Those who are interested in this, can find out more in [this Discourse post](https://discourse.jupyter.org/t/collaborating-on-one-binder-instance/407) and in the [`jupyterlab-link-share` repository](https://github.com/jtpio/jupyterlab-link-share).

### How is mybinder.org different to Google Colab?

Google Colab provides a "kitchen sink" computational environment with many of the most popular data science software packages pre-installed.
In contrast, mybinder.org builds bespoke images for each repository launched, specifically installing the packages listed in your configuration files.

### Can I connect to `INSERT DATA PROVIDER HERE`?

Network connections on mybinder.org are quite limited for security and abuse-prevention purposes.
That being said you should be able to connect to an external data provider so long as it satisfies the following two criteria:

- It can be accessed over an HTTP/HTTPS connection
- You do not need credentials to access the data

Remember, mybinder.org is an entirely public service and under no circumstances should you provide confidential information, such as credentials, to a Binder instance.

(binder-segue)=
## How to create a Binder-ready project

The next chapter contains a [Zero-to-Binder tutorial](z2b) that will guide you through creating your first Binder-ready project on GitHub.
