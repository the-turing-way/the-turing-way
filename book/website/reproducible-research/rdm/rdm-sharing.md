(rr-rdm-sharing)=
# Sharing and Archiving Data

(rr-rdm-sharing-motivations)=
##  Motivations For Sharing Data
There are many reasons to share your research data publicly.

1. To allow the possibility to fully reproduce a scientific study.
2. To prevent duplicate efforts and speed up scientific progress.
Large amounts of research funds and careers of researchers can be wasted by only sharing a small part of research in the form of publications.
3. To facilitate collaboration and increase the impact and quality of scientific research.
4. To make results of research openly available as a public good, since research is often publicly funded.

You can read more about why data should be available, and why some data should remain closed, in the {ref}`Open Data section <rr-open-data>`.

```{figure} ../../figures/birds-of-open-data.*
---
height: 400px
name: birds-of-open-data.*
alt: Two birds in a fountain of open data. One asks "You mind if I reuse this data?" The other answers "Go ahead! We can even work together on it!"
---
Birds of Open Data. _The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

(rr-rdm-sharing-steps)=
## Steps To Share Your Data

### Step 1: Select what data you want to share

Not all data can be made openly available, due to ethical and commercial concerns (see the {ref}`Open Data section <rr-open-data>`), and you may decide that some of your intermediate data is too large to share.
As such, you first need to decide which data you need to share for others to be able to reproduce your research.

### Step 2: Choose a data repository or other sharing platform

Data should be shared in a formal, open, and indexed data repository [{term}`def<Repository>`] where possible so that it will be accessible in the long run.
Suitable data repositories by subject, content type or location can be found at [Re3data.org](https://www.re3data.org/), and in [FAIRsharing](https://fairsharing.org/databases) where you can also see which standards (metadata and identifier) the repositories implement and which journal/publisher recommend them.
If possible use a repository that assigns a DOI, a digital object identifier, to make it easier for others to cite your data. Have a look in the {ref}`cm-citable` to see how to share and cite your data and other research objects. The {ref}`cm-citable-linking` section explains several options for linking your data and other research objects.

A few public data repositories are [Zenodo](https://zenodo.org/), [Figshare](https://figshare.com/), [Harvard Dataverse](https://dataverse.harvard.edu/), [4TU.ResearchData](https://data.4tu.nl/info/en), and [Dryad](https://datadryad.org/). 
See the [NIH list of Generalist Repositories](https://sharing.nih.gov/data-management-and-sharing-policy/sharing-scientific-data/generalist-repositories) for more data repositories.

### Step 3: Choose a licence and link to your paper and code

So that others know what they can do with your data, you need to apply a licence [{term}`def<License>`] to your data.
The most commonly used licences are [Creative Commons](https://creativecommons.org/choose/), [Open Government Licence](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), or an [Open Data Commons Attribution License](https://opendatacommons.org/licenses/by/index.html).
To get maximum value from data sharing, make sure that your paper and code both link to your data, and vice versa, to allow others understand your project better.
See {ref}`rr-licensing` for more information. 

### Step 4: Upload your data and documentation

In line with the {ref}`FAIR principles <rr-rdm-FAIR>`, upload the data in open formats as much as possible and include sufficient documentation and metadata so that someone else can understand your data.
It is also essential to think about the file formats in which the information is provided.
Data should be presented in structured and standardised formats to support interoperability, traceability, and effective reuse.
In many cases, this will include providing data in multiple, standardized formats, so that it can be processed by computers and used by people.

(rr-rdm-sharing-resources)=
## Additional resources on data sharing
* '[How can you make research data accessible?](https://www.software.ac.uk/how-can-you-make-research-data-accessible)': a blog that contains five steps to make your data more accessible
* The European Commission's [data guidelines](https://open-research-europe.ec.europa.eu/for-authors/data-guidelines)
* Videos on [Data sharing and reuse](https://www.youtube.com/watch?v=4igGBCggU0Y) & [Data Preservation and Archiving](https://www.youtube.com/watch?v=J76yTp8XE-0) from the [TU Delft Open Science MOOC](https://online-learning.tudelft.nl/courses/open-science-sharing-your-research-with-the-world/).
* [Webinar: Why share your data?](https://www.ebi.ac.uk/training/online/courses/bringing-data-life-data-management-biomolecular-sciences/why-share-your-data/)
* [Webinar: Publishing and citing data in practice by Jez Cope](https://youtu.be/PpMOkTnBMlI)
* Coursera Videos from [Research Data Management and Sharing](https://www.coursera.org/learn/data-management) on the [Benefits of Sharing](https://www.coursera.org/lecture/data-management/benefits-of-sharing-IPZ0h), [Why Archive Data?](https://www.coursera.org/lecture/data-management/why-archive-data-lcQ2m), and [Why is Archiving Data Important?](https://www.coursera.org/lecture/data-management/why-is-archiving-data-important-04Gji)
* [Blog: Ask not what you can do for open data; ask what open data can do for you](http://blogs.nature.com/naturejobs/2017/06/19/ask-not-what-you-can-do-for-open-data-ask-what-open-data-can-do-for-you/)
* {cite:ps}`Levenstein2018sharing`

(rr-rdm-data-availability-statement)=
## Data Availability Statement
Once you made your data available, it is important to ensure that people can find it when they read the associated article.
You should cite your dataset directly in the paper in places where it is relevant, and include a citation in your reference list, as well as include a Data Availability Statement at the end of the paper (similar to the acknowledgement section).
See {ref}`cm-citable-cite-data` for some examples.

