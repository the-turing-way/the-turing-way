# What is reproducible science?

## Prerequisites / recommended skill level
No previous knowledge needed.

## Summary
There are several definitions of reproducibility in use.
This chapter will lay out why reproducibility is important for science and scientists, provide an overview of the most common definitions and define reproducibility for the context of this handbook.

## How this will help you/ why this is useful
This chapter sets out the definition of reproducibility that the Turing Way project team used when writing this handbook.
It will be useful to avoid misunderstandings when reading the rest of the handbook.

***SUBSECTIONS PULLED OUT FROM HERE!***

### Definitions of reproducibility

The most common definition of reproducibility (and replication) was first noted by Claerbout and Karrenbach in 1992 and has been used in computational science literature since then.
Another popular definition has been introduced in 2013 by the Association for Computing Machinery (ACM) which swapped the meaning of the terms 'reproducible' and 'replicable' compared to Claerbout and Karrenbach.
The following table contrasts both definitions following Heroux et al. (2018).

| Term | Claerbout & Karrenbach | ACM |
| -----|------------------------|-----|
| Reproducible | Authors provide all the necessary data and the computer codes to run the analysis again, re-creating the results.| (Different team, different experimental setup.) The measurement can be obtained with stated precision by a different team, a different measuring system, in a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using artifacts which they develop completely independently. |
| Replicable |  A study that arrives at the same scientific findings as another study, collecting new data (possibly with different methods) and completing new analyses. | (Different team, same experimental setup.) The measurement can be obtained with stated precision by a different team using the same measurement procedure, the same measuring system, under the same operating conditions, in the same or a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using the author's own artifacts. |

Barba (2018) conducted a detailed literature review on the usage of reproducible/replicable covering several disciplines.
Most papers and disciplines use the terminology as defined by Claerbout and Karrenbach, whereas mircobiology, immunology and computer science tend to follow the ACM use of reproducibility and replication.
In political science and economics literature, both terms are used interchangeably.

In addition to these high level definitions of reporducibility, some authors provide more detailed disctinctions.
Victoria Stodden [(2014)](http://edge.org/response-detail/25340), a prominent scholar on this topic, has for example identified the following further distinctions:

- _Computational reproducibility_: when detailed information is provided about code, software, hardware and implementation details.

- _Empirical reproducibility_: when detailed information is provided about non-computational empirical scientific experiments and observations. In practise this is enabled by making data freely available, as well as details of how the data was collected.

- _Statistical reproducibility_: when detailed information is provided about the choice of statistical tests, model parameters, threshold values, etc. This mostly relates to pre-registration of study design to prevent p-value hacking and other manipulations.


### The Turing Way definition of reproducibility

The Turing Way project will define reproducible research as both data and code being available to fully rerun the analysis.

| ![Kirstie's definition of reproducible research](/assets/figures/reproducibility/ReproducibleMatrix.jpg) |
| -------------------------------------------------------------------------------------------------------- |
|  How the Turing Way defines reproducible research  |

However, we recognize that some research will use sensitive data that cannot be shared and this handbook will provide guides on how your research can be reproducible without all parts necessarily being open.
The handbook will cover:
* Version control (using git)
* Using GitHub/GitLab for collaboration
* Open Science
* Research Data Management
* Reproducible computing environments
* Testing
* Continous integration
* Various case studies
* Checklists to get you started on reproducible practices

## Checklist/Exercise
- [ ] define reproducibility for yourself

## What to learn next?
Open Science will be a good chapter to read next.
If you want to start learning hands-on practices, we recommend learning about version control next.

## Bibliography

* Baker, M. (2016). 1,500 scientists lift the lid on reproducibility. Nature, 533(7604), 452–454. https://doi.org/10.1038/533452a

* Barba, L. (2018). Terminologies for Reproducible Research, arXiv preprint: https://arxiv.org/abs/1802.03311

* Claerbout, J. F., & Karrenbach, M. (1992). Electronic documents give reproducible research a new meaning. In SEG Technical Program Expanded Abstracts 1992. Society of Exploration Geophysicists. https://doi.org/10.1190/1.1822162

* Dirnagl, U., & Lauritzen, M. (2010). Fighting Publication Bias: Introducing the Negative Results Section. Journal of Cerebral Blood Flow & Metabolism, 30(7), 1263–1264. https://doi.org/10.1038/jcbfm.2010.51

* Heroux, M. A., Barba, L., Parashar, M., Stodden, V., & Taufer, M. (2018). Toward a Compatible Reproducibility Taxonomy for Computational and Computing Sciences. Office of Scientific and Technical Information (OSTI). https://doi.org/10.2172/1481626

* Markowetz, F. (2015). Five selfish reasons to work reproducibly. Genome Biology, 16(1). https://doi.org/10.1186/s13059-015-0850-7

* Piwowar, H. A., Day, R. S., & Fridsma, D. B. (2007). Sharing Detailed Research Data Is Associated with Increased Citation Rate. PLoS ONE, 2(3), e308. https://doi.org/10.1371/journal.pone.0000308

* Piwowar, H. A., & Vision, T. J. (2013). Data reuse and the open data citation advantage. PeerJ, 1, e175. https://doi.org/10.7717/peerj.175

* Whitaker, Kirstie (2018): Barriers to reproducible research (and how to overcome them). figshare. Paper. https://doi.org/10.6084/m9.figshare.7140050.v2

## Additional material
### Videos

* Markowetz, F. (2016). 5 selfish reasons to work reproducibly. Talk at scidata 2016. https://www.youtube.com/watch?v=Is15CMVPHas&feature=youtu.be

### Recommended reading
* Barba, L. (2017): Barba-group Reproducibility Syllabus. figshare. Paper. https://doi.org/10.6084/m9.figshare.4879928.v1

### Other useful links
* Markowetz, F. (2018). 5 selfish reasons to work reproducibly. Slides available at https://osf.io/a8wq4/
