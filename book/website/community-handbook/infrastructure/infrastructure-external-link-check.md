# External Link Checking

An external link check tests if links between pages of The Turing Way and other websites work.
This is a useful tool which helps us ensure that when uses click a link they are brought to a working page.

There is a [GitHub workflow](https://github.com/alan-turing-institute/the-turing-way/blob/main/.github/workflows/external_link_check.yml) which regularly tests external links in the book and posts a list of broken links to an [issue](https://github.com/alan-turing-institute/the-turing-way/issues/3171).
This section explains the processes which updates the broken links issue.

## Workflow

The [workflow](https://github.com/alan-turing-institute/the-turing-way/blob/main/.github/workflows/external_link_check.yml) is dispatched according to a [schedule](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule).
The schedule uses [POSIX cron](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule) format to specify when the workflow should run.
The workflow is currently configured to run once per week at midnight on Monday in the UTC+00:00 time zone.

[Lychee](https://lychee.cli.rs/) is used to test external links in the books' links _after_ building the book.
If the book fails to build then the workflow will fail.
The workflow uses cached results from previous runs to avoid the need to recheck all links every time the check is run.
This does however mean that cached results may not be up to date.

The GitHub runners GitHub Token is specified as an environment variable for the Lychee action.
This prevents false negatives due to rate limiting when testing links to GitHub.

The [Lychee configuration](https://github.com/alan-turing-institute/the-turing-way/blob/main/lychee.toml) in the root of the repository controls the behaviour of Lychee.
An example configuration file with explanations can be found in [the Lychee documentation](https://lychee.cli.rs/#/usage/config).

The configuration file can be used to improve the usefulness of the broken links issue.
In particular, it is possible to exclude domains which are known to produce false negatives.

Lychee produces a report of broken links and save this to a Markdown file.
The workflow then concatenates this report with an [issue header](https://github.com/alan-turing-institute/the-turing-way/blob/main/.github/workflows/resources/external_link_check_header.md) and updates the broken links issue.

## Issue

The broken links issue is [#3171](https://github.com/alan-turing-institute/the-turing-way/issues/3171).
The information added to the issue in the [issue header](https://github.com/alan-turing-institute/the-turing-way/blob/main/.github/workflows/resources/external_link_check_header.md) aims to explain the output and provide some guidance for fixing broken links.
That information is not duplicated here.
Improvements to the explanation or guidance should be made to the [issue header](https://github.com/alan-turing-institute/the-turing-way/blob/main/.github/workflows/resources/external_link_check_header.md) as any changes made to the issue will be overwritten when it is next updated.
