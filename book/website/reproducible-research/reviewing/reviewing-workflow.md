(rr-reviewing-workflow)=
# Typical Workflows

*This chapter has particular reference to Github*

```{figure} ../../figures/readable-code.*
---
height: 500px
name: readable-code
alt: This image highlights the importance of code readability.
---
_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).
```

## Formal vs Informal Reviews

For a formal review process to work effectively, it's imperative that the project is using good {ref}`version control<rr-vcs>`.
However, it bears stating that **all review of code is very valuable**, including informal or ad-hoc approaches. Indeed, this kind of informal "over the shoulder" peer review can form a key preliminary component even in highly formalised review pipelines, saving a lot of stress and arguing once the formal stage begins.

This section focuses on the typical workflows behind a formal review process, as commonly implemented within [Github](https://github.com/).
Other coding environments like [BitBucket](https://bitbucket.org/) or [GitLab](https://about.gitlab.com/) could have conceptually similar mechanisms but they are not explained here.

## Prepare The Code

Before requesting a review, make sure you've met all the obvious quality benchmarks for the project you are contributing to.
This means making sure you have checked the review list (see {ref}`checklist for the coder<rr-checklist-for-code-review>`).

A reviewer should check these things (see {ref}`checklist for the coder<rr-checklist-for-code-review>`), but defects on these fronts should be by occasional oversight, rather than systematic.

## Propose Changes

In the GitHub system, the review is begun directly from and often accessed through the [pull request page](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
The review step occurs between the points where the coder believes their contribution is complete and where that contribution is merged into the trunk code for the project, and so it is intimately associated with a single pull request.

Within the Github environment, projects can be configured to *require* a review before a given pull request can be merged.
Even if this option hasn't been selected, it's still possible (and indeed best practice) to manually request a review on a pending pull request.

## Create and Discuss The Review

At this point, the review process can begin. In Github, the reviewer can provide both general comments as well as line-by-line comments, see [GitHub code review](https://github.com/features/code-review).
Each comment becomes its own comment thread, permitting back-and-forth discussion about each issue as required.
This interaction should allow consensus to be reached on every comment.

Once the review is complete, you can discuss any comments necessary. Then you make the changes, and record the changes made against appropriate comments.
Also, you check that the reviewer knows you believe you have fully addressed the review.

Once you believe changes are complete, the reviewer checks that they do indeed address all of the initial comments. As needed, the reviewer engages constructively with you if they disagree on certain points in order to come to a consensus. In most cases, the reviewer has a final say if a consensus cannot be found.

Once post-review changes have been made to the code, make final updates the comments as needed to complete a history of what has been done and the reasoning behind it.

## Communicating Results Through GitHub

In Github, comments should be added in the `Files changed` section, so they can be attached to a particular line of code, see [GitHub reviewing changes in pullrequests](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/reviewing-changes-in-pull-requests). Make many small comments this way, rather than a big ball of text with everything in it, so that different issues can be kept separate. Where relevant, refer to existing Issues and documentation.

If you're reviewing existing code rather than changes, it is still handy to use pull requests.
If you find an issue that has an obvious fix, you can submit a pull request with a patch in the usual way.

If you don't have a fix, you can add an empty comment to the relevant line, and create a pull request from that as a patch. The relevant line(s) will then light up in the pull request's `Files changed` overview, and you can add your comments there.
In this case, either the pull request is never merged (but the comments processed some other way, or not at all), or the extra comments are reverted and replaced by an agreed-upon fix.

In all cases, file many small pull requests, not one big one, as GitHub's support for code reviews is rather limited. Putting too many issues into a single pull request quickly becomes unwieldy.

## Merge The Changes

Once the review process is complete, the reviewer approves the changes, and the merge can occur.
Individual projects typically have rules and/or guidelines for whether the coder or the reviewer actually presses the merge button, so check.
In many cases, project workflows make completion of a review and its sign-off by the reviewer a formal precondition of performing the merge.
For the avoidance of doubt, adopting this principle even for small or informal projects is probably sensible.
