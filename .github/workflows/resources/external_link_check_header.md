# Broken Links

**This is an automated issue created in a weekly continuous integration job 🤖.**

This issue contains a list of links external to The Turing Way that appeared to be broken when the check was last run.

**The conversation on this issue has been locked.**
This is because the list of broken links will change whenever the job is run, so this is not a good place to discuss particular links.

## Understanding the Errors

### Locating Errors

Errors are grouped by the output html pages they appear in.

The paths of these pages after `book/website/_build/html` correspond to their source Markdown files.
For example, `book/website/_build/html/reproducible-research/vcs/vcs-workflow.html` corresponds to `book/website/reproducible-research/vcs/vcs-workflow.md`.
Broken links can be fixed in the Markdown file.

### False Negatives

The list of error **will contain false negatives**.
Some domains will interpret the link checker as a possible denial of service attack, especially if it makes multiple requests.
Others may require authentication for particular pages.
The link checker may then be unable to verify that certain links works.

If certain domains are repeatedly producing false negatives they can be ignored by adding an entry to the `exclude` list in the [Lychee configuration file](https://github.com/the-turing-way/the-turing-way/blob/main/lychee.toml).

### Link Status

Each failing link is presented with its status which is either a string like `ERR`, `TIMEOUT` or a HTTP response status code like `404`.
Mozilla has a [guide to HTTP response codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) which can help explain the codes in the list.

Here are some rules of thumb.
These are quite likely to be false negatives,

- 403
- TIMEOUT

These are quite likely to be genuine problems,

- 404
- ERR
- 50? (500, 501, 502, _etc._)
