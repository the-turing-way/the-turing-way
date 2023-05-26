
(pd-sdpw)=
# Working on Sensitive Data Projects

(pd-sdpw-prerequisites)=
## Prerequisites

| Prerequisite | Importance | Skill Level | Notes |
| -------------|----------|------|----|
| {ref}`Research Data Management <rr-rdm>` | Helpful | Beginner |  |

(pd-sdpw-summary)=
## Summary

In this chapter, we describe how you can work with sensitive data in a practical way.
We cover working on projects that use trusted research environments (TREs) such as data safe havens, including writing code and version control in TREs. 

There are also sub-chapters that describe steps that are good to think about at the start of your project, such as how to {ref}`ensure that your sensitive files remain secure<pd-sdpw-sensitive-files>` when using GitHub. We also show how you can {ref}`safely share your code<pd-sdpw-sensitive-code>`, even though it uses sensitive data, and draw attention to {ref}`what you should do if you inadvertently expose sensitive data on GitHub<pd-sdpw-exposing-data>`.

Sub-chapters include:
* {ref}`Working with Trusted Research Environments<pd-sdpw-trew>`
* {ref}`Privacy-preserving machine learning<pd-sdpw-private-learning>`
* {ref}`Keeping sensitive files secure<pd-sdpw-sensitive-files>`
* {ref}`Sharing your Jupyter notebook<pd-sdpw-sensitive-code>`
* {ref}`Removing sensitive data from Github<pd-sdpw-exposing-data>`
* {ref}`Further recommendations<pd-sdpw-resources>`

  
(pd-sdpw-motivation)=
## Motivation

Working in sensitive data projects can be challenging and it often requires the development of a bespoke way of working for each project.  

Researchers need to consider how they are going to work collaboratively using Trusted Research Environments and how they can enable reproducible research and publish as openly as possible. 
We must also consider how to keep our data secure and prevent unintentional sharing of data. 

