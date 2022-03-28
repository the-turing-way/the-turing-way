(rr-make-casestudy-rp)=
# Case Study: Reproducible Paper using Make

In the tutorial above we used IMDB movie ratings for different genres as
example data. This data was obtained from a dataset [shared on
Kaggle](https://www.kaggle.com/orgesleka/imdbmovies#imdb.csv) as a CSV file.
The file looks like this:

```text
fn,tid,title,wordsInTitle,url,imdbRating,ratingCount,duration,year,type,nrOfWins,nrOfNominations,nrOfPhotos,nrOfNewsArticles,nrOfUserReviews,nrOfGenre,Action,Adult,Adventure,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,FilmNoir,GameShow,History,Horror,Music,Musical,Mystery,News,RealityTV,Romance,SciFi,Short,Sport,TalkShow,Thriller,War,Western
titles01/tt0012349,tt0012349,Der Vagabund und das Kind (1921),der vagabund und das kind,http://www.imdb.com/title/tt0012349/,8.4,40550,3240,1921,video.movie,1,0,19,96,85,3,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
titles01/tt0015864,tt0015864,Goldrausch (1925),goldrausch,http://www.imdb.com/title/tt0015864/,8.3,45319,5700,1925,video.movie,2,1,35,110,122,3,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
titles01/tt0017136,tt0017136,Metropolis (1927),metropolis,http://www.imdb.com/title/tt0017136/,8.4,81007,9180,1927,video.movie,3,4,67,428,376,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0
titles01/tt0017925,tt0017925,Der General (1926),der general,http://www.imdb.com/title/tt0017925/,8.3,37521,6420,1926,video.movie,1,1,53,123,219,3,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
```

While on the surface this looks like a regular CSV file, when you try to open
it with the Python CSV library, or Pandas, or R's ``read_csv``, or even
``readr:read_csv``, the data is not loaded correctly. This happens because the
CSV file uses an escape character ``\`` for movie names that have commas in
them and the CSV readers don't automatically detect this variation in the CSV
format.  It turns out that this is quite a common issue for data scientists:
CSV files are often messy and use an uncommon *dialect*: such as strange delimiters and
uncommon quote characters.  Collectively, data scientists waste quite
some time on these data wrangling issues where manual intervention is needed.
But this problem is also not that easy to solve: to a computer a CSV file is
simply a long string of characters and every dialect will give you *some*
table, so how do we determine the dialect accurately in general?

Recently, researchers from the Alan Turing Institute have presented a method
that achieves 97% accuracy on a large corpus of CSV files, with an improvement
of 21% over existing approaches on non-standard CSV files. This research was
made reproducible through the use of Make and is available through an online
repository:
[https://github.com/alan-turing-institute/CSV_Wrangling](https://github.com/alan-turing-institute/CSV_Wrangling).

Below we will briefly describe what the Makefile for such a project looks
like.  For the complete file, please see the repository. The Makefile consists
of several sections:

1. Data collection: because the data is collected from public sources, the
   repository contains a Python script that allows anyone to download the data
   through a simple ``make data`` command.

2. All the figures, tables, and constants used in the paper are generated
   based on the results from the experiments. To make it easy to recreate all
   results of a certain type, ``.PHONY`` targets are included that depend on
   all results of that type (so you could run ``make figures``). The rules for
   these outputs follow the same pattern as those for the figures in the
   tutorial above.  Tables are created as LaTeX files so they can be directly
   included in the LaTeX source for the manuscript.

3. The rules for the detection results follow a specific signature:

   ```makefile
   $(OUT_DETECT)/out_sniffer_%.json: $(OUT_PREPROCESS)/all_files_%.txt
   	python $(SCRIPT_DIR)/run_detector.py sniffer $(DETECTOR_OPTS) $< $@
   ```

   The ``%`` symbol is used to create outputs for both sources of CSV files
   with a single rule in {ref}`rr-make-examples-patternrules` and the rule 
   uses in {ref}`rr-make-examples-automaticvar` to extract the input and 
   output filenames.

4. Some of the cleaning rules will remove output files that take a while to
   create.  Therefore, these depend on a special ``check_clean`` target that
   asks the user to confirm before proceeding:

   ```makefile
   check_clean:
   	@echo -n "Are you sure? [y/N]" && read ans && [ $$ans == y ]
   ```

It is important to emphasize that this file was not created in one go, but was
constructed iteratively. The Makefile started as a way to run several dialect
detection methods on a collection of input files and gradually grew to include
the creation of figures and tables from the result files. Thus the advice for
using Make for reproducibility is to *start small and start early*.

The published Makefile in the repository does not contain the paper, but this
*is* included in the internal Makefile and follows the same structure as the
``report.pdf`` file in the tutorial above. This proved especially useful for
collaboration as only a single repository needed to be shared that contains
the code, the results, and the manuscript.
