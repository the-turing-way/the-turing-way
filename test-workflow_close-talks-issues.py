import os
import re
import sys
from datetime import datetime
from ghapi.all import GhApi, paged

# Repository details
owner = "alan-turing-institute"
repo = "the-turing-way"

# The label we want our returned issues to have
label = "talks-and-workshops"
newsletter_label = "newsletter"

# A token to authenticate against the GitHub REST API with
github_token = os.environ.get("GITHUB_TOKEN", None)
if github_token is None:
    raise Exception("GITHUB_TOKEN must be provided!")

# Authenticate against the GitHub REST API
api = GhApi(token=github_token)

# Get all the issues on the repo that have a desired label
all_issues = paged(
    api.issues.list_for_repo,
    owner=owner,
    repo=repo,
    state="open",
    labels=label,
    per_page=100,
)

issues_to_close = []
today = datetime.now()
pattern = re.compile("[0-9]{4}-[0-1][0-9]-[0-3][0-9]")

for paged_issues in all_issues:
    for issue in paged_issues:
        match = pattern.search(issue.body)
        talk_date = datetime.strptime(match[0], "%Y-%m-%d")
        date_diff = talk_date - today
        to_be_closed = date_diff.days < -7

        if to_be_closed:
            issue_info = {
                "repository_url": issue.repository_url,
                "issue_number": issue.number,
            }
            issues_to_close.append(issue_info)

if len(issues_to_close) == 0:
    sys.exit()

# Construct Markdown text listing all the issues that have been closed
body = (
    "Please add the following talks to the next newsletter!\n\n"
    + "\n".join([f"- {issue['repository_url']}" for issue in issues_to_close])
)

# Check if a newsletter issue is already open
all_issues = paged(
    api.issues.list_for_repo,
    owner=owner,
    repo=repo,
    state="open",
    creator="github-actions[bot]",
    labels=newsletter_label,
    per_page=100,
)
# print(all_issues)

# for paged_issues in all_issues:
#     print(type(paged_issues))
#     for issue in paged_issues:
#         print(type(issue))
paged_issues = next((p for p in all_issues), False)
print(bool(paged_issues))
if paged_issues:
    print(paged_issues[0].number)
