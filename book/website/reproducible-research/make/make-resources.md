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

(rr-make-resources-glossary)=
## Glossary

**Makefile:** a text file that contains the configuration for the build

**Rule:** an element of the Makefile that defines something that must be
built, usually consists of *targets*, *recipes*, and optionally,
*prerequisites*.

**Target:** the outcome of a *rule* in a Makefile. It is usually a file. If it
is not a file, it's a *phony* target.

**Recipe:** one or more shell commands that are executed by Make. Usually
these commands update the *target* of the *rule*.

**Prerequisite:** the prerequisite(s) of a rule correspond to files or other
targets in the Makefile that must be up to date before the rule is run.

**Phony:** a phony target is one that doesn't correspond to a file on the
filesystem. A target is marked as phony by making it a prerequisite of the
``.PHONY`` target.

**Pattern:** A pattern rule is a rule that contains exactly one ``%``
character in the target, which can be used to match a part of a filename.

(rr-make-resources-appendix)=
## Appendix

(rr-make-resources-dag)=
### Directed Acyclic Graph

A Directed Acyclic Graph (DAG) is a *graph* of nodes and edges that is:

1. *directed*: edges have a direction and you can only walk the graph in that
   direction
2. *acyclic*: does not contain cycles: A can't depend on B when B depends on A.

The latter property is of course quite handy for a build system. More
information on DAGs can be found on
[Wikipedia](https://en.wikipedia.org/wiki/Directed_acyclic_graph).

(rr-make-resources-installing)=
### Installing Make

First, check if you have GNU Make installed already. In a terminal type:

```bash
$ make
```

If you get ``make: command not found`` (or similar), you don't have Make. If
you get ``make: *** No targets specified and no makefile found.  Stop.`` you
do have Make.

We'll be using **GNU Make** in this tutorial. Verify that this is what you
have by typing:

```bash
$ make --version
```

If you don't have GNU Make but have the BSD version, some things might not
work as expected and we recommend installing GNU Make.

To install GNU Make, please follow these instructions:

- **Linux**: Use your package manager to install Make. For instance on Arch
  Linux:

  ```bash
  $ sudo pacman -S make
  ```

  Ubuntu:
  ```bash
  $ sudo apt-get install build-essential
  ```

- **MacOS**: If you have [Homebrew](https://brew.sh/) installed, it's simply:

  ```bash
  $ brew install make
  ```

  If you have a builtin Make implementation, please ensure that it's GNU Make
  by checking ``make --version``.

(rr-make-resources-advanced-gr)=
### Advanced: Generating Rules using Call

*This section continues the tutorial above and demonstrates a feature of Make
for automatic generation of rules.*

In a data science pipeline, it may be quite common to apply multiple scripts
to the same data (for instance when you're comparing methods or testing
different parameters). In that case, it can become tedious to write a separate
rule for each script when only the script name changes. To simplify this
process, we can let Make expand a so-called [*canned*
recipe](https://www.gnu.org/software/make/manual/make.html#Canned-Recipes).

To follow along, switch to the ``canned`` branch:

```bash
$ make clean
$ git stash --all        # note the '--all' flag so we also stash the Makefile
$ git checkout canned
```

On this branch you'll notice that there is a new script in the **scripts**
directory called ``generate_qqplot.py``. This script works similarly to the
``generate_histogram.py`` script (it has the same command line syntax), but it
generates a [QQ-plot](https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot). The
**report.tex** file has also been updated to incorporate these plots.

After switching to the ``canned`` branch there will be a Makefile in the
repository that contains a separate rule for generating the QQ-plots. This
Makefile looks like this:

```makefile
# Makefile for analysis report
#

ALL_CSV = $(wildcard data/*.csv)
DATA = $(filter-out $(wildcard data/input_file_*.csv),$(ALL_CSV))
HISTOGRAMS = $(patsubst data/%.csv,output/figure_%.png,$(DATA))
QQPLOTS = $(patsubst data/%.csv,output/qqplot_%.png,$(DATA))

.PHONY: all clean

all: output/report.pdf

$(HISTOGRAMS): output/histogram_%.png: data/%.csv scripts/generate_histogram.py
	python scripts/generate_histogram.py -i $< -o $@

$(QQPLOTS): output/qqplot_%.png: data/%.csv scripts/generate_qqplot.py
	python scripts/generate_qqplot.py -i $< -o $@

output/report.pdf: report/report.tex $(FIGURES)
	cd report/ && pdflatex report.tex && mv report.pdf ../$@

clean:
	rm -f output/report.pdf
	rm -f $(HISTOGRAMS) $(QQPLOTS)
```

You'll notice that the rules for histograms and QQ-plots are very similar.

As the number of scripts that you want to run on your data grows, this may
lead to a large number of rules in the Makefile that are almost exactly the
same. We can simplify this by creating a [*canned
recipe*](https://www.gnu.org/software/make/manual/html_node/Canned-Recipes.html)
that takes both the name of the script and the name of the genre as input:

```makefile
define run-script-on-data
output/$(1)_$(2).png: data/$(2).csv scripts/generate_$(1).py
	python scripts/generate_$(1).py -i $$< -o $$@
endef
```

Note that in this recipe we use ``$(1)`` for either ``histogram`` or
``qqplot`` and ``$(2)`` for the genre. These correspond to the expected
function arguments to the ``run-script-on-data`` canned recipe. Also, notice
that we use ``$$<`` and ``$$@`` in the actual recipe, with two ``$`` symbols
for escaping. To actually create all the targets, we need a line that calls
this canned recipe.  In our case, we use a double for loop over the genres and
the scripts:

```makefile
$(foreach genre,$(GENRES),\
	$(foreach script,$(SCRIPTS),\
		$(eval $(call run-script-on-data,$(script),$(genre))) \
	) \
)
```

In these lines the ``\`` character is used for continuing long lines.

The full Makefile then becomes:

```makefile
# Makefile for analysis report
#

ALL_CSV = $(wildcard data/*.csv)
DATA = $(filter-out $(wildcard data/input_file_*.csv),$(ALL_CSV))
HISTOGRAMS = $(patsubst %,output/histogram_%.png,$(GENRES))
QQPLOTS = $(patsubst %,output/qqplot_%.png,$(GENRES))

GENRES = $(patsubst data/%.csv,%,$(DATA))
SCRIPTS = histogram qqplot

.PHONY: all clean

all: output/report.pdf

define run-script-on-data
output/$(1)_$(2).png: data/$(2).csv scripts/generate_$(1).py
	python scripts/generate_$(1).py -i $$< -o $$@
endef

$(foreach genre,$(GENRES),\
	$(foreach script,$(SCRIPTS),\
		$(eval $(call run-script-on-data,$(script),$(genre)))\
	)\
)

output/report.pdf: report/report.tex $(HISTOGRAMS) $(QQPLOTS)
	cd report/ && pdflatex report.tex && mv report.pdf ../$@

clean:
	rm -f output/report.pdf
	rm -f $(HISTOGRAMS) $(QQPLOTS)
```

Note that we've added a ``SCRIPTS`` variable with the ``histogram`` and
``qqplot`` names. If we were to add another script that follows the same
pattern as these two, we would only need to add it to the ``SCRIPTS``
variable.

To build all of this, run

```bash
$ make -j 4
```
