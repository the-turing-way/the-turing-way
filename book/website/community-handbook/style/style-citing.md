(ch-style-citing)=
# Citing and Referencing

In MyST Markdown you can make citations in two ways, using DOIs or the bibliography.
If you want to cite an article with a DOI, you can use a [DOI link](https://mystmd.org/guide/citations#doi-links).
We maintain a centralised [BibTeX](http://www.bibtex.org/) bibliography file containing references.
The bibliography file is located in the book repository, [`./book/website/references.bib`][turingbib].

## DOI citations

You can reference a document by its DOI simply by linking to the DOI url.
For example, `[_The Turing Way_](https://doi.org/10.5281/zenodo.15213042)` renders as [_The Turing Way_](https://doi.org/10.5281/zenodo.15213042).
Note that this _only_ works for the `doi.org` url and not, for example, a `zenodo.org` url.

You can also let MyST create a citation string using the DOI string and the prefix `doi:`.
For example, `[](doi:10.5281/zenodo.15213042)` renders as [](doi:10.5281/zenodo.15213042).

You can read more about DOI links in the [MyST Markdown documentation](https://mystmd.org/guide/citations#doi-links).

## Bibliography

### BibTeX file basics

BibTeX files are a way to format lists of references in a structured way.
Basic elements of an entry include a reference type, a unique citation key, and a series of key-value pairs that describe the reference (for example, author or title).

There are a number of keywords for different references types in BibTeX.
Luckily, there are tools to help format references into BibTeX syntax.
If you know the DOI for your reference, you can use [doi2bib](https://doi2bib.org/) to help populate a good enough BibTeX entry.
For example, [here](https://doi2bib.org/bib/https://doi.org/10.5281/zenodo.3233853) is a good enough BibTeX entry for The Turing Way handbook itself.
Another good tool is [Google Scholar](https://scholar.google.com/), where you search for a reference, click on the large double quotes `"` or activate the pop-up menu labeled "Cite," and then click on "BibTeX" near the bottom.

Examples of listing a BibTeX-formatted reference are shown below.

### Adding a new reference in `references.bib`

You can edit reference file locally using a method from the following:

- Edit [`references.bib`][turingbib] directly using a text editor
- Edit [`references.bib`][turingbib] directly using a managing program such as [JabRef](http://www.jabref.org/) (Linux, Windows, macOS) or [BibDesk](https://bibdesk.sourceforge.io/) (macOS)

We use a standard BibTeX format to add a new entry.
For example, there is an entry in the [`references.bib`][turingbib] file as:

```
@article{baker2016reproducibility,
    author={Baker, Monya},
  	title={Reproducibility crisis?},
  	journal={Nature},
  	volume={533},
  	number={26},
  	pages={353--66},
  	year={2016}
}
```

### Citation key style-guide

We recommend using the following structure for citation keys:

```
AuthorYYYYword
```

Where:

1. `Author` is the surname of the first author (`Baker` above)
2. `YYYY` is the year (`2016` above)
3. `word` is the first meaningful word in the title (`reproducibility` above). Note, this is subjective―choose a name that makes it easy to remember the reference when you see the citation key.

### Adding a new reference in the text

To cite an item in the bibliography, use the citation key (from [`references.bib`][turingbib]) with an `@` prefix.
For example, `@baker2016reproducibility` renders as @baker2016reproducibility.

You can cite multiple items at once by separating them with semi-colons and enclosing them in square brackets.
For example, `[@baker2016reproducibility; @Markowetz2015]` renders as [@baker2016reproducibility; @Markowetz2015].

You can read more about the markdown citation syntax in the [MyST Markdown documentation](https://mystmd.org/guide/citations#markdown-citations).

### Sphinx-style Citation Roles

MyST also support the older style of [citation role](https://mystmd.org/guide/citations#citation-roles) used in Jupyter Book v1.
These are not preferred for new citations, but you may see existing citation in this style in the book.

[turingbib]: https://github.com/the-turing-way/the-turing-way/blob/main/book/website/references.bib
