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
4. [Checklist](#checklist)
5. [What to learn next](#what-to-learn-next)
6. [Further reading](#further-reading)

## Summary

Reproducible research is great, but spending time on it will reduce the time you have available for activities by which researchers are traditionally measured, such as writing papers. But what if you could get credit for your reproducibility efforts as well?

## How this will help you/ why this is useful

Academic research is a reputation economy, and citations are the currency. Most research institutions' promotion and hiring criteria depend to a greater or lesser extent on your publishing record: how many articles you have published, how "important" the journals were, and how many times each article has been cited.

This is a well established practice, and while it has its problems at least all stakeholders understand what's involved. One of the consequences of this system is that labour which *doesn't* result in published articles tends to be ignored, discouraging researchers from making their data more open or specialising in software development.

Establishing good citation practice for non-article content is a step towards recognising this valuable work and encouraging more people to take it up. If you can demonstrate the impact of your reproducible research work in addition to more traditional research outputs, you can justify spending more time on doing things right.

## Making it easy to cite your stuff

There are many reasons why authors don't cite the data and software that they use, but one of the biggest ones is that it's not clear how. You can go a long way to reducing this barrier by following a few steps to make it as easy as possible.

### Open research

The first step is to ensure that you have something worth citing. Practising open research isn't essential to get credit for your data or software, but it makes it much easier for others to build on your work in a way that acknowledges your contribution. There is a growing body of evidence that shows open research tends to be cited more than non-open research of equivalent quality and significance.

<!-- TODO: Cite relevant paper for this (Piwowar et al 2013?) -->

* [Learn more about making your research open][open research]

### Show people how to do it

Showing an example reference in the most common referencing format in your discipline serves two purposes:

1. It demonstrates that software & data are actually things that can be cited;
2. It gives authors a reference that they can copy and paste directly into their document.

<!-- TODO: insert example citation in suitable format -->
<!-- TODO: link to DataCite data citation guidance -->

If you use GitHub, GitLab or similar, consider creating a `CITATION` file in each repository containing an example reference.

### Add machine-readable referencing information

You can go one better by allowing people to import information about your research objects into their preferred referencing database.
If BibTeX is popular in your field, post a `.bib` file of *all* your outputs, not just your papers; if it's Endnote, make an Endnote export available.
If possible, provide several formats: you won't need to update these very often and it will pay off.

<!-- TODO: Information about cite.json(?) -->

### Publish in software & data journals

It's perfectly possible to cite a dataset or software package directly, and most major publishers now permit this in their style guides. However, it can sometimes help to have a more conventional paper to cite, and this is where software and data journals come in. These journals are similar to methods journals, in that they tend not to include significant results but instead focus on describing data and software in sufficient detail to allow reuse. Some examples include:

- [Journal of Open Research Software][jors]
- [Journal of Open Source Software][joss]

[JORS]: https://openresearchsoftware.metajnl.com/
[JOSS]: https://joss.theoj.org/

<!-- TODO: more examples, especially data journals -->

<!-- TODO: deprecated practices such as citing an early paper or a software manual -->

<!--
- Making stuff citable
  - *Can this just link to other chapters mainly?*
  - Data
    - Deposit it
  - Software
    - Deposit it (github isn't good enough)
    - Software journals (e.g. [JORS][], [JOSS][])
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

- Pick out key datasets and software your conclusions rely on
- Cite data and software just like you would cite a paper
- Publish your own data/software and cite that too!

### For data creators

- Deposit your data in a stable repository
- Get a persistent identifier (DOI) for your data
- Include an example citation in your dataset's README file

### For software developers

- Deposit key version snapshots of your software in a stable repository
- Get a distinct persistent identifier for each key version
- Include an example citation in your software manual

<!-- ## What to learn next -->

## Further reading

- [FAIR data principles](https://www.force11.org/group/fairgroup/fairprinciples)
- [FORCE11 Software Citation principles](https://www.force11.org/software-citation-principles)

<!-- ## Definitions/glossary -->

<!-- ## Bibliography -->
