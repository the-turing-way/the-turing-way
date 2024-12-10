(rr-make-resources)=
# Resources for "Make"

(rr-make-resources-manual)=
## Manual

- [The Official Make Reference
  manual](https://www.gnu.org/software/make/manual/make.html).

(rr-make-resources-discussions)=
## Discussions

- [Discussion on Make on
  HackerNews](https://news.ycombinator.com/item?id=15041986).

- [Recursive Make Considered
  Harmful](http://aegis.sourceforge.net/auug97.pdf). This is a well-known
  paper on why you shouldn't use nested makefiles. To summarise: if you do
  this Make can't see the entire DAG and that leads to problems.

- [Non-Recursive Make Considered
  Harmful](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/03/hadrian.pdf):
  This is a research paper describing the failings of Make for large and
  complex builds.

(rr-make-resources-blogs)=
## Blogs

Of course we are not the first to suggest the use of Make for reproducibility!
The blog posts cited below were found after the above tutorial was written,
but can add further information and examples.

- [Reproducibility is
  hard](https://kbroman.wordpress.com/tag/reproducible-research/). Discusses
  making a research project reproducible using Make.

- [GNU Make for Reproducible Data Analysis](http://zmjones.com/make/). Argues
  for using Make for reproducible analysis in a similar vein as we do above.

- [Reproducible Bioinformatics Pipelines using
  Make](http://byronjsmith.com/make-bml/). A quite extensive tutorial on using
  Make for data analysis.

- [Automatic Data-analysis
  Pipelines](http://stat545.com/automation04_make-activity.html). A similar
  tutorial that uses R for the analysis.

- [Writing a reproducible Paper](http://handbook.datalad.org/en/latest/usecases/reproducible-paper.html#automation-with-existing-tools).
  A similar tutorial with Python using variables to populate tables in the
  manuscript.

(rr-make-resources-tools)=
## Tools

- Plot the DAG of the Makefile with
  [makefile2graph](https://github.com/lindenb/makefile2graph).

(rr-make-resources-alternatives)=
## Alternatives to Make

There are [many alternatives to
Make](https://en.wikipedia.org/wiki/List_of_build_automation_software). Below
are some that caught our eye and that might be worth a look.

- [SnakeMake](https://snakemake.readthedocs.io/en/stable/). A Python3-based
  alternative to Make. Snakemake supports multiple wildcards in filenames,
  supports Python code in rules, and can run workflows on workstations,
  clusters, the grid, and in the cloud without modification.

- [Tup](http://gittup.org/tup/index.html). A fast build system that processes
  prerequisites bottom-up instead of Make's top-down. The speed looks
  impressive and the paper describing it is interesting, but for small
  projects Make's speed will not be a bottleneck. The Tupfile syntax is not
  compatible with that of Makefiles.

- [Bazel](https://www.bazel.build). An open-source version of Google's Blaze
  build system.

- [Buck](https://buckbuild.com/). Facebook's build system.


