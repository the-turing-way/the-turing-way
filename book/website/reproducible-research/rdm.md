(rr-rdm)=
# Research Data Management

(rr-rdm-prerequisites)=
## Prerequisites

The following sections in this handbook provide useful context and complementary information to this chapter:

| Prerequisite                                        | Importance |
| --------------------------------------------------- | ---------- |
| {ref}`rr-vcs` | Helpful    |
| {ref}`rr-open`      | Helpful    |

(rr-rdm-summary)=
## Summary

Research Data Management (RDM) [{term}`def<Research Data Management>`] covers how research data can be stored, described and reused.
Data here is used as a generic term to encompass all digital objects.
RDM is a vital part of enabling reproducible research.
RDM ensures efficiency in research workflows, and also greater reach and impact, as data become {ref}`FAIR <rr-rdm-fair>` (Findable, Accessible, Interoperable and Reusable).
Data should be stored in multiple locations and backed-up regularly to prevent loss or data corruption.
Clearly describing data using documentation and metadata ensures that others know how to access, use and reuse your data, and also enable conditions for sharing and publishing data to be outlined.

```{figure} ../figures/data-ecosystem.*
---
height: 400px
name: data-ecosystem
alt: image of the data ecosystem with private and public data.
---
Open and closed data for reproducibility.
_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300. 
```


(rr-rdm-useful)=
## Motivation and Background

```{figure} ../figures/rdm-storage.*
---
height: 400px
name: rdm-storage
alt: A cartoon woman standing in front of a very messy closet. She is looking for data that she generated last year. Behind her a person is watching doubtfully, unsure whether she can find it in this mess.
---
Research Data Management: making it possible to retreive data from last year.
_The Turing Way_ project illustration by Scriberia. Original version on Zenodo. http://doi.org/10.5281/zenodo.3695300. 
```

- {ref}`Managing your data <rr-rdm-storage-organisation>` allows you to always find your data and ensure the quality of scientific practice.
- {ref}`Storing your data properly <rr-rdm-storage>` and backing-up regularly prevents data loss.
- It can help with {ref}`recognition <cm-citable-orcid>` for all research outputs.
- It stimulates **collaboration** with others, who will find it easier to {ref}`understand and reuse your data <rr-rdm-metadata>`.
- RDM is cost/time efficient (see [Why Does Data Need to be Managed?](https://www.youtube.com/watch?v=C7RZ2t3Cpig)), especially if {ref}`shared publicly <rr-rdm-sharing>`, as you will always be able to find and use your data.
