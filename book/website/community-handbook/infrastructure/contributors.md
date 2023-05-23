# Contributors

Contributors are published in the book's {ref}`Record of Contributions<contributors-record>`.
The information for this page's three subsections are source from different places.

## Personal Highlights

The {ref}`Personal Highlight section<contributors-record-highlights>` is taken directly from [`contributors.md`](https://github.com/alan-turing-institute/the-turing-way/blob/main/contributors.md) in the root of the repository.
This is inserted into [`contributors-record.md`](https://github.com/alan-turing-institute/the-turing-way/blob/main/book/website/afterword/contributors-record.md`) verbatim using the [`include` docutils directive](https://docutils.sourceforge.io/docs/ref/rst/directives.html#including-an-external-document-fragment).

To modify this section you would change `contributors.md` and rebuild the book.

## All Contributors

The {ref}`All Contributors section<contributors-record-all>` displays the same [all contributors](https://allcontributors.org/docs/en/overview) table as [`README.md`](https://github.com/alan-turing-institute/the-turing-way/blob/main/README.md).

The information to build this table is contained in [`.all-contributors.rc`](https://github.com/alan-turing-institute/the-turing-way/blob/main/.all-contributorsrc), the configuration file for all contributors.
This JSON file controls the appearance of the table and also specifies where to write the all contributors table in the `"files"` list.
Each time the all contributors bot or CLI is run the table will be written to files in the `"files"` list.

The table is inserted as html between the following sets of tags

```
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
```

```
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
```

## Collaborating Organisations and Projects

The {ref}`Collaborating Organisation and Projects section<contributors-record-collaborators>` is written directly in `contributors-record.md`.
