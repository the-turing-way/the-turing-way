# Naming files, folders and other things 

## Prerequisites / recommended skill level

None.

## Summary

By naming your files, folders, and other research components consistently and descriptively, you can make your work findable, understandable and reusable by yourself, your collaborators, and other people interested in your research.
It allows others to understand what the digital object is about: What the files contain and where to find them. Moreover, by following simple tips for file naming, you can make your files easy for computers to identify and process.

## How this will help you/why this is useful

Using good names is probably the easiest way to improve reproducibility and reusability of your research project.

## Chapter content

There are three principles to naming things; the first two apply to all kinds of things and the third is optional but valuable for keeping track of your files. 

File names should be:
1. Machine readable
2. Human readable
3. Optional: Play well with default ordering


Before we dive into the details of what they mean, let's look at some examples of bad and good file names.

| :x: Bad          | :heavy_check_mark: Good |
| -----------------|-------------------------|
|`Myabstract.docx` | `2020-06-08_abstract-for-sla.docx` |
|`Joe’s Filenames Use Spaces and Punctuation.xlsx` | `Joes-filenames-are-getting-better.xlsx` |
|`figure 1.png` | `Fig01_scatterplot-talk-length-vs-interest.png` |
|`fig 2.png` | `Fig02_histogram-talk-attendance.png` |
|`JW7d^(2sl@deletethisandyourcareerisoverWx2*.txt` | `1986-01-28_raw-data-from-challenger-o-rings.txt` |


### Machine readable

Names of digital components should be easy to understand for computers.
Computers like names to have no spaces, deliberate use of delimiters, and no special or accented characters.
Also computers are case sensitive, so for them `cat.txt` and `Cat.txt` are different files.

The file names `Joe´s Filenames Use Spaces and Punctuation.xlsx` and `JW7d^(2sl@deletethisandyourcareerisoverWx2*.txt` shown above use empty spaces and special characters (`´`, `^`, `(`, `@`,`*`), which can lead to difficulties, for example when you want to send it someone else's computer.

Good file/folder names are easy to search for (also using regular expressions) and easy to compute on (for example by splitting on `_` or `-` characters).


### Human readable

To achieve human readability, it is helpful to have short (< 25 characters) but descriptive names that contain information on the content of the file/folder.
Word boundaries in the file name can be indicated by using medial capitalization called camel case, for example "FileName", or underscore, for example "file_name".
File names should not have any spaces or other special characters.

For web links or Uniform Resource Locator (URL), this concept is called [clean URL](https://en.wikipedia.org/wiki/Clean_URL).

### Play well with default ordering

To create a good default ordering adding a number or date at the beginning of the name is often a good idea. 
This keeps our files sorted in ascending order based on file versions or in chronological order. 
For instance, we often organize all our slide decks created on different dates in the same folder. 
To sort them by their date of creation, we can start the file names with `year-month-day` (for example `2020-02-21`).
We recommend using something like the [ISO 8601 standard: YYYY-MM-DD](https://en.wikipedia.org/wiki/ISO_8601) for dates. 
If you use other numbers, we recommend left padding them with zeros, because your computer will order `003 < 004 < 020 < 100` as opposed to `100 < 20 < 3 < 4`. 

Naming folders according to a logical number can lead to a mess if the ordering changes in the future.
For example, there is a folder with the book chapters `01_introduction`, `02_naming_files`, and `03_naming_folders`. The author writes a preface of the book and decides to squeeze it before the introduction chapter. This would mean that they will have to rename all the files to maintain the intended order. 
This happens a lot and clearly, this has more downsides than upsides.

## Checklist

Here are some tips for naming files within a research project, which are both human- and machine-readable (taken from [Research Data Management at Princeton](https://libguides.princeton.edu/c.php?g=102546&p=930626))

- [ ] Name your files consistently
- [ ] Keep it short but descriptive
- [ ] Avoid special characters or spaces to keep it machine-compatible
- [ ] Use capitals or underscores to keep it human-readable
- [ ] Use consistent date formatting, for example ISO 8601: `YYYY-MM-DD` to maintain default order
- [ ] Include a version number when applicable
- [ ] Share/establish a naming convention when working with collaborators
- [ ] Record a naming convention in your data management plan


## What to learn next

Want to build a folder with all the files from your research project? 
Check out our chapter on [research compendia](research_compendia/research_compendia).


## Bibliography

- Jenny Brian's slide deck on [naming things](https://speakerdeck.com/jennybc/how-to-name-files).
- File naming and file structure recommendations by [Research Data Management at Princeton](https://libguides.princeton.edu/c.php?g=102546&p=930626)
- Amy Hodge compiled a set of recommendations as [best practices for file naming](https://library.stanford.edu/research/data-management-services/data-organization/best-practices-file-naming) and [case studies of file naming done well](https://library.stanford.edu/research/data-management-services/case-studies/case-study-file-naming-done-well) at Data Management Services in Stanford Library
