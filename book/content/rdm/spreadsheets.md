# Using spreadsheets for research data

Spreadsheets, such as Microsoft Excel files and its Open Source alternative [LibreOffice](https://www.libreoffice.org), are commonly used to collect, store, manipulate, analyse, and share research data.
Spreadsheets are convenient and easy-to-use tools for these tasks but are not facilitate reproducibility
if used as dynamic documents.
There is a collection of [horror-stories](http://www.eusprig.org/horror-stories.htm) that document the many ways that the use of spreadsheets have scuppered analyses due to unexpected behaviour or error-prone
editing processes.
Some of these mishaps are not unique to spreadsheets, but [many are](https://doi.org/10.1186/s13059-016-1044-7).

Data manipulation and analysis in spreadsheets in particular is best avoided as, without version control, it can lead to non-reproducible workflows.
By opening and editing raw data files directly by hand, for example to change values or perform calculations, the process by which new values are obtained is not properly documented, and you may accidentally over-write something or type in the wrong value only to notice after it's too late (or not at all).

Even if these errors are avoided, if the spreadsheet is poorly organised then it may be [difficult for collaborators](https://luisdva.github.io/pls-don't-do-this/) to easily [read-in and re-use](#FAIR) your
data for further analysis.

It's often not practical to avoid the use of spreadsheets altogether but there are some simple steps that can be taken
to mitigate their flaws.
The following principles, provide some practical advice to ensure your data is clearly organised and human- and machine-readable {% cite Broman2018data --suppress_author %}:

- Be consistent
- Write dates as YYYY-MM-DD
- Don't leave any cells empty, if there is no data use "NA" (Not Available)
- Put each observation/sample in its own cell/row
- Put each variable in a column
- Each cell should contain information on one thing: separate multiple pieces of information to different cells
- Create a data dictionary
- Don't include calculations in the raw data files: make the file with raw data read-only!
- Don’t use font, color or highlighting, consider adding another variable/column for this information
- Choose descriptinve names for observations and variables and make sure there are no spaces or special characters in the names
- Make backups
- Use data validation to avoid data entry mistakes
- Save the data in text files (such as `.csv` - comma-separated values) to ensure interoperability with other software programmes.

You can explain the file naming convention in a README.txt file, so that it will also become clear to others what the file names mean.
To learn more about data organisation in spreadsheets, have a look at the Data Carpentry lessons for [Social Scientists](https://datacarpentry.org/spreadsheets-socialsci/) and [Ecologists](https://datacarpentry.org/spreadsheet-ecology-lesson/).
