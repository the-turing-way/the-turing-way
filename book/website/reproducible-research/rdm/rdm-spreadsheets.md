(rr-rdm-spreadsheets)=
# Using spreadsheets for research data

Spreadsheets, such as Microsoft Excel files, google sheets, and their Open Source alternative [(for instance) LibreOffice](https://www.libreoffice.org), are commonly used to collect, store, manipulate, analyse, and share research data.
Spreadsheets are convenient and easy-to-use tools for organising information into an easy to write and easy to read forms for humans. 
However, one should use them with caution, as the use of an inappropriate spreadsheet is a major cause of mistakes in the data analysis workflow.
There is a collection of [horror-stories](http://www.eusprig.org/horror-stories.htm) that tells how the use of spreadsheets can ruin analysis-based studies due to unexpected behaviour of the spreadsheet or error-prone
editing processes.
Some of these mishaps are not unique to spreadsheets, but many, such as [this](https://doi.org/10.1186/s13059-016-1044-7) and [this](https://doi.org/10.1186/1471-2105-5-80), are.

Most problems can be avoided with the recommendations described below: 
- use spreadsheet in a text-only format (.csv or .tsv)
- create tidy spreadsheets
- make spreadsheets consistent (with each other) and implement rules for data entries.
- and avoid manipulating and analysing data in spreadsheet software (this includes copy-paste). 

Spreadsheets are a powerful tool only if the dataset is collected and organised in specific formats that are usable for both the computers and researchers.

## 1. Avoid Non-data content

Spreadsheets are used for organising data in a tabular form. 
The subject, the object and the relationship between them are transformed into rows, cells and columns respectively.
For example, the subject: `experiment`, relationship: `was performed on the date`, the object: `2020-06-06` gives one row for each experiment, one column for `date of experiment` and the value `2020-06-06` in the cell. 
Unfortunately for data science, the spreadsheets program allows you to add other kinds of contents to this, like adding color to specific cells. 
While it may help the researchers at some point, one needs to remember that this kind of **cell modification should not be considered as data**, especially since they cannot be exported to other software.

As a simple rule, what can be exported in a text-only format, comma-separated values (CSV) or tab-separated values (TSV), can be considered as the data, other functions should be avoided when using these programs for research data. 
This includes: 
- changing font, color or borders,
- using functions, 
- merging cells (this one is particularly problematic), 
- using specific cell formats (especially dates, see below). 

As a test for your spreadsheet compatibility with reproducible research, export your data from the spreadsheet to the CSV format and reopen it.
If you can still get all the information that you stored in your sheet, then your data is fine.

```
Tip: If you want to use color to help with a rapid highlight in your document, create a new column to indicate which cells are highlighted (it becomes a part of your data).
In addition to the visual feedback, you can now also use this information to filter or sort your data and get the highlighted cells quickly.

```

## 2. Tidy format for spreadsheets

If the spreadsheet is poorly organised then it may be [difficult for collaborators](https://luisdva.github.io/pls-don't-do-this/) to easily [read-in and re-use](#FAIR) your
data for further analysis.

Indeed, a large part of the work of data scientists is to transform the data into a form that the computer can read. 
This is particularly time-consuming when the information is split between several spreadsheets and that no plan was made before data acquisition.

There are very simple rules to facilitate data use, which go into the concept of [**tidy data**](https://en.wikipedia.org/w/index.php?title=Tidy_data&oldid=962241815). 
Furthermore, this specific format also allows for filtering and sorting data easily in spreadsheet software. 
In short:

- one column = one variable (no more, no less, this implies that two header names can not be identical)
- one row = one sample
- one cell = one information
- **the first row is the header** 
- Headers name: do not include a special character (including space), do not start with a number

| ![tidy table figure](../../figures/tidy-1.png)         |
| ------------------------------------------------------------------------------------ |
Three rules which make a dataset tidy:
1. Each variable must have its own column.
2. Each observation must have its own row.
3. Each value must have its own cell.

There are data validation tools available, like https://goodtables.io, that allows you to check automatically whether your spreadsheets are tidy.

## 3. Consistent values

When you work with several spreadsheets or with a team during data collection, it is very important to make sure the same information will be entered with the same term, and the same term always conveys the same information. 
In the example of iris data, if some people use different terms to record information for a specific column, such as naming the column `species` instead of `Species` or using `iris setosa`, `set.` or `i.setosa` instead of `setosa`, the creation of a reproducible workflow will be more difficult and errors may even be overlooked.  
Discrepancies often lead to errors, especially when the same terms could mean different things depending on who is entering the data. 
For example, indicating date as 02-03 will mean February the third in the USA, but March the second in Europe.

It is good practice to implement a `data dictionary` or a `taxonomy` of accepted terms and to document the convention used in a README file.
Depending on the software you are using, you may be able to restrict the accepted values in specific columns.
If there is such a taxonomy or ontology available, using it may allow you (and others) to use the data in conjunction with other datasets.
For example, use the generic `male` and `female` terms for the sex of animal (without capitals, and without using abbreviation), as many ontologies use these terms.
Besides, you may want to use some extra tools to validate the spreadsheets before its integration in the analysis.

You should also have clear rules about missing data points, using `NA`, `NULL`, and/or empty cells is not trivial and may have different meanings (impossible data point, not recorded, or lost data point). 
Let's imagine, one would record the time spent before seeing the first pollinator landing on the iris flower measured previously, and that no pollinator was seen during the 5 minutes experiment.
If one reports `600` (the duration of the experiment in seconds), there will be no way to distinguish a case where no pollinator was seen, and one when one was seen at the end of the experiment (and you may forget that rule and treat 600 as a normal value).
If `NA` is reported, one may interpret this value as a non-existing data point (the experiment had not been performed).
An elegant solution is to have a second column stating whether a pollinator was seen during the experiment, where `TRUE`, `FALSE` and `NA` values are accepted.

Finally, you should also be aware of the default behaviour of your spreadsheet program, as it may be different for different programs, and different versions of the same program.
For instance, the decimal is usually indicated with a comma in the French or German version of excel, but while a dot in English versions where the comma has no meaning
(`9,000`  will be translated into 9000 or 9 depending on the version you are using).

## 4. Data manipulation and analysis

***Do not manipulate or analyse data in a spreadsheet program.***

In particular, only copy-paste from one spreadsheet to another if the process is used very rarely. 
It is now very easy to read and combine the different spreadsheets in the analysis software, with the additional advantage that the software will return an error message if the headers do not fit.

## Other tips

### Deal with time information

While dates should be written as yyyy-mm-dd, excel and other software tend to transform this data into their own format for dates (even during data import from a CSV file). 
The only 100% secure way to deal with this is to make different columns for years, months, and days and recreate the data in the software used for analysis. Time entered with hh:mm:ss normally works.

### Working with several sheets

We often use several sheets for different but related data. 
It is a very useful tool indeed, especially when one wants to share the complete dataset with colleagues. 
On the other hand, CSV files only save one sheet at a time. 
Though most data analysis software has several ways to import xlsx files, the practical solution is to work with the xlsx format while making sure that the information is available in CSV format for each sheet. 
A better solution, especially for long term storage, is to save all sheets separately in a CSV file and zip them together. 
This latter solution allows containing also extra documentation that could be in a different format (for example a text file explaining the meaning of the headers and the unit chosen).

### Spreadsheet design

Data is often collected manually, on paper.
To avoid mistakes and be most efficient in this case, it is best to collect the data in the same format as it will be digitalised, that is one should design the computer-readable spreadsheet to be printed for data collection.
This poses some design questions, especially for information which are unique for one experiment (one paper), but changes between experiments (for example, experimentalist or temperature of the room).
You indeed want that information into one column, but you would like to enter it only once during data acquisition (especially on the paper version).
One solution is to move these columns on a second (Non-printed) page on the spreadsheet and playing with the headers and footers to enter the information on the paper version.
One needs to make sure the information is indeed entered in the column during digitalisation.

The way you enter the information (that is the way you design your headers and cell content) may be different depending on the analysis you want to perform later.
One should still always try to be as generic and objective as possible, and think about additional analysis one may want to perform. 
The way you enter the information (that is the way you design your headers and cell content) may be different depending on the analysis you want to perform later. One should still always try to be as generic and objective as possible, and think about additional analysis one may want to perform. 

As an example, let's suppose you are interested in depicting if the percentage of flowers whose sepal length is longer than 6 mm is different in three iris species.
You may be inclined to record a true or false column `is-sepal-longer-than-6cm`, but this will restrict the analysis you can perform.
A better solution is to record the length of the sepal (in mm) and create automatically the categorization later.

If you are using R, you would then plot what you wanted with:
```
iris %>% ## the iris dataset is included in R base
  dplyr::mutate ("is-sepal-longer-than-6cm" = ifelse(Sepal.Length >6, TRUE, FALSE)) %>% ## this create the new column
  ggplot2::ggplot (aes (x=`is-sepal-longer-than-6cm` , fill= Species)) + ggplot2::geom_bar() ## this plots the data
```

Headers names should be chosen with care, and when it is not clear what is meant and what unit is used, you may want to add some explanation in an external document. 
You may also share a sample spreadsheet to a colleague to receive feedback on how understandable your sheet is.

An alternative way is to put some explanations on the top of the sheet in the first rows before the headers.
By keeping human-readable information at the top of the file, one can better understand the data that starts in a row with the header.
This information can also help in analysing that data making sure that the scripts ignore the explanation lines and consider the explanation during analysis.
However, a good file with tidy columns and rows should not need extra explanation.

As for file name, the size of the headers is not an issue for computers, but for human readability, it might be better to keep it short (up to 32 characters).

You do not have to think about the order of the columns for the analysis, as it has no importance for data analysis software. 
You can therefore completely optimise that parameter for the data collection step.

### Standard and versioning

A good spreadsheet design has instructive and intuitive header names, and it facilitates both data collection and analysis. 
Building such a spreadsheet design is difficult as it takes time, multiple iterations, and consensus. 
It is therefore very useful to look for a standard spreadsheet before designing your own, and share your design openly once you created yours. 
One should also use a version history of the spreadsheets (as they will evolve over time) and the analysis script should mention the version number of the spreadsheet. 
Documentation of the spreadsheet, its version history, and the ontologies it is linked to, can be useful for future users. 

### Working in a team: wrap-up

If you are working with a team on data collection, make sure:
- everyone is using the same software (and software version) to enter the data.
- everyone is using the same version of the spreadsheet template.
- everyone understands what each column represents, and the unit that should be used.
- every column has a defined standard on how to enter data in it or taxonomy of terms that one can use.
- One person is responsible to answer putative questions during data collection.
- every spreadsheet is validated before entering the analysis workflow, and as soon as possible.



## Summary

While spreadsheets can be a very user-friendly way to collect and share data, they can also be the source of mistakes if used inappropriately. 
When aiming at developing a reproducible workflow for analyses, one should design the spreadsheet for both computer and human readability, and even before starting data collection, they should consider what makes their data analysis easy. 
Data manipulation and analysis in spreadsheets, in particular, is best avoided as it leads to non-reproducible workflows. 
Using version control and making the data read-only are two additional data management practices that can prevent accidents.

Use a README file to explain naming conventions and other design choices on top of the spreadsheet.
It will make it clear to others what the file names mean and what criteria to consider when designing an analysis workflow. 
If you work in a team, you should take particular care of the conventions and make sure everyone follows them. 

To learn more about data organisation in spreadsheets, you may have a look at the Data Carpentry lessons for [Social Scientists](https://datacarpentry.org/spreadsheets-socialsci/) and [Ecologists](https://datacarpentry.org/spreadsheet-ecology-lesson/).
