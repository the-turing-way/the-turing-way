# Reproducible, Reliable, Reusable Analyses with BinderHub on Cloud

Sarah Gibson, _The Alan Turing Institute_

## The Problem

Here's my thesis:

![thesis](thesis.jpg)

And [a video](https://www.dropbox.com/s/rxxvv7pxbf4y4q6/demo1_edited.mov?dl=0) of the laptop producing a figure for [my first journal paper](https://arxiv.org/pdf/1706.04802.pdf).

This work would be difficult for anyone to reproduce for a number of reasons:
* Was not version controlled
* Computing environment was not documented
* Computing environment no longer exists since the laptop has been returned and wiped :scream:

## Binder to the Rescue!

[My PhD repo](https://github.com/sgibson91/magprop/tree/ff527ae769fa9562e42556bdc8f38e7751bd4cb2)

Run `code/figure2.py` to reproduce the same plot in the video.

## Issues with the current Binder

* Only works for **public** repos, cannot host private/sensitive code or data
* Large datasets are discouraged
* Computing resources are minimal

## Solution: BinderHub 4 U

Now going to demo how you can build your own BinderHub for your Institution/Company/RSE group tailored to their needs.

Some useful links:
* [Zero-to-JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/)
* [Zero-to-BinderHub](https://binderhub.readthedocs.io/en/latest/)
* [repo2docker](https://repo2docker.readthedocs.io/en/latest/?badge=latest)
