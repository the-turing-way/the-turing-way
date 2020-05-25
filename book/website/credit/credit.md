# Credit for reproducible research

<!--

Future work:

- Demonstrating impact with various metrics

-->

## Prerequisites / recommended skill level

| Prerequisite        | Importance               | Notes  |
| -------------       | ----------               | ------ |
| [Reproducibility][] | Useful but not essential |        |
| [Open research][]   | Useful but not essential |        |

[Reproducibility]: /reproducibility/reproducibility.html
[Open research]: /open_research/open_research.html

1. [Summary](#summary)
2. [How this will help you/why this is useful?](#how-this-will-help-you-why-this-is-useful)
3. [Making it easy to cite your stuff](#making-it-easy-to-cite-your-stuff)
4. [How to cite data?](#how-to-cite-data)
5. [How to make software citeable?](#how-to-make-software-citeable)
6. [Making sure YOU get cited by using ORCID to increase your visibility](#making-sure-you-get-cited-by-using-orcid-to-increase-your-visibility)
7. [Checklist](#checklist)
<!--8. [What to learn next](#what-to-learn-next)-->
8. [Further reading](#further-reading)

## Summary

Reproducible research is great, but spending time on it will reduce the time you have available for activities by which researchers are traditionally measured, such as writing papers. 
But what if you could get credit for your reproducibility efforts as well?

## How this will help you/ why this is useful

Academic research is a reputation economy, and citations are the currency. 
Most research institutions' promotion and hiring criteria depend to a greater or lesser extent on your publishing record: how many articles you have published, how "important" the journals were, and how many times each article has been cited.

This is a well established practice, and while it has its problems at least all stakeholders understand what's involved. 
One of the consequences of this system is that labour which *doesn't* result in published articles tends to be ignored, discouraging researchers from making their data more open or specialising in software development.

Establishing good citation practice for non-article content is a step towards recognising this valuable work and encouraging more people to take it up. 
If you can demonstrate the impact of your reproducible research work in addition to more traditional research outputs, you can justify spending more time on doing things right.

## Making it easy to cite your stuff

There are many reasons why authors don't cite the data and software that they use, but one of the biggest ones is that it's not clear how. 
You can go a long way to reducing this barrier by following a few steps to make it as easy as possible.

### Open research

The first step is to ensure that you have something worth citing. 
Practising open research isn't essential to get credit for your data or software, but it makes it much easier for others to build on your work in a way that acknowledges your contribution. 
There is a growing body of evidence that shows open research tends to be cited more than non-open research of equivalent quality and significance.

<!-- TODO: Cite relevant paper for this (Piwowar et al 2013?) -->
Learn more about:

* [Making your research open][open research]
* [How to make your research FAIR][rdm]

[rdm]: /rdm/rdm.html

### Show people how to do it

Showing an example reference in the most common referencing format in your discipline serves two purposes:

1. It demonstrates that software & data are actually things that can be cited;
2. It gives authors a reference that they can copy and paste directly into their document.

If you use GitHub, GitLab or similar, consider creating a `CITATION` file in each repository containing an example reference.

### Make your research identifiable

As part of the citation for your software and data it is important to give people a persistent link to it, this will usually be a DOI.
DOIs (or more formally Digital Object Identifiers) are unique, persistent identifiers which are attached to a digital object such as a journal article, dataset or piece of software.
Using DOIs makes it much easier for others to cite your data, reduces the risk of linkrot and means you can track how your research is being used and cited.

### Add machine-readable referencing information

You can go one better by allowing people to import information about your research objects into their preferred referencing database.
If BibTeX is popular in your field, post a `.bib` file of *all* your outputs, not just your papers; if it's Endnote, make an Endnote export available.
If possible, provide several formats: you won't need to update these very often and it will pay off.

<!-- TODO: Information about cite.json(?) -->

### Publish in software & data journals

It's perfectly possible to cite a dataset or software package directly, and most major publishers now permit this in their style guides. 
However, it can sometimes help to have a more conventional paper to cite, and this is where software and data journals come in. 
These journals are similar to methods journals, in that they tend not to include significant results but instead focus on describing data and software in sufficient detail to allow reuse. Some examples include:

- [Journal of Open Research Software][jors]
- [Journal of Open Source Software][joss]

[JORS]: https://openresearchsoftware.metajnl.com/
[JOSS]: https://joss.theoj.org/

## How to cite data?

A dataset citation includes all of the same components as any other citation:
- Author
- Title
- Year of publication
- Publisher (for data, this is often the data repository where it is housed),
- Version (if indicated)
- Access information (a URL or DOI)

**APA citation style:** 
Author/Rightsholder. (Year). Title of data set (Version number). [Retrieved from https://] ***OR*** [DOI]

See also [this example](https://www.force11.org/node/4771) provided by FORCE11.

### Where to cite data in papers?

You should cite your dataset directly in the paper in places where it is relevant, just like publications, as well as in a **data availability statement** at the end of the paper (similar to the acknowledgement section). 
You can find examples of these statements in the publishers' (research data) author policies, or below:
    
### Data availability statement examples:
**Using the Digital Object Identifier (DOI):**
“The data that support the findings of this study are openly available in [repository name] at http://doi.org/[doi].”

**If no DOI is issued:** 
- “The data that support the findings of this study are openly available in [repository name] at [URL], reference number [reference number].”

**When there is an embargo period you can reserve your DOI and still include a reference to the dataset in your paper:**
- “The data that support the findings will be available in [repository name] at [URL / DOI] following a [6 month] embargo from the date of publication to allow for commercialisation of research findings.” 

**When data cannot be made available:**
- “Restrictions apply to the data that support the findings of this study. 
[Explain nature of restrictions, for example, if the data contains information that could compromise the privacy of research participants] Data are available upon reasonable request by contacting [name and contact details] and with permission of [third party name].” 
-  “The data that support the findings of this study are available upon request. 
Access conditions and procedures can be found at [URL to restricted access repository such as [EASY](https://easy.dans.knaw.nl/ui/home).]”

## How to make software citeable?

A software citation has a lot of the same elements as a data citation, described above, and are described in more detail in the [Software Citation Principles](https://www.force11.org/software-citation-principles). 
When using others software, it is vital to cite and attribute it properly. 

To make your code citeable, you can use the integration between [Zenodo](https://zenodo.org/) and GitHub. 
 
- Create a file to tell people how to cite your software. Use this [handy guide](https://citation-file-format.github.io/cff-initializer-javascript/) to format the file. 
- Link your GitHub account with a Zenodo account. This guide explains [how](https://guides.github.com/activities/citable-code/).  
- You can tell Zenodo what information or metadata you want to include with your software by adding a `zenodo.json` file, described [here](https://guide.esciencecenter.nl/citable_software/making_software_citable.html). 
- On Zenodo, flip the swith to the 'on' position for the GitHub repository you want to release
- On GitHub, click the *Create a new release* button. 
Zenodo should automatically be notified and should make a snapshot copy of the current state of your repository (just one branch, without any history), and should also assign a persistent identifier (DOI) to that snapshot.
- Use the DOI in any citations of your software and tell any collaborators and users to do the same!

## Making sure YOU get cited by using ORCID to increase your visibility

### What is ORCID?
- ORCID is short for ‘Open Researcher and Contributor iD'
- ORCID is a long lasting unique identifier for you as a researcher, comparable to a personal identification number that your government may issue to you.

You can watch this short video for more information https://vimeo.com/97150912

### Why should you get an ORCID?
- To distinguish yourself from others with the same or a similar name;
- To enable others to find all your outputs/related outputs so they can use and cite them
- All your outputs will remain linked to your unique identifier even if you change your name or your institute. This way, you only have to enter the information once.
- to access or sign up to services that utilise ORCID, for example publisher requirements, funding management portals ([ResearchFish](ResearchFish)), the [CRIS (current research information system)](https://en.wikipedia.org/wiki/Current_research_information_system) system at your institute, like the [Zenodo](https://zenodo.org) repository.
- you can add your ORCID to your CV/resume so that anyone can have a look at all your research outputs.

### How do you get an ORCID?
You can sign up very quickly here: https://orcid.org/login
Once you have signed up and verify your email address you can start adding in your outputs by importing them through [trusted organisations](https://support.orcid.org/hc/en-us/articles/360006973893) and [search and link wizards](https://support.orcid.org/hc/en-us/articles/360006973653-Add-works-by-direct-import-from-other-systems)


### When do you use your ORCID?
You can use your ORCID iD whenever you’re prompted to do so, give your [trusted organisations](https://support.orcid.org/hc/en-us/articles/360006973893) (funders, publishers, institutions) permission to automatically update your ORCID record.

<!-- TODO: more examples, especially data journals -->

<!-- TODO: deprecated practices such as citing an early paper or a software manual -->

<!--
- Making stuff citable
  - *Can this just link to other chapters mainly?*
  - Data
    - Deposit it
  - Software
    - Deposit it (github isn't good enough)
    - Software journals (like [JORS](https://openresearchsoftware.metajnl.com), [JOSS](https://joss.theoj.org))
- Citing stuff
  - Importance of using true citations
  - Different ways of citing
    - The data/software itself (preferred)
    - A data/software paper from a dedicated data/software journal
    - A key paper identified by the creator/developer
    - A software manual
  - What does/doesn't need to be cited
  - Overflow space for citations
-->

## Checklist

### For authors

- [ ] Pick out key datasets and software your conclusions rely on
- [ ] Cite data and software just like you would cite a paper
- [ ] Publish your own data/software and cite that too
- [ ] Get an ORCID ID!

### For data creators

- [ ] Deposit your data in a stable repository
- [ ] Get a persistent identifier (DOI) for your data
- [ ] Include an example citation in your dataset's README file

### For software developers

- [ ] Deposit key version snapshots of your software in a stable repository
- [ ] Get a distinct persistent identifier for each key version
- [ ] Include an example citation in your software manual

<!-- ## What to learn next -->

## Further reading

- [DataCite Citation Guidance](https://datacite.org/cite-your-data.html)
- [FAIR data principles](https://www.force11.org/group/fairgroup/fairprinciples)
- [FORCE11 Data Citation principles](https://www.force11.org/datacitationprinciples)
- [FORCE11 Software Citation principles](https://www.force11.org/software-citation-principles)
- [Getting Started with your ORCID record](https://support.orcid.org/hc/en-us/articles/360006896894-Getting-started-with-your-ORCID-record) 
- [Making software citeable](https://guide.esciencecenter.nl/citable_software/making_software_citable.html)
- [OpenAIRE Guide on Person Identifiers](https://www.openaire.eu/how-can-identifiers-improve-the-dissemination-of-your-research-outputs)

## Definitions/glossary

Digital Object Identifiers (DOIs) - an alpha-numeric string which acts as a unique, persistent identifier for a digital object (journal article, data, software and so on). 

<!-- ## Bibliography -->
