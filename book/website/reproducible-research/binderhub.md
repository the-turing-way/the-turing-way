(rr-binderhub)=
# BinderHub

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
|---|---|---|
| [Version Control](./version-control) | Very Important | |
| [Reproducible Environments](./reproducible-environments) | Very Important | Particularly read the section on [Binder](./reproducible-environments/binder). |

This chapter will discuss [BinderHub](https://binderhub.readthedocs.io/en/latest/index.html), which is the cloud technology powering [Binder](https://mybinder.readthedocs.io/en/latest/).
We will cover the technologies and tools that BinderHub utilises and the resources you will need to setup your own BinderHub.

This chapter is primarily aimed at Research Software Engineers and IT Services who wish to provide a BinderHub as a service to a group of researchers.
Though anyone can build a BinderHub.

## How this will help you/ why this is useful

Reading this chapter will give you a clearer picture of how Binder services (such as [mybinder.org](https://mybinder.org)) operate, the technologies powering BinderHub and how they interact with one another.
This chapter also covers reasons why you might build your own BinderHub, rather than using the public service at mybinder.org.
