(ch-infrastructure-contributors)=
# Publishing Contributors

Keeping track of contributions of all types is important: both code and non-code contributors.
Within _The Turing Way_, contributors are kept track of and published in the book's {ref}`Record of Contributions<contributors-record>`.
The rationale and guidance for acknowledging contributions are explained in {ref}`ch-acknowledgement`

The information for the {ref}`Record of Contributions<contributors-record>` page's three subsections are sourced from different places.
This page documents how these sources are combined to create the {ref}`Record of Contributions<contributors-record>`.

## Personal Highlights

The {ref}`Personal Highlights section<contributors-record-highlights>` is taken directly from [`contributors.md`](https://github.com/the-turing-way/the-turing-way/blob/main/contributors.md) in the root of the repository.
This is inserted into [`contributors-record.md`](https://github.com/the-turing-way/the-turing-way/blob/main/book/website/afterword/contributors-record.md) verbatim using the [`include` docutils directive](https://docutils.sourceforge.io/docs/ref/rst/directives.html#including-an-external-document-fragment).

To modify this section you would change `contributors.md` and rebuild the book.

## All Contributors

The {ref}`All Contributors section<contributors-record-all>` displays the same [all contributors](https://allcontributors.org/docs/en/overview) table as [`README.md`](https://github.com/the-turing-way/the-turing-way/blob/main/README.md).

The information to build this table is contained in [`.all-contributorsrc`](https://github.com/the-turing-way/the-turing-way/blob/main/.all-contributorsrc), the configuration file for all contributors.
This JSON file controls the appearance of the table and also specifies where to write the all contributors table in the `"files"` list.
Each time the all contributors bot or CLI is run the table will be written to files in the `"files"` list.

The table is inserted as HTML between the following sets of tags:

```Markdown
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
```

```Markdown
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
```

You shouldn't need to make changes to the HTML directly.
Furthermore, it will be overwritten often by the all contributors bot.
Manual changes to the contributors list, such as adding a contributor or regenerating the table, can be made using the [all contributors CLI](https://allcontributors.org/docs/en/cli/usage).

## Collaborating Organisations and Projects

The description of the {ref}`Collaborating Organisation and Projects<collaborators>` should be directly written in `collaborarators.md` file in the 'Afterword' of the book.
