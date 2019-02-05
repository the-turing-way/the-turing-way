# Reproducible, Reliable, Reusable Analyses with BinderHub on Cloud

Sarah Gibson, _The Alan Turing Institute_

## The Problem

Here's my thesis:

<html><img src="thesis.jpg" alt="thesis" height="420" width="420"></html>

And [a video](https://www.dropbox.com/s/rxxvv7pxbf4y4q6/demo1_edited.mov?dl=0) of the laptop producing a figure for [my first journal paper](https://arxiv.org/pdf/1706.04802.pdf).

This work would be difficult for anyone to reproduce for a number of reasons:
* Was not version controlled
* Computing environment was not documented
* Computing environment no longer exists since the laptop has been returned and wiped :scream:

## Binder to the Rescue!

[My PhD repo](https://github.com/sgibson91/magprop/tree/ff527ae769fa9562e42556bdc8f38e7751bd4cb2)

Click the "launch binder" button. When JupyterLab has loaded, open a Python 2 Console and execute `%run code/figure2.py` (SHIFT+RETURN to execute) to reproduce the same plot in the video. A sub-folder called plots will be created and the figure saved there.

## Why tracking Dependencies is Important

Version updates to software packages could cause fundamental changes to your code that do not raise a fatal error, and so will pass without you realising.

[UKRI demo repo](https://github.com/sgibson91/ukri_demo)

## What is Binder doing?

<html><img src="binder_demo.jpg" alt="mybinder" height="420" width="540"></html>

Courtesy of [Juliette Belin](https://twitter.com/JulietteTaka/status/1082735653929000960)

## Issues with the current Binder

* Only works for **public** repos, cannot host private code or sensitive data
* Large datasets are discouraged
* Computing resources are minimal

## Solution: BinderHub 4 U

<html><img src="binder_demo2.jpg" alt="yourbinder" height="420" width="580"></html>

**Some useful links:**
* [Zero-to-JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/)
* [Zero-to-JupyterHub with Kubernetes](https://zero-to-jupyterhub.readthedocs.io/en/latest/index.html)
* [Step Zero: Kubernetes on Microsoft Azure](https://zero-to-jupyterhub.readthedocs.io/en/latest/microsoft/step-zero-azure.html)
* [repo2docker](https://repo2docker.readthedocs.io/en/latest/?badge=latest)

## Finally...

Please come and visit our repo! [The Turing Way](https://github.com/alan-turing-institute/the-turing-way)
