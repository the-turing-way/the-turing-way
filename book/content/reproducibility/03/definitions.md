# Definitions of reproducibility

The most common definition of reproducibility (and replication) was first noted by Claerbout and Karrenbach in 1992 and has been used in computational science literature since then.
Another popular definition has been introduced in 2013 by the Association for Computing Machinery (ACM), which swapped the meaning of the terms 'reproducible' and 'replicable' compared to Claerbout and Karrenbach.
The following table contrasts both definitions following Heroux et al. (2018).

| Term | Claerbout & Karrenbach | ACM |
| -----|------------------------|-----|
| Reproducible | Authors provide all the necessary data and the computer codes to run the analysis again, re-creating the results.| (Different team, different experimental setup.) The measurement can be obtained with stated precision by a different team, a different measuring system, in a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using artifacts which they develop completely independently. |
| Replicable |  A study that arrives at the same scientific findings as another study, collecting new data (possibly with different methods) and completing new analyses. | (Different team, same experimental setup.) The measurement can be obtained with stated precision by a different team using the same measurement procedure, the same measuring system, under the same operating conditions, in the same or a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using the author's own artifacts. |

Barba (2018) conducted a detailed literature review on the usage of reproducible/replicable covering several disciplines.
Most papers and disciplines use the terminology as defined by Claerbout and Karrenbach, whereas mircobiology, immunology and computer science tend to follow the ACM use of reproducibility and replication.
In political science and economics literature, both terms are used interchangeably.

In addition to these high level definitions of reproducibility, some authors provide more detailed disctinctions.
Victoria Stodden [(2014)](http://edge.org/response-detail/25340), a prominent scholar on this topic, has for example identified the following further distinctions:

- _Computational reproducibility_: When detailed information is provided about code, software, hardware and implementation details.

- _Empirical reproducibility_: When detailed information is provided about non-computational empirical scientific experiments and observations. In practice this is enabled by making data freely available, as well as details of how the data was collected.

- _Statistical reproducibility_: When detailed information is provided, for example, about the choice of statistical tests, model parameters, and threshold values. This mostly relates to pre-registration of study design to prevent p-value hacking and other manipulations.

## The Turing Way definition of reproducibility

The Turing Way project will define reproducible research as both data and code being available to fully rerun the analysis.

| ![Kirstie's definition of reproducible research](../../figures/reproducibility/ReproducibleMatrix.jpg) |
| -------------------------------------------------------------------------------------------------------- |
|  How the Turing Way defines reproducible research  |

However, we recognize that some research will use sensitive data that cannot be shared and this handbook will provide guides on how your research can be reproducible without all parts necessarily being open.

The handbook will cover:
* Open research
* Version control (using git)
* Collaborating on GitHub/GitLab
* Credit for reproducible research
* Research data management
* Reproducible environments
* Testing
* Reviewing
* Continuous integration
* Reproducible research with make
* Risk assessments
* Various case studies
* Checklists to get you started on reproducible practices
