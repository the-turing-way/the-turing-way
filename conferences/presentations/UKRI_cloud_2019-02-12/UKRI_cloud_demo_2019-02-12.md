# Reproducible, Reliable, Reusable Analyses with BinderHub on Cloud

Sarah Gibson, _The Alan Turing Institute_

## What does "Reproducibility" mean?

* It has a lot of different meanings across research fields
* In this context, to be "reproducible" means the same results (e.g. that are published in a paper) are generated given the same input data pushed through the same analysis pipeline

**An independent person should be able to easily check my (our) work.**

## An Example of Not Being Reproducible
**(AKA: I'm guilty of this too...)**

<html><img src="graduation.png" alt="graduation" height="415" width="480"></html>

* Astrophysics PhD, graduated January 2019
* Researched phenomenon known as Gamma-Ray Bursts (not your average supernova...) and the neutron stars that power them

<html><img src="figure2.png" alt="figure2" height="400" width="320"></html>

* This is a figure published in [my first journal paper](https://arxiv.org/pdf/1706.04802.pdf)
* It describes the evolution of the spin of a neutron star (middle panel) and the mass of its accretion disc (top panel) as it was being fed by fallback accretion
* The bottom panel is the property we were interested in which is when a derived parameter would cross a specific threshold (the dashed line)

**What my research was about isn't necessarily important.
What is important is whether other scientists in my field could verify my work.**

Here is [a video](https://www.dropbox.com/s/rxxvv7pxbf4y4q6/demo1_edited.mov?dl=0) of my PhD laptop producing the figure which turned out to **not** be reproducible for a number of reasons:
* Was not version controlled
* Computing environment(s) was not documented
* Computing environment no longer exists - the laptop has been returned and wiped :scream:

## Binder to the Rescue!

With a little bit of work, I've managed to reproduce my figure using [Binder](https://mybinder.org).

* My code is in a public GitHub repo - now version controlled :ballot_box_with_check:
* The computing environment has been documented in an `environment.yml` file :ballot_box_with_check: _(other config file types are available)_

[My PhD repo](https://github.com/sgibson91/magprop/tree/ff527ae769fa9562e42556bdc8f38e7751bd4cb2)

## What is Binder doing?

<html><img src="binder_demo.jpg" alt="mybinder" height="420" width="540"></html>

Courtesy of [Juliette Belin](https://twitter.com/JulietteTaka/status/1082735653929000960)

## Limitations with the public Binder instance

* Only works for **public** repos, cannot host private code or sensitive data
* Large datasets are discouraged
* Computing resources are minimal

## Solution: BinderHub 4 U

<html><img src="binder_demo2.jpg" alt="yourbinder" height="420" width="580"></html>

This is something we're trying to achieve at the Turing Institute.

**Some useful links if you'd like to try yourself:**
* [Zero-to-JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/)
* [Zero-to-JupyterHub with Kubernetes](https://zero-to-jupyterhub.readthedocs.io/en/latest/index.html)
* [Step Zero: Kubernetes on Microsoft Azure](https://zero-to-jupyterhub.readthedocs.io/en/latest/microsoft/step-zero-azure.html)
* [repo2docker](https://repo2docker.readthedocs.io/en/latest/?badge=latest)

## Why tracking Dependencies is Important (demo)

Version updates to software packages could cause fundamental changes to your code that do not raise a fatal error, and so will pass without you realising.

Here's a little demo to highlight this: [UKRI demo repo](https://github.com/sgibson91/ukri_demo)

## Thank You

Thanks to **The Turing Way** team!
* Kirstie Whitaker (PI)
* Martin O'Reilly
* Louise Bowler
* Anna Krystalli
* Becky Arnold
* Patricia Herterich
* Rosie Higman
* Alexander Morley
* ... and me!

**The Turing Way** is a lightly opinionated guide to reproducible data science.
Our goal is to provide all the information that researchers need at the start of their projects to ensure that they are easy to reproduce at the end.

Please visit our repo and help us deliver our dream!

[github.com/alan-turing-institute/the-turing-way/](https://github.com/alan-turing-institute/the-turing-way)
