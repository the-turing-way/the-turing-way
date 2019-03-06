# What is reproducible science?

## Prerequisites / recommended skill level
No previous knowledge needed.

## Summary
There are several definitions of reproducibility in use.
This chapter will lay out why reproducibility is important for science and scientists, provide an overview of the most common definitions and define reproducibility for the context of this handbook.

## How this will help you/ why this is useful
This chapter sets out the definition of reproducibility that the Turing Way project team used when writing this handbook.
It will be useful to avoid misunderstandings when reading the rest of the handbook.

## Chapter content

### Why reproducibility is important for science

Major media outlets have [reported on](https://www.theguardian.com/science/2018/aug/27/attempt-to-replicate-major-social-scientific-findings-of-past-decade-fails) investigations that show that a significant percentage of scientific studies cannot be reproduced.  
This leads to other academics and society losing trust in scientific results. (Baker, 2016).
Working reproducibly means others can check your results - even early on in the research process.
Thus, the full analysis and methodology is transparent.
Scientific results and evidence are strenghtened if they are reproduced and confirmed by several indepedent researchers.
With all parts used in an analyses being available and/or documented, valuable time is saved reproducing published results and other researchers can easily build on these resarch results and re-use data or code for their analyses.
In addition, so called "negative results" can be published easily and avoid that other researchers waste time repeating analyses that will not return the expected results. (Dirnagl & Lauritzen, 2010)

### Why you should care about reproducibility

Markowetz highlights five reasons to work reprodubily (Markowetz, 2015):
- Avoiding disaster: Through working reproducibly, you can trust your own research results and will not have to retract published results or keep publications back because you cannot reproduce your results.
- Writing papers easier: well documented analyses ensure you have easy access to the latest results, your work can easily be written up and collaborators can easily get on board as additional authors.
Furthermore, you can be sure that you easily comply with the highest-level journal guidelines.
- Convincing reviewers: Making code and data available to the reviewers means their review comments will be constructive as they are able to develop an in-depth understanding of your work and can even try changes to your analysis themselves and see the impact.
- Facilitating continuity of work: Well documented work means your work can easily be picked up and continued - either by others in your lab or yourself if you want to build on your own work after a longer period.
- Building your reputation: Putting in effort to make your research reproducible shows that you are a careful researcher and makes your research results more robust.

Papers whose underlying data is available get cited more often (Piwowar, Day & Fridsma, 2007, Piwowar & Vision, 2013).
All research outputs that are shared can be built upon more easily by others and in some cases, others following up on your work might lead to new collaborations.
Other benefits of working openly are covered in our Open Science chapter.


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
![Kirstie's definition of reproducible research](https://github.com/pherterich/the-turing-way/blob/master/reproducibility_kirstie.png)
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
