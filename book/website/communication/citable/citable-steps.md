(cm-citable-steps)=
# Steps for Making Research Objects Citable

There are many reasons why authors don't cite the data, protocols, software and hardware that they use, but one of the biggest ones is that it's not clear how.
You can go a long way to reducing this barrier by following a few steps to make it as easy as possible.

(cm-citable-steps-object)=
## 1. Identify Your Research Objects

We want to emphasise that most of our research objects should be shared so that other researchers can reproduce and reuse them.
 Therefore, the first step is to identify all the research components that you would share online.
Practising open research isn't essential to get credit for your data or software, but it makes it much easier for others to build on your work in a way that acknowledges your contribution.
There is a growing body of evidence that shows open research tends to be cited more than non-open research of equivalent quality and significance.

As part of the citation for your research objects, it is important to publish research objects beyond papers, such as images, data, software, protocols, methods, and workflow associated with your research.

The best way to get started with this will be to look up some examples of what kind of research objects are or should be cited.
Finding commonly referenced research objects in your discipline serves two purposes:
1. It demonstrates that software & data are things that can be cited;
2. It gives authors a reference and format that they can copy and paste directly into their document.
<!-- TODO: Cite relevant paper for this (Piwowar et al 2013?) -->

```{note}
You can learn more about the different types of research objects in the chapters {ref}`making your research open<rr-open>` and {ref}`making your research FAIR<rr-rdm>`.
```

(cm-citable-steps-publish)=
## 2. Publish your work online

Online publications are attached to [persistent identifiers](https://www.youtube.com/watch?v=iea6d5oI8Ag) that are used for citing them.
It's important to note that not everything published online gets a unique identifier but it is important that research objects are published online with DOIs as described below.

(cm-citable-steps-doi)=
### DOIs

```{figure} ../../figures/DOI.*
---
name: doi
alt: This image shows three boxes with materials on top. The main box in the middle has 'identifiers' written on it with three discs on top of it that are labelled 'data sets'. Both boxes by their side have journal articles on top of them. An arrow on the top of the image points to these images as being 'Digital Object Identifiers'. There is text at the bottom of the image which says 'Persistent', 'Unique', 'Trusted'.
---
Digital Object Identifiers or DOIs are persistent, unique and trusted. _The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

Unique identifiers or persistent links for digital objects are more formally called [Digital Object Identifiers or DOIs](https://en.wikipedia.org/wiki/Digital_object_identifier).
Using DOIs makes it much easier for others to cite your data, reduces the risk of link rot and means you can track how your research is being used and cited.

### Servers that provide DOIs

Independent of the paper, different research objects can be published online on servers that offer DOIs.
Some of these servers are [Zenodo](https://zenodo.org/) and [FigShare](https://figshare.com/) (for different objects such as figures, presentations and reports), [Data Dryad](https://datadryad.org/stash) (for data), [Open Grants](https://www.ogrants.org/) (for grant proposals) and [Open Science Framework (OSF)](https://osf.io/) (for different components of an open research project).

It's perfectly possible to cite a dataset or software package directly, and most major publishers now permit this in their style guides.
However, it can sometimes help to have a more conventional paper to cite, and this is where software and data journals come in.
These journals are similar to methods journals, in that they tend not to include significant results but instead focus on describing data and software in sufficient detail to allow reuse.
Some examples include:
- [Journal of Open Research Software](https://openresearchsoftware.metajnl.com/)
- [Journal of Open Source Software](https://joss.theoj.org/)

You can read more about these different article types in our {ref}`Chapter on Publishing Different Article Types<cm-dif-articles>`.

(cm-citable-steps-referencing)=
## 3. Add Machine-Readable Referencing Information

You can go a step further by allowing people to import information about your research objects into their preferred referencing database.
If [BibTeX](https://en.wikipedia.org/wiki/BibTeX) is popular in your field for managing references, post a `.bib` file of *all* your outputs (not just your papers).
If [Endnote](https://endnote.com/) is more popular, make an Endnote export available.
If you use GitHub, GitLab or a similar public repository, consider creating a `CITATION.cff` file in each repository, which will describe how someone can refer to different research outputs from your project.
You can read more about `CITATION.cff` in {ref}`Software citation with CITATION.CFF <cm-citable-cff>`.

If possible, provide several formats: you won't need to update these very often and it will pay off.

```{note}
Many online tools allow exporting citation of research objects in different formats.
For example, see [https://www.citethisforme.com/](https://www.citethisforme.com/).
```
