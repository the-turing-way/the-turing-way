### Citing and Referencing

We maintain a centralised [bibtex](http://www.bibtex.org/) file containing all references.
The file is located within this repository in the file `./book/website/_bibliography/references.bib`.

#### Adding a new reference

To include a citation in your content, we follow the recommendation by [JupyterBook](https://jupyterbook.org/content/citations.html) that uses sphinxcontrib-bibtex extension.

The key concepts are:

- Include a reference using {cite}`CITEKEY`, where `CITEKEY` is the corresponding citation key in `references.bib`
- You can also include multiple citations in one go by separating the CITEKEYs by a comma: {cite}`CITEKEY1,CITEKEY2,CITEKEY3`
- Add a bibliography entry at the end of your file use the following directive under a reference header:

```{bibliography} ../_bibliography/references.bib
```

This will generate a bibliography for all the files you have referenced in your file.
Please note that you will need to edit the relative path (`../_bibliography/references.bib`) of the `references.bib` based on the location of file you edit.

#### Adding a new reference in `references.bib`

You can edit references locally using a method from the following:

- Edit `references.bib` directly using a text editor
- Edit `references.bib` directly using a managing program such as [JabRef](http://www.jabref.org/) (linux, windows, macOS) or [BibDesk](https://bibdesk.sourceforge.io/) (macOS)

For example, say we have an entry in the `references.bib` file as:

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

We could cite this article in the book using {cite}`Kuula2010archiving`.

For the advanced usage, see the the [documentation  by sphinxcontrib-bibtex](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html), which is a Sphinx extension for BibTeX style citations.

#### Citation key style-guide

We recommend using the following structure for citation keys:

```
AuthorYYYYword
```
Where:
1. `Author` is the surname of the first author (`Kuula` above)
2. `YYYY` is the year (`2010` above)
3. `word` is the first meaningful word in the title (`archiving` above). Note, this is subjective – choose a name that makes it easy to remember the reference when you see the citation key.
