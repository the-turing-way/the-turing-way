(rr-rdm-fair)=
# The FAIR Principles

The FAIR guiding principles for scientific data management and stewardship {cite:ps}`Wilkinson2016fair` were developed as guidelines to improve the **F**indability, **A**ccessibility, **I**nteroperability and **R**eusability of digital assets; all of which support research reproducibility.
The FAIR principles play an important role in making your data available to others for reuse.

It is much easier to make data FAIR if you plan to do this from the beginning of your research project.
You can plan for this in your Data Management Plan (DMP) (see points 4 and 5 of the {ref}`Data Management Plan<rr-rdm-dmp>` chapter).

Even though the FAIR principles have been defined to allow machines to find and use digital objects automatically, they improve the reusability of data by humans as well.
The capacity of computational systems to find, access, interoperate, and reuse data, with none or minimal human intervention, is essential in today's data-driven era, where humans increasingly rely on computational support to deal with data as a result of the increase in [volume, velocity and
variety](https://www.zdnet.com/article/volume-velocity-and-variety-understanding-the-three-vs-of-big-data/).

This chapter provides an abstract and broad view of what the FAIR principles are. How to put the FAIR principles into practise is discussed in other sub chapters ( {ref}`Data Organisation in Spreadsheets<rr-rdm-fair>`, {ref}`Documentation and Metadata<rr-rdm-metadata>` and {ref}`Sharing and Archiving Data<rr-rdm-sharing>`). You can also use the [Wellcome Getting Started Guide](https://f1000researchdata.s3.amazonaws.com/resources/FAIR_Open_GettingStarted.pdf) or the [How To FAIR](https://howtofair.dk/) website to find out more about the FAIR principles and how to get started.

```{figure} ../../figures/fair-principles.*
---
name: fair-principles
alt: Illustration of the FAIR principles to show the definition of being Findable, Accessible, Interoperable and Reusable.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

(rr-rdm-fair-theory)=
## Theory

In brief, FAIR data should be:

**Findable:** The first step in (re)using data is to find it!
Descriptive metadata (information about the data such as keywords) is essential.

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

The FAIR principles are also applied to software (see [[LGK+20](https://book.the-turing-way.org/afterword/bibliography.html#id10)]and [[HCH+20](https://book.the-turing-way.org/afterword/bibliography.html#id9)]). Watch a [ten minute video on FAIR software](https://www.youtube.com/watch?v=ME8_NRGRhSs&list=PL1CvC6Ez54KDvJbbdLn5rPvf1kInifEh9&index=16) for a short explanation.

## FAIR principles and environmental sustainability

> "FAIR practices can result in highly efficient code implementations, reduce the need to retrain models, and reduce unnecessary data generation/storage, thus reducing the overall carbon footprint.
> As a result, green computing and FAIR practices may boht stimulate innovation and reduce financial costs." - {cite:ps}`Lannelongue2023greener`

## FAIR principles and accessibility

The Accessible in FAIR is not equal to ensuring that your research objects are accessibles to all users. 
For this, the term “actually accessible” has been coined by {cite:ps}`Colon2023accessibility` to refer to data that is "easy to locate, obtain, interpret, use, share, and analyze for everybody, including disabled people."

(rr-rdm-fair-community)=
## Community involvement

Various online resources are provided for people who are working in the life sciences, to guide them in ensuring FAIRness in their data, providing them with tools and advice for good data management at various stages of their work. Two prominent ones include: 
* Under the [FAIR Cookbook](https://faircookbook.elixir-europe.org/content/home.html), several resources are offering guidance and assistance in FAIR data management.
 The FAIR Cookbook is designed to serve a variety of audience types and involved in different stages of data management life cycle.
The FAIR Cookbook is developed and maintained by life sciences professionals, both in the academia and industry sectors, including members of the ELIXIR community. 
* Under [ELIXIR Research Data Management Kit (RDMkit)](https://rdmkit.elixir-europe.org/), resources are provided for life scientists to guide them in better management of their research data in adhering to the FAIR Principles. 
It is an attempt to help researchers work at different capacities, both in individual and collaborative workspaces.
The RDMkit is open for suggestions from anyone, as long as they abide by the [contributor responsibilities](https://rdmkit.elixir-europe.org/how_to_contribute).



Many groups and organisations are working to define guidance and tools to help researchers and other stakeholders (like librarians, funders, publishers, and trainers) make data more FAIR.
There are two global initiatives that act as umbrella organisations and reference points for many discipline-specific efforts, including the ones listed above: [GOFAIR](https://www.go-fair.org) and the [Research Data Alliance (RDA)](https://www.rd-alliance.org).
* Under GOFAIR, there are many [Implementation Networks (INs)](https://www.go-fair.org/implementation-networks) committed to implementing the FAIR principles.
* Under the RDA, there are several groups tackling different aspects relevant to the RDM life cycle. Among these, one group, the [FAIR Data Maturity Model Working Group](https://www.rd-alliance.org/groups/fair-data-maturity-model-wg) is reviewing existing efforts, building on them to define a standard set of common assessment criteria for the evaluation of FAIRness.

## More information
- Deep dive into the [FAIR principles by Dr. Maryann Martone](https://www.youtube.com/watch?v=xx2wHxQfcnA) (45 minute video)
