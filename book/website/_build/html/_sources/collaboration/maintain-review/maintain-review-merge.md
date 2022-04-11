(cl-maintain-review-merging)=
# Merging Contributions
Pull requests made by contributors can be approved or merged by maintainers after the review.
There are different ways of merging a pull request:
- *Merge pull request*: Merges all commits to base branch.
It keeps all commits made in the PR as separate and merges them as they are, through a single merge commit to the base branch.
- *Squash and merge*: Squashes all commits created in the pull request into one commit and merges them as a single commit (with the help of a merge commit) to the base branch (see this [blog for details](https://github.blog/2016-04-01-squash-your-commits/)).
- *Rebase and merge*: Rebases all commits individually to base branch (integrating changes from one branch to other) before merging.
In the prompt message, the maintainer can provide a merge message along with comments(if any) and then press the “confirm merge” button.
