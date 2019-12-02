# Data organisation in spreadsheets

Spreadsheets, such as Microsoft Excel files, are commonly used to collect, store, manipulate, analyse, and share
research data. Spreadsheets are convenient and easy-to-use tools for these tasks but are not amenable to reproducibility
if used as dynamic documents. There is a collection of [horror-stories](http://www.eusprig.org/horror-stories.htm) that
document the many ways that the use of spreadsheets have scuppered analyses due to unexpected behaviour or error-prone
editing processes. Some of these mishaps are not unique to spreadsheets, but
[many are](https://doi.org/10.1186/s13059-016-1044-7).

Data manipulation and analysis in spreadsheets in particular is best avoided as, without version control, it can lead to
non-reproducible workflows. By opening and editing raw data files directly by hand, for example to change values or
perform calculations, the process by which new values are obtained is not properly documented, and you may accidentally
over-write something or type in the wrong value only to notice after it's too late (or not at all).

Even if these errors are avoided, if the spreadsheet is poorly organised then it may be
[difficult for collaborators](https://luisdva.github.io/pls-don't-do-this/) to easily [read-in and re-use](#FAIR) your
data for further analysis.

It's often not practical to avoid the use of spreadsheets altogether but there are some simple steps that can be taken
to mitigate their flaws. The following principles, taken from Broman et al. {% cite Broman2018data --suppress_author %},
provide some practical advice to ensure your data is clearly organised and human- and machine-readable:

- Be consistent
- Write dates as YYYY-MM-DD
- Don't leave any cells empty
- Put just one thing in a cell
- Organize the data as a single rectangle
- Create a data dictionary
- Don't include calculations in the raw data files
- Don’t use font colour or highlighting as data
- Choose good names for things
- Make backups
- Use data validation to avoid data entry mistakes
- Save the data in plain text files
