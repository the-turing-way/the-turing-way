# Naming files, folders and other things 

## Prerequisites / recommended skill level

None.

## Summary

Good names for files, folders and other things can make your life and the life of collaborators and other people using your research much easier.
It allows others to understand what the digital object is about and at the same time good names are easy for computers to understand and process.

## How this will help you/ why this is useful

Using good names is probably the easiest way to improve reproducibility and reusability of your research project.

## Chapter content

There are three principles to naming things. The first two apply to all kinds of things. The third is optional and especially valuable for files. Names should be:

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

To achieve human readability, it is helpful to have a name that contains information on the content of the file/folder or other thing. For URLs this concept is called [clean URL](https://en.wikipedia.org/wiki/Clean_URL).

For example, we can probably all agree that `JW7d^(2sl@deletethisandyourcareerisoverWx2*.txt` is worse to understand than `1986-01-28_raw-data-from-challenger-o-rings.txt` in terms of what the file contains.


### Play well with default ordering

To create a good default ordering, adding number at the beginning of the name, is often a good idea. 
Imagine you have a folder with all your presentation slides, it would probably be helpful to have them ordered by date. 
So starting the file names with `year-month-day` (for example `2020-02-21`), does that for you.
We recommend using something like the [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601) for dates.
File name `2020-06-08_abstract-for-sla.docx` is a nice example.

If you use other number, we recommend left padding them with zeros, because your computer will order `003 < 004 < 020 < 100` as opposed to `100 < 20 < 3 < 4`. You can also use words and numbers in combination to get the ordering you want. `Fig01_scatterplot-talk-length-vs-interest.png` and `Fig02_histogram-talk-attendance.png` are a good example.
From experience we know that naming folders according to logical numbers can lead to a mess if the ordering changes.
For example if you have book chapter folders `01_introduction`, `02_naming_files`, `03_naming_folders`, and so on and then you decide to change the order or try to squeeze in a folder in between `01_introduction` and `02_naming_files`, this can create a wors situation than not using numbers to enforce ordering.



## Checklist

Make sure, the names of files, folders and other things are:

- [ ] Machine readable
- [ ] Human readable

And potentially also 

- [ ] Play well with default ordering


## What to learn next

Want to build a folder with all the files from your research project? 
Check out our chapter on [research compendia](research_compendia/research_compendia).


## Further reading

The ideas for this chapter are taken from Jenny Brian's slide deck on [naming things](https://speakerdeck.com/jennybc/how-to-name-files).



