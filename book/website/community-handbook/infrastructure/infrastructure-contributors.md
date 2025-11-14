(ch-infrastructure-contributors)=
# Publishing Contributors

Keeping track of contributions of all types is important: both code and non-code contributors.
Within _The Turing Way_, contributors are kept track of and published in the book's [](#contributors-record).
The rationale and guidance for acknowledging contributions are explained in [](#ch-acknowledgement).

The data for sections of [the contributors record](#contributors-record) are sourced from different places,

:::{embed} tab-contribution-records
:::

In this page we describe the infrastructure supporting publishing contributors.

## All Contributors

The [All Contributors section](#contributors-record-all) displays the same [all contributors](https://allcontributors.org/docs/en/overview) table as [`README.md`](https://github.com/the-turing-way/the-turing-way/blob/main/README.md).

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

## Translators

The [translation contributions](#contributors-record-translators) are taken from the Crowdin API.
This process is automated in [this workflow](https://github.com/JimMadge/the-turing-way/blob/main/.github/workflows/crowdin-contributors.yml).
The workflow, which runs weekly, fetches data from the Crowdin API then updates the tables in both the project's `README.md` and the page in the afterword.
