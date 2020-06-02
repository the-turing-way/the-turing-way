## Typical workflows (with particular reference to Github)

<a name="Formal_vs_informal_reviews"></a>
### Formal vs informal reviews

This section focuses on the typical workflows behind a formal review process, as commonly implemented within a social coding environment like Github. However, it bears stating that **all review of code is very valuable**, including informal or ad-hoc approaches. Indeed, this kind of informal "over the shoulder" peer review can form a key preliminary component even in highly formalised review pipelines, saving a lot of stress and arguing once the formal stage begins.

<a name="forks_and_branches"></a>
### Forks and branches

For a formal review process to work effectively, it's imperative that the project is using good [version control](/version_control/version_control). The review step occurs between the points where the coder believes their contribution is complete and where that contribution is merged into the trunk code for the project, and so it is intimately associated with a single pull request. Creation of the review and discussion between the reviewer and the coder occurs once the pull request is made and before it is merged into the master. In the github system, the review is begun directly from and often accessed through the pull request page.

Within the Github environment, projects can be configured to *require* a review before a given pull request can be merged. Even if this option hasn't been selected, it's still possible (and indeed best practice) to manually request a review on a pending PR.

<a name="prepare_the_code"></a>
### Prepare the code

Before requesting a review, be sure you've met all the obvious quality benchmarks for the project you are contributing to. This means making sure:

- you have created [documentation](#Documentation) to the required standards of the project,
- you have [tested](#Improvements_to_testing) your code to the required standards of the project,
- your code is not causing the tests in the main project to fail (many [continuous integration](/continuous_integration/continuous_integration) systems will test this automatically for you once you create the PR), and
- you believe your code meets the declared [style guide](../../code_quality/code_quality#code-style) for the project.

A reviewer should check these things, but defects on these fronts should be by occasional oversight, rather than systematic.

<a name="create_discuss_change"></a>
### Create and discuss the review; make the changes

At this point, the review process can begin. In Github, the reviewer can provide both general comments as well as line-by-line comments. Each comment becomes its own comment thread, permitting back-and-forth discussion about each issue as required. This interaction should allow consensus to be reached on every comment. In most cases, the reviewer has final say if a consensus cannot be found.

Once post-review changes have been made to the code, make final updates the comments as needed to complete a papertrail of what has been done and the reasoning behind it.

<a name="make_the_merge"></a>
### Make the merge

Once the review process is complete, the merge can occur. Individual projects typically have rules and/or guidelines for whether the coder or the reviewer actually presses the merge button, so check. In many cases, project workflows make completion of a review and its sign-off by the reviewer a formal precondition of performing the merge. For the avoidance of doubt, adopting this principle even for small or informal projects is probably sensible.
