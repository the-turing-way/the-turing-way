# Introduction to BinderHub

[BinderHub](https://binderhub.readthedocs.io/en/latest/index.html) is a cloud-based technology that can launch a repository of code (from GitHub, GitLab, and others) in a browser window such that the code can be executed and interacted with.
A unique URL is generated allowing the interactive code to be easily shared.

The purpose of these Binder instances is to promote reproducibility in research projects by encouraging researchers to document their software dependencies and produce fun, interactive environments!

Binder, as a user interface, is useful for reproducibility because the code needs to be version controlled and the computational environment needs to be documented in order to benefit from the functionality of Binder.
Each change to the code repository also forces a new build of the Binder instance.
This acts as a proxy for continuous integration of the computational environment as the Binder instance will break if the configuration file is not updated.

Learn more about Continuous Integration in [this chapter](../continuous_integration/continuous_integration).

## How does a BinderHub work?

BinderHub relies on different tools and resources in order to create and launch the Binder instances.

For more information, see this [high-level explanation of the BinderHub architecture](https://binderhub.readthedocs.io/en/latest/overview.html).

| ![../../figures/cloud_neutral_binderhub.png](https://zenodo.org/api/iiif/v2/e4125eaf-b456-4097-85fc-6a2e80482d1c:96c70193-2f9e-442d-8cf8-21485d8864e1:1728_TURI_Book%20sprint_45%20repo2docker_040619_v2_MK.jpg/full/750,/0/default.jpg) |
|:---:|
| A representation of the BinderHub architecture. This image was created by [Scriberia](http://www.scriberia.co.uk/) for The Turing Way community and is used under a CC-BY licence. |
