(ch-style-citing)=
# Citing and Referencing

We maintain a centralised [BibTeX](http://www.bibtex.org/) file containing all references.
The file is located within this repository in the file
[`./book/website/_bibliography/references.bib`][turingbib].

## BibTeX file basics

BibTeX files are a way to format lists of references in a structured way.
Basic elements of an entry include a reference type, a unique citation key, and a series of key-value pairs that describe the reference (for example, author or title).

There are a number of keywords for different references types in BibTeX.
Luckily, there are tools to help format references into BibTeX syntax.
If you know the DOI for your reference, you can use [doi2bib](https://doi2bib.org/) to help populate a good enough BibTeX entry.
For example, [here](https://doi2bib.org/bib/https://doi.org/10.5281/zenodo.3233853) is a good enough BibTeX entry for The Turing Way handbook itself.
Another good tool is [Google Scholar](https://scholar.google.com/), where you search for a reference, click on the large double quotes `"`, and then click on "BibTeX" near the bottom.

Examples of listing a BibTeX-formatted reference are shown below.

## Adding a new reference in `references.bib`

You can edit reference file locally using a method from the following:

- Edit [`references.bib`][turingbib] directly using a text editor
- Edit [`references.bib`][turingbib] directly using a managing program such as [JabRef](http://www.jabref.org/) (Linux, Windows, macOS) or [BibDesk](https://bibdesk.sourceforge.io/) (macOS)

We use a standard bibtex format to add a new entry.
For example, there is an entry in the [`references.bib`][turingbib] file as:

```
@article{Kuula2010archiving,
	Author = {Kuula, Arja},
	Date-Added = {2019-05-28 17:47:46 +0100},
	Date-Modified = {2019-05-30 8:57:26 am +0100},
	Journal = {IASSIST Quarterly},
	Number = {3-4},
	Pages = {35},
	Title = {Methodological and Ethical Dilemmas of Archiving Qualitative Data},
	Url = {http://www.iassistdata.org/sites/default/files/iqvol34_35_kuula.pdf},
	Volume = {34},
	Year = {2010}}
```

**Finish editing by adding a new entry at the end of the file.**

## Citation key style-guide

We recommend using the following structure for citation keys:

```
AuthorYYYYword
```

Where:

1. `Author` is the surname of the first author (`Kuula` above)
2. `YYYY` is the year (`2010` above)
3. `word` is the first meaningful word in the title (`archiving` above). Note, this is subjective―choose a name that makes it easy to remember the reference when you see the citation key.

## Adding a new reference in the text

To include a citation in your content, we follow the recommendation by [Jupyter Book](https://jupyterbook.org/content/citations.html) that uses [`sphinxcontrib-bibtex`](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/) extension.

The key concepts are:

- Include a reference using {cite}`CITEKEY`, where `CITEKEY` is the corresponding citation key in [`references.bib`][turingbib]
- You can also include multiple citations in one go by separating the CITEKEYs by a comma: `{cite}CITEKEY1,CITEKEY2,CITEKEY3`

We will cite the article that we edit earlier in the [`reference.bib`][turingbib] file using:

```
{cite}`Kuula2010archiving`
```

This will appear in your chapter as {cite}`Kuula2010archiving`.

The complete bibliography entry is available at the end of this book (see {ref}`resources <afterword-bibliography>`) using the directives:

    ```{bibliography} ../_bibliography/references.bib

    ```

For the advanced usage, see the [documentation by sphinxcontrib-bibtex](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html), which is a Sphinx extension for BibTeX style citations.

[turingbib]: https://github.com/alan-turing-institute/the-turing-way/blob/master/book/website/_bibliography/references.bib
