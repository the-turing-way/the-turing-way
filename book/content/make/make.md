# Reproducible Research with Make

## Prerequisites / recommended skill level

| Prerequisite | Importance | Notes |
| ------------ | ---------- | ----- |
| [Experience with the command line](https://programminghistorian.org/en/lessons/intro-to-bash) | Necessary | |
| [Version control](/version_control/version_control) | Helpful | Experience using git is useful to follow along with examples |

Recommended skill level: intermediate

## Table of contents

- [Summary](#Summary)
- [An introduction to Make](#an_introduction_to_make)
  - [What is Make?](#What_is_make)
  - [Why use Make for reproducible research?]()
- [Learning Make by example]()
- [Example of a real reproducible paper with Make]()
- [Further reading]()
- [Definitions/glossary]()
- [Bibliography](#Bibliography)


## Summary

A research project can be seen as a tree of dependencies: the paper depends on 
the figures and tables, and these in turn depend on the data and the analysis 
scripts used to process this data. Make is a tool for creating output files 
from their dependencies through pre-specified rules. It is possible to combine 
these two ideas to create a reproducible research project with Make. In this 
chapter we give an introduction to Make and provide a tutorial on how Make can 
be used for a data analysis pipeline. We also describe a real-world 
reproducible research project that uses Make to go from the raw input data to 
the experiments all the way to the pdf file of the paper!

## An Introduction to Make

### What is Make

Make is a build automation tool. It uses a configuration file called a 
Makefile that contains the *rules* for what to build. Make builds *targets* 
using *recipes*.  Targets can optionally have *prerequisites*.  Prerequisites 
can be files on your computer or other targets. Make determines what to build 
based on the dependency tree of the targets and prerequisites (technically, 
this is a [directed acyclic graph](#directed-acyclic-graph)).  It uses the 
*modification time* of prerequisites to update targets only when needed.

### Why use Make for Reproducible Research?

There are several reasons why Make is a good tool to use for reproducible 
research:

1. Make is available on many platforms
2. Make is easy to learn
3. Makefiles are text files, which makes them easy share and keep in version 
   control.
4. Many people are already familiar with Make
5. Using Make doesn't exclude using other tools such as Travis, Docker, etc.

## Learn Make by Example

One of the things that might scare people off from using Make is that existing 
Makefiles can seem daunting and it may seem difficult to tailor to your own 
needs.  In this hands-on tutorial we will iteratively construct a Makefile for 
a real data analysis project. The idea is to explain different features of 
Make by iterating through several versions of a Makefile for this project. 
Hopefully the experience that you gain from this tutorial allows you to create 
Makefiles for your own projects.

### A Data Analysis Pipeline

We will create a ``Makefile`` for a data analysis pipeline. The task is as 
follows:

> **Task: Given some datasets, create a summary report (in pdf) that contains 
> the histograms of these datasets.**

(Of course this data task is very simple to focus on how to use Make.)

#### Setting up

To start, clone the base repository:

```bash
git clone https://github.com/GjjvdBurg/IntroToMake
```

This basic repository contains all the code that we'll need in this tutorial:

- **data**: directory with two datasets that we're going to analyse
- **report**: the input directory for the report
- **scripts**: directory for the analysis script
- **output**: output directory for the figures and the report

You'll notice that there are two datasets in the **data** directory 
(``input_file_1.csv`` and ``input_file_2.csv``) and that there is already a 
basic Python script in **scripts** and a basic report LaTeX file in 
**report**. Ensure that you have the ``matplotlib`` and ``numpy`` packages 
installed:

```bash
pip install [--user] matplotlib numpy
```

You will also need a working version of ``pdflatex`` and, of course, 
``make``.

#### Makefile no. 1 (The Basics)

Let's create our first Makefile. In the terminal, move into the 
``IntroToMake`` repository that you just cloned and, using your favorite 
editor, create a file called ``Makefile`` with the following contents:

```Makefile
# Makefile for analysis report

output/figure_1.png: data/input_file_1.csv scripts/generate_histogram.py
	python scripts/generate_histogram.py -i data/input_file_1.csv -o output/figure_1.png

output/figure_2.png: data/input_file_2.csv scripts/generate_histogram.py
	python scripts/generate_histogram.py -i data/input_file_2.csv -o output/figure_2.png

output/report.pdf: report/report.tex output/figure_1.png output/figure_2.png
	cd report/ && pdflatex report.tex && mv report.pdf ../output/report.pdf
```

To test that everything works correctly, you should now be able to type:

```bash
$ make output/report.pdf
```

If everything works correctly, the two figures will be created and pdf report 
will be built.

Let's go through the Makefile in a bit more detail. We have three rules, two 
for the figures and one for the report. Let's look at the rule for 
``output/figure_1.png`` first. This rule has the target 
``output/figure_1.png`` that has two prerequisites: ``data/input_file_1.csv`` 
and ``scripts/generate_histogram.py``. By giving the output file these 
prerequisites it will be updated if either of these files changes. This is one 
of the reasons why Make was created: to update output files when source files 
change.

You'll notice that the recipe line calls Python with the script name and uses 
command line flags (``-i`` and ``-o``) to mark the input and output of the 
script. This isn't a requirement for using Make, but it makes it easy to see 
which file is an input to the script and which is an output.

The rule for the PDF report is very similar, but it has three prerequisites 
(the LaTeX source and both figures). Notice that the recipe changes the 
working directory before calling LaTeX and also moves the generated PDF to the 
output directory. We're doing this to keep the LaTeX intermediate files in the 
report directory. However, it's important to distinguish the above rule from 
the following:

```Makefile
# don't do this
output/report.pdf: report/report.tex output/figure_1.png output/figure_2.png
        cd report/
        pdflatex report.tex
        mv report.pdf ../output/report.pdf
```

This rule places the three commands on separate lines. However, Make executes 
each line independently in a separate subshell, so changing the working 
directory in the first line has no effect on the second, and a failure in the 
second line won't stop the third line from being executed. Therefore, we 
combine the three commands in a single recipe above.

This is what the dependency tree looks like for this Makefile:

![DAG for Makefile no. 1](/assets/figures/make/makefile_no_1.png)


#### Makefile no. 2 (all and clean)

In our first Makefile we have the basic rules in place. We could stick with 
this if we wanted to, but there are a few improvements we can make:

1. We now have to explicitly call ``make output/report.pdf`` if we want to 
   make the report.

2. We have no way to clean up and start fresh.

Let's remedy this by adding two new targets: ``all`` and ``clean``. Again, 
open your editor and change the contents to add the ``all`` and ``clean`` 
rules:

```Makefile
# Makefile for analysis report

all: output/report.pdf

output/figure_1.png: data/input_file_1.csv scripts/generate_histogram.py
	python scripts/generate_histogram.py -i data/input_file_1.csv -o output/figure_1.png

output/figure_2.png: data/input_file_2.csv scripts/generate_histogram.py
	python scripts/generate_histogram.py -i data/input_file_2.csv -o output/figure_2.png

output/report.pdf: report/report.tex output/figure_1.png output/figure_2.png
	cd report/ && pdflatex report.tex && mv report.pdf ../output/report.pdf

clean:
        rm -f output/report.pdf
        rm -f output/figure_*.png
```

Note that we've added the ``all`` target to the top of the file. This is 
because Make executes the *first* target when no explicit target is given.  So 
you can now type ``make`` on the command line and it would do the same as 
``make all``. Also, note that we've only added the report as the prerequisite 
of ``all`` because that's our desired output and the other rules help to build 
that output. If you'd have multiple outputs, you could add these as further 
prerequisites to the ``all`` target.

The ``clean`` rule is typically at the bottom, but that's more style than 
requirement. Note that we use the ``-f`` flag to ``rm`` to stop it complaining 
when there is no file to remove.

You can try out the new Makefile by running:

```bash
$ make clean
$ make
```

#### Makefile no. 3 (Phony Targets)

Typically, ``all`` and ``clean`` are defined as so-called [Phony 
Targets](https://www.gnu.org/software/make/manual/make.html#Phony-Targets). 
These are targets that don't actually create an output file. Such targets will 
always be run if they come up in a dependency, but will no longer be run if a 
directory/file is created that is called ``all`` or ``clean``. We therefore 
add a line at the top of the Makefile so that it looks like this:

```Makefile
# Makefile for analysis report

.PHONY: all clean

all: output/report.pdf

output/figure_1.png: data/input_file_1.csv scripts/generate_histogram.py
	python scripts/generate_histogram.py -i data/input_file_1.csv -o output/figure_1.png

output/figure_2.png: data/input_file_2.csv scripts/generate_histogram.py
	python scripts/generate_histogram.py -i data/input_file_2.csv -o output/figure_2.png

output/report.pdf: report/report.tex output/figure_1.png output/figure_2.png
	cd report/ && pdflatex report.tex && mv report.pdf ../output/report.pdf

clean:
        rm -f output/report.pdf
        rm -f output/figure_*.pdf
```

Phony targets are also useful when you want to use Make recursively. In that 
case you would specify the subdirectories as phony targets. You can read more 
about [phony targets in the 
documentation](https://www.gnu.org/software/make/manual/make.html#Phony-Targets), 
but for now it's enough to know that ``all`` and ``clean`` are typically 
declared as phony.

> Sidenote: another target that's typically phony is **test**, in case you 
> have a directory of tests called **test** and want to have a target to run 
> them that's also called **test**.

<a name="makefile_auto_var_and_pat_rule">
#### Makefile no. 4 (Automatic Variables and Pattern Rules)

There's nothing wrong with the Makefile we have now, but it's somewhat verbose 
because we've declared all the targets explicitly using separate rules. We can 
simplify this by using [Automatic 
Variables](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html) 
and [Pattern 
Rules](https://www.gnu.org/software/make/manual/html_node/Pattern-Rules.html#Pattern-Rules). 

<a name="automatic_var">

**Automatic Variables.** With automatic variables we can use the names of the 
prerequisites and targets in the recipe. Here's how we would do that for the 
figure rules:

```Makefile
# Makefile for analysis report

.PHONY: all clean

all: output/report.pdf

output/figure_1.png: data/input_file_1.csv scripts/generate_histogram.py
        python scripts/generate_histogram.py -i $< -o $@

output/figure_2.png: data/input_file_2.csv scripts/generate_histogram.py
        python scripts/generate_histogram.py -i $< -o $@

output/report.pdf: report/report.tex output/figure_1.png output/figure_2.png
	cd report/ && pdflatex report.tex && mv report.pdf ../output/report.pdf

clean:
        rm -f output/report.pdf
        rm -f output/figure_*.pdf
```

We've replaced the input and output filenames in the recipes respectively by 
``$<``, which denotes the *first* prerequisite and ``$@`` which denotes the 
*target*. There are more automatic variables that you could use, see [the 
documentation](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html).

<a name="pattern_rules">

**Pattern Rules.** Notice that the figure recipes have become identical! 
Because we don't like to repeat ourselves, we can combine the two rules into a 
single one by using pattern rules. Pattern rules allow you to use the ``%`` 
symbol as a wildcard and combine the two rules into one:

```Makefile
# Makefile for analysis report

.PHONY: all clean

all: output/report.pdf

output/figure_%.png: data/input_file_%.csv scripts/generate_histogram.py
        python scripts/generate_histogram.py -i $< -o $@

output/report.pdf: report/report.tex output/figure_1.png output/figure_2.png
	cd report/ && pdflatex report.tex && mv report.pdf ../output/report.pdf

clean:
        rm -f output/report.pdf
        rm -f output/figure_*.pdf
```

The ``%`` symbol is now a wildcard that (in our case) takes the value ``1`` or 
``2`` based on the input files in the ``data`` directory. You can check that 
everything still works by running ``make clean`` followed by ``make``.


#### Makefile no. 5 (Wildcards and Path Substitution)

When Makefiles get more complex, you may want to use more "bash-like" features 
such as building outputs for all the files in an input directory. While 
pattern rules get you a long way, Make also has features for wildcards and 
string/path manipulation for when pattern rules are insufficient.

While before our input files were numbered, we'll now switch to a scenario 
where they have more meaningful names. Let's switch over to the ``big_data`` 
branch:

```bash
$ git stash                     # stash the state of your working directory
$ git checkout big_data         # checkout the big_data branch
```

If you inspect the **data** directory, you'll notice that there are now 
additional input files that are named more meaningfully (the data are IMBD 
movie ratings by genre). Also, the **report.tex** file has been updated to 
work with the expected figures.

We'll adapt our Makefile to create a figure in the output directory called 
``histogram_{genre}.png`` for each ``{genre}.csv`` file, while excluding the 
``input_file_{N}.csv`` files.

> Sidenote: if we were to remove the ``input_file_{N}.csv`` files, pattern 
> rules would be sufficient here. This highlights that sometimes your 
> directory structure and Makefile should be developed hand in hand.

Before changing the Makefile, run

```bash
$ make clean
```

to remove the output files.

First, we'll create a variable that lists all the CSV files in the data 
directory and one that lists only the old ``input_file_{N}.csv`` files:

```Makefile
ALL_CSV = $(wildcard data/*.csv)
INPUT_CSV = $(wildcard data/input_file_*.csv)
```

A code convention for Makefiles is to use full caps for variable names and 
define them at the top of the file.

Next, we'll list just the data that we're interested in by filtering out the 
``INPUT_CSV`` from ``ALL_CSV``:

```Makefile
DATA = $(filter-out $(INPUT_CSV),$(ALL_CSV))
```

This line uses the 
[``filter-out``](https://www.gnu.org/software/make/manual/make.html#index-filter_002dout) 
command to remove items in the ``INPUT_CSV`` variable from the ``ALL_CSV`` 
variable.  Note that we use both the ``$( ... )`` syntax for functions and 
variables (the ``${ ...  }`` syntax also works). Finally, we'll use the 
``DATA`` variable to create a ``FIGURES`` variable with the desired output:

```Makefile
FIGURES = $(patsubst data/%.csv,output/figure_%.png,$(DATA))
```

Here we've used the 
[``patsubst``](https://www.gnu.org/software/make/manual/make.html#index-patsubst-1) 
function to transform the input in the ``DATA`` variable (that follows the 
``data/{genre}.csv`` pattern) to the desired output filenames (using the 
``output/figure_{genre}.png`` pattern).

Now we can use these variables for the figure generation rule as follows:

```Makefile
$(FIGURES): output/figure_%.png: data/%.csv scripts/generate_histogram.py
        python scripts/generate_histogram.py -i $< -o $@
```

Note that this rule again applies a pattern: it takes a list of targets 
(``FIGURES``) that all follow a given pattern (``output/figure_%.png``) and 
based on that creates a prerequisite (``data/%.csv``). Such a pattern rule is 
slightly different from the one we saw before because it uses two ``:`` 
symbols. It is called a [static pattern 
rule](https://www.gnu.org/software/make/manual/make.html#Static-Pattern).

Of course we also have to update the ``report.pdf`` rule:

```Makefile
output/report.pdf: report/report.tex $(FIGURES)
	cd report/ && pdflatex report.tex && mv report.pdf ../$@
```

and the ``clean`` rule:

```Makefile
clean:
	rm -f output/report.pdf
	rm -f $(FIGURES)
```

The resulting Makefile should now look like this:

```Makefile
# Makefile for analysis report
#

ALL_CSV = $(wildcard data/*.csv)
INPUT_CSV = $(wildcard data/input_file_*.csv)
DATA = $(filter-out $(INPUT_CSV),$(ALL_CSV))
FIGURES = $(patsubst data/%.csv,output/figure_%.png,$(DATA))

.PHONY: all clean

all: output/report.pdf

$(FIGURES): output/figure_%.png: data/%.csv scripts/generate_histogram.py
	python scripts/generate_histogram.py -i $< -o $@

output/report.pdf: report/report.tex $(FIGURES)
	cd report/ && pdflatex report.tex && mv report.pdf ../$@

clean:
	rm -f output/report.pdf
	rm -f $(FIGURES)
```

If you run this Makefile, it will need to build 28 figures. You may want to 
use the ``-j`` flag to ``make`` to build these targets **in parallel!**

```bash
$ make -j 4
```

The ability to build targets in parallel is quite useful when your project has 
many dependencies.

## A Real Reproducible Paper using Make

In the tutorial above we used IMDB movie ratings for different genres as 
example data. This data was obtained from a dataset [shared on 
Kaggle](https://www.kaggle.com/orgesleka/imdbmovies#imdb.csv), through a CSV 
file. The file looks like this:

```text
fn,tid,title,wordsInTitle,url,imdbRating,ratingCount,duration,year,type,nrOfWins,nrOfNominations,nrOfPhotos,nrOfNewsArticles,nrOfUserReviews,nrOfGenre,Action,Adult,Adventure,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,FilmNoir,GameShow,History,Horror,Music,Musical,Mystery,News,RealityTV,Romance,SciFi,Short,Sport,TalkShow,Thriller,War,Western
titles01/tt0012349,tt0012349,Der Vagabund und das Kind (1921),der vagabund und das kind,http://www.imdb.com/title/tt0012349/,8.4,40550,3240,1921,video.movie,1,0,19,96,85,3,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
titles01/tt0015864,tt0015864,Goldrausch (1925),goldrausch,http://www.imdb.com/title/tt0015864/,8.3,45319,5700,1925,video.movie,2,1,35,110,122,3,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
titles01/tt0017136,tt0017136,Metropolis (1927),metropolis,http://www.imdb.com/title/tt0017136/,8.4,81007,9180,1927,video.movie,3,4,67,428,376,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0
titles01/tt0017925,tt0017925,Der General (1926),der general,http://www.imdb.com/title/tt0017925/,8.3,37521,6420,1926,video.movie,1,1,53,123,219,3,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
```

While on the surface this looks like a regular CSV file, when you try to open 
it with the Python CSV library, or Pandas, or R's ``read_csv``, or even 
``readr:read_csv``, the data is not loaded correctly. It turns out that the 
CSV file uses an escape character ``\`` when movie names have commas in them 
and the CSV readers can't detect this variation in the CSV format.  It turns 
out that this is quite a common issue for data scientists: CSV files are often 
messy and use an uncommon *dialect*: a strange delimiter, uncommon quote 
characters, etc. Collectively, data scientists waste quite some time on these 
data wrangling issues where manual intervention is needed.  However, this 
problem is also not that easy to solve: to a computer a CSV file is simply a 
long string of characters, so how do we determine the dialect accurately in 
general?

Recently, researchers from the Alan Turing Institute have presented a method 
that achieves 97% accuracy on a large corpus of CSV files, with an improvement 
of 21% over existing approaches on non-standard CSV files. This research was 
made reproducible through the use of Make and is available through an online 
repository: 
[https://github.com/alan-turing-institute/CSV_Wrangling](https://github.com/alan-turing-institute/CSV_Wrangling).

Below we will briefly describe what the Makefile for such a project looks 
like. For the complete file, please see the repository. The Makefile consists 
of several sections:

1. Data collection: because the data is collected from public sources, the 
   repository contains a Python script that allows anyone to download the data 
   through a simple ``make data`` command.

2. All the figures, tables, and constants used in the file are generated based 
   on the results from the experiments. To make it easy to recreate all 
   results of a certain type, ``.PHONY`` targets are included that depend on 
   all results of that type. The rules for these outputs follow the same 
   pattern as those for the figures in the tutorial above. Tables are created 
   as LaTeX files so they can be directly included in the LaTeX source for the 
   manuscript.

3. The rules for the detection results follow a specific signature:

   ```Makefile
   $(OUT_DETECT)/out_sniffer_%.json: $(OUT_PREPROCESS)/all_files_%.txt
           python $(SCRIPT_DIR)/run_detector.py sniffer $(DETECTOR_OPTS) $< $@
   ```

   The ``%`` symbol is used to create outputs for both sources of CSV files 
   with a single rule (see [Pattern Rules](#pattern_rules)) and the rule uses 
   [automatic variables](#automatic_var) to extract the input and output 
   filenames.

4. Some of the cleaning rules remove output files that take a while to create. 
   Therefore, these depend on a special ``check_clean`` target that asks the 
   user to confirm before proceeding:

   ```Makefile
   check_clean:
        @echo -n "Are you sure? [y/N]" && read ans && [ $$ans == y ]
   ```

It is important to emphasize that this file was not created in one go, but was 
constructed iteratively. The file started as a way to run several dialect 
detection methods on a collection of input files and gradually grew to include 
the creation of figures and tables from the result files. Thus the advice for 
using Make for reproducible research is to start small and to start using Make 
early.

The published Makefile in the repository does not contain the paper, but this 
*is* included in the internal Makefile and follows the same structure as the 
``report.pdf`` file in the tutorial above. This proved especially useful for 
collaboration as only a single repository needed to be shared that contains 
the code, the results, and the manuscript.

## Further Reading

### Sites and Tools

- [Recursive Make Considered 
  Harmful](http://aegis.sourceforge.net/auug97.pdf). This is a well-known 
  paper on why you shouldn't use nested makefiles. To summarise: if you do 
  this Make can't see the entire DAG and that leads to problems.

- [Non-Recursive Make Considered 
  Harmful](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/03/hadrian.pdf): 
  This is a research paper describing the failings of Make for large and 
  complex builds.

- [Discussion on HN on Make](https://news.ycombinator.com/item?id=15041986).

- Plot the DAG of the Makefile with 
  [makefile2graph](https://github.com/lindenb/makefile2graph).

### Alternatives to Make

I'm not explicitly recommending any of these, but if you want features that 
Make doesn't support or have a really big project with complex dependencies, 
then here are some alternatives.  I would recommend not to optimise your build 
system until you run into a problem with your current one. Optimising your 
build system might lead you down to a rabbit hole that ends up taking more 
time than the slow builds!

- [Bazel](https://www.bazel.build): An open-source version of Google's Blaze 
  build system.

- [Buck](https://buckbuild.com/): Facebook's build system.

- [Tup](http://gittup.org/tup/index.html): a fast build system that processes 
  prerequisites bottom-up instead of Make's top-down. The speed looks 
  impressive and the paper describing it is interesting. Would have been great 
  if it could be run on Makefiles too instead of requiring a Tupfile with 
  different syntax.

- [Walk](https://github.com/ejholmes/walk): Make alternative that claims to be 
  more flexible than Make because it doesn't just rely on modification time. 
  Makefile is now essentially a bash script.

## Definitions/Glossary

## Bibliography

## Appendix

### Directed Acyclic Graph

A Directed Acyclic Graph (DAG) is a *graph* of nodes and edges that is:

1. *directed*: edges have a direction and you can only walk the graph in that 
   direction
2. *acyclic*: does not contain cycles: A can't depend on B when B depends on A.

The latter property is of course quite handy for a build system. More on DAGs 
on [Wikipedia](https://en.wikipedia.org/wiki/Directed_acyclic_graph).

### Installing Make

First check if you have GNU Make installed already. In a terminal type:

```bash
$ make
```
If you get ``make: command not found`` (or similar), you don't have make. If 
you get ``make: *** No targets specified and no makefile found.  Stop.`` you 
do have make.

We'll be using **GNU Make** in this tutorial. Verify that this is what you 
have by typing:

```bash
$ make --version
```

If you don't have GNU make but have the BSD version, some things might not 
work as expected.

To install GNU Make, please follow these instructions:

- **Linux**: Use your package manager to install Make. For instance on Arch 
  Linux:

  ```bash
  $ pacman -S make
  ```

  Ubuntu:
  ```bash
  $ sudo apt-get install build-essential
  ```

- **MacOS**: If you have [Homebrew](https://brew.sh/), it's simply:

  ```bash
  $ brew install make
  ```

  If you have a builtin Make implementation, please ensure that it's GNU make 
  by checking ``make --version``.

