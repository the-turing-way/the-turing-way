(rr-rdm-fair)=
# The FAIR Principles

The FAIR guiding principles for scientific data management and stewardship {cite}`Wilkinson2016fair` were developed as guidelines to improve the **F**indability, **A**ccessibility, **I**nteroperability and **R**eusability of digital assets; all of which support research reproducibility.
The FAIR principles play an important role in making your data available to others for reuse.

It is much easier to make data FAIR if you plan to do this from the beginning of your research project.
You can plan for this in your Data Management Plan (DMP) (see points 4 and 5 of the {ref}`Data Management Plan<rr-rdm-dmp>` chapter).

Even though the FAIR principles have been defined to allow machines to find and use digital objects automatically, they improve the reusability of data by humans as well.
The capacity of computational systems to find, access, interoperate, and reuse data, with none or minimal human intervention, is essential in today's data-driven era, where humans increasingly rely on computational support to deal with data as a result of the increase in [volume, velocity and
variety](https://www.zdnet.com/article/volume-velocity-and-variety-understanding-the-three-vs-of-big-data/).

This chapter provides an abstract and broad view of what the FAIR principles are. How to put the FAIR principles into practise is discussed in other sub chapters ( {ref}`Data Organisation in Spreadsheets<rr-rdm-fair>`, {ref}`Documentation and Metadata<rr-rdm-metadata>` and {ref}`Sharing and Archiving Data<rr-rdm-sharing>`). You can also use the [Wellcome Getting Started Guide](https://f1000researchdata.s3.amazonaws.com/resources/FAIR_Open_GettingStarted.pdf) or the [How To FAIR](https://howtofair.dk/) website to find out more about the FAIR principles and how to get started.

```{figure} ../../figures/fair-principles.jpg
---
name: fair-principles
alt: Illustration of the FAIR principles to show the definition of being Findable, Accessible, Interoperable and Reusable.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

(rr-rdm-fair-theory)=
## Theory

In brief, FAIR data should be:

**Findable:** The first step in (re)using data is to find them!
Descriptive metadata (information about the data such as keywords) are essential.

**Accessible:** Once the user finds the data and software they need to know how to access it.
Data could be openly available but it is also possible that authentication and authorisation procedures are necessary.

**Interoperable:** Data needs to be integrated with other data and interoperate with applications or workflows.

**Reusable:** Data should be well-described so that they can be used, combined, and extended in different settings.

You can find a more detailed [overview of the FAIR principles by GO FAIR](https://www.go-fair.org/fair-principles) of what the FAIR principles recommend.
You can also read [A FAIRy tale](https://doi.org/10.5281/zenodo.2248200) for an understandable explanation of each principle.

Making data 'FAIR' is not the same as making it 'open'.
Accessible means that there is a procedure in place to access the data.
Data should be as open as possible, and as closed as necessary.

It is also important to say that the FAIR principles are aspirational: they do not strictly define how to achieve a state of FAIRness, but rather describe a continuum of features, attributes, and behaviours that will move a digital resource closer to that goal.

The FAIR principles are also applied to software (see {cite}`Lamprecht2020FAIRsoftware`and {cite}`Hasselbring2020FAIRsoftware`).


(rr-rdm-fair-community)=
## Community involvement

Although started by a community operating in the life science, the FAIR principles have rapidly been adopted by publishers, funders, and pan-disciplinary infrastructure programmes and societies.
Many groups and organisation are working to define guidance and tools to help researchers and other stakeholders (like librarians, funders, publishers, and trainers) make data more FAIR.
If you are interested in participating in these communities there are two global initiatives that act as umbrella organizations and reference points for many discipline-specific efforts: [GOFAIR](https://www.go-fair.org) and the [Research Data Alliance (RDA)](https://www.rd-alliance.org).
* Under GOFAIR, there are many [Implementation Networks (INs)](https://www.go-fair.org/implementation-networks) committed to implementing the FAIR principles.
* Under the RDA, there are several groups tackling different aspects relevant to the RDM life cycle. Among these, one [group](https://www.rd-alliance.org/groups/fair-data-maturity-model-wg) is reviewing existing efforts, building on them to define a standard set of common assessment criteria for the evaluation of FAIRness.
