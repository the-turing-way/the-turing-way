"""
Script to pull changed files in a Pull Request using a GET resquest to the
GitHub API.
"""
import requests
import argparse


def parse_args():
    """Construct the command line interface for the script"""
    DESCRIPTION = "Script to check for occurences of 'Lorem Ipsum' in Markdown files"
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "--pull-request",
        type=str,
        default=None,
        help="If the script is be run on files changed by a pull request, parse the PR number",
    )

    return parser.parse_args()


def get_files_from_pr(pr_num):
    """Return a list of changed files from a GitHub Pull Request

    Arguments:
        pr_num {str} -- Pull Request number to get modified files from

    Returns:
        {list} -- List of modified filenames
    """
    files = []
    pr_url = f"https://api.github.com/repos/the-turing-way/the-turing-way/pulls/{pr_num}/files"
    resp = requests.get(pr_url)

    # Raising for status to avoid ending up with red-herring tracebacks later
    resp.raise_for_status()

    for item in resp.json():
        files.append(item["filename"])

    return files


def filter_files(pr_num, start_phrase="book/website", ignore_suffix=None):
    """Filter modified files from a Pull Request by a start phrase

    Arguments:
        pr_num {str} -- Number of the Pull Request to get modified files from

    Keyword Arguments:
        start_phrase {str} -- Start phrase to filter changed files by
                              (default: {"book/website"})

        ignore_suffix {str} -- File suffix or tuple of suffixes to ignore.


    Returns:
        {list} -- List of filenames that begin with the desired start phrase
    """
    files = get_files_from_pr(pr_num)
    filtered_files = []

    if ignore_suffix is None:
        ignore_suffix = ()

    for filename in files:
        if filename.startswith(start_phrase) and not filename.endswith(ignore_suffix):
            filtered_files.append(filename)

    return filtered_files


if __name__ == "__main__":
    args = parse_args()
    changed_files = filter_files(args.pull_request)
    print(changed_files)
