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
### Single-button reproducibility and workflow automation

The concept of *single-button reproducibility* was introduced by Claerbout and Karrenbach in the early 1990s. The idea is that a complete analysis—from raw data to final figures, tables, and results—should be reproducible by running a single command or script. This allows another researcher (or even your future self) to regenerate the results without needing to manually follow many steps or guess missing details.

A workflow may still be considered reproducible even if it includes many instructions, but manual processes are difficult to repeat reliably. They are rarely tested end-to-end during the research process, and it is easy to forget small steps or apply them inconsistently. Even well-written documentation cannot prevent human error.

Automating workflows reduces these risks. When processing steps are scripted or handled by tools such as Make, Snakemake, Nextflow, or R Markdown, each run is identical, repeatable, and testable. Automation also improves efficiency: once a workflow is defined, updating and regenerating results becomes faster and less error-prone. This makes reproducibility a natural part of the research process, rather than a separate task performed only at the end of a project.


Scientific results and evidence are strengthened if those results can be replicated and confirmed by several independent researchers (see {ref}`definitions <rr-overview-definitions>`).

When researchers employ transparency in their research - in other words, when they properly document and share the data and processes associated with their analyses - the broader research community is able to save valuable time when reproducing or building upon published results. 
Often, data or code from prior projects will be re-used by new researchers to verify old findings or develop new analyses. 

Learn about some of the other benefits of reproducible research in the {ref}`Added Advantages <rr-overview-benefits>` subchapter.

Major media outlets have [reported on](https://www.theguardian.com/science/2018/aug/27/attempt-to-replicate-major-social-scientific-findings-of-past-decade-fails) investigations showing that a significant percentage of scientific studies cannot be reproduced. This leads to other academics and society losing trust in scientific results {cite:ps}`baker2016reproducibility`. 

In addition, "negative results" can be published easily, helping avoid other researchers wasting time repeating analyses that will not return the expected results {cite:ps}`Dirnagl2010bias`.

For further reading resources on reproducibility, please check out the [Resources](#rr-overview-resources) subchapter.

***Chapter Tags**: This chapter is curated for the `Turing Data Study Group` (`turing-dsg`).*
