(rr-overview)=
# Overview of Reproducible Research

(rr-overview-prerequisites)=
## Prerequisites

No previous knowledge needed.

```{figure} ../../figures/research-cycle.*
---
name: research-cycle
alt: The research process is represented as a perpetual cycle of generating research ideas, performing data planning and design, data collection, and data processing and analysis, publishing, preserving and hence, allowing reuse of data.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

(rr-overview-summary)=
## Summary

Scientific results and evidence are strengthened if those results can be replicated and confirmed by several independent researchers (see {ref}`definitions <rr-overview-definitions>`).

When researchers employ transparency in their research - in other words, when they properly document and share the data and processes associated with their analyses - the broader research community is able to save valuable time when reproducing or building upon published results. 
Often, data or code from prior projects will be re-used by new researchers to verify old findings or develop new analyses. 

Learn about some of the other benefits of reproducible research in the {ref}`Added Advantages <rr-overview-benefits>` subchapter.

Major media outlets have [reported on](https://www.theguardian.com/science/2018/aug/27/attempt-to-replicate-major-social-scientific-findings-of-past-decade-fails) investigations showing that a significant percentage of scientific studies cannot be reproduced. This leads to other academics and society losing trust in scientific results {cite:ps}`baker2016reproducibility`. 

In addition, "negative results" can be published easily, helping avoid other researchers wasting time repeating analyses that will not return the expected results {cite:ps}`Dirnagl2010bias`.

For further reading resources on reproducibility, please check out the [Resources](#rr-overview-resources) subchapter.

***Chapter Tags**: This chapter is curated for the `Turing Data Study Group` (`turing-dsg`).*

The following example illustrates how a simple reproducible data science workflow can be structured in practice:
### Example: A Simple Reproducible Data Science Workflow

A reproducible data science workflow helps others understand, repeat, and verify a piece of work. A simple workflow might include the following steps:

1. **Data collection**
   - Store raw data in a dedicated folder such as `data/raw/`
   - Avoid modifying original data files directly

2. **Data processing**
   - Use scripts (for example, in Python or R) to clean and transform the data
   - Save outputs in a separate folder such as `data/processed/`

3. **Version control**
   - Track code and documentation changes using Git
   - Avoid committing large raw datasets where possible

4. **Analysis**
   - Run analysis in scripts or notebooks
   - Ensure the workflow can be executed from start to finish without manual intervention

5. **Environment management**
   - Record dependencies in files such as `requirements.txt` or `environment.yml`
   - This helps others recreate the same computational environment

6. **Documentation**
   - Include a README describing the project structure, how to run the analysis, and expected outputs

This kind of structure improves transparency, reproducibility, and collaboration in research workflows.
