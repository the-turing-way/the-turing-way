#!/usr/bin/env python3

import json
import shutil
from os.path import isfile
from pathlib import Path
from subprocess import run, PIPE
from fuzzywuzzy import fuzz, process

"""
This is a helper tool that compares the committers in the Git history of a 
repository to the names of people acknowledged in the allcontribtursrc file
in this repository.

Examples:
- Run the tool in the root of the repository:

    $ tools/didwegivecredit.py
    
- Run the tool on a repository in a different location:

    $ tools/didwegivecredit.py --path /path/to/root-directory

"""
# bots don't need acknowledgement even though they are doing a great job
bots = ['allcontributors[bot]', 'The Gitter Badger', 'dependabot[bot]']

def get_committers(path, since=None):
    """
    Find all contributors to a project from the Git commit history

    Args:
        path: str; Path to the root of the git repository

    Returns:
        committers: list; Names of committers
    """

    cmd = ["git", "shortlog", "-s"]
    # But if we were pointed to a different location...
    if path != Path.cwd():
        # ... we need to modify the git call
        cmd = ["git", "-C", str(path), "shortlog", "-s"]
    if since:
        # we want to specify a range
        cmd = cmd + ["{}..HEAD".format(since)]

    shortlog = run(cmd,
                   stdout=PIPE).stdout.decode().split('\n')

    committers = [c.split('\t', 1)[-1] for c in shortlog]

    return committers


def parse_allcontributors(allcontrib_file):
    """
    get the names and github handles of all contributors as acknowledged by
    the .allcontributorsrc file.

    Args:
        allcontrib_file: Path object
    Returns:
        allcontrib_names: list; names of contributors
        allcontrib_login: list; github handles of contributors
    """

    allcontrib = json.loads(allcontrib_file.read_text())
    allcontrib_names = [
        " ".join(val["name"].split(",")[::-1]).strip()
        for val in allcontrib["contributors"]
    ]
    allcontrib_login = [
        " ".join(val["login"].split(",")[::-1]).strip() for val in
        allcontrib["contributors"]
    ]
    return allcontrib_names, allcontrib_login


def match_authors(name, allcontrib_names, allcontrib_login):
    """
    Use fuzzy string matching to match names of committers
    to the names or handles mentioned in the allcontributors file.

    Args:
        name: str; name of committer
        allcontrib_names: list; names in allcontributorsrc file
        allcontrib_login: list; logins in allcontributorsrc file

    Returns:

    """

    # First, match the name. If no match, try Github login
    matching = process.extract(name,
                               allcontrib_names,
                               scorer=fuzz.token_sort_ratio,
                               limit=1)
    if matching[0][1] < 71:
        # we likely haven't found a match yet, lets check Github handles
        matching = process.extract(name,
                                   allcontrib_login,
                                   scorer=fuzz.token_sort_ratio,
                                   limit=1)
    if matching[0][1] >= 71:
        return [name, matching[0][0]], None
    else:
        return None, name


def add_emojis(message, emo, first=False):
    """
    If Python package emoji is installed, return plenty of emojis in output.
    Args:
        message: str;
        emoji: str;
    Returns: an emojified string
    """
    if emojize():
        import emoji
        msg = emoji.emojize(emo + message) if first \
            else emoji.emojize(message + emo)
    else:
        msg = message
    return msg


def report_on_missings(missings, path):
    """
    Summary report on potentially unaknowledged contributors
    Args:
        missings: list; Names of users

    Returns:
    """
    no = len(missings)
    if no == 0:
        msg = add_emojis("\nWonderful! I did not find commits of yet unacknowledged "
                         "contributors! ", ":dizzy:\n")
        print(msg)
    else:
        msg2 = add_emojis("\nThere are {} potentially unacknowledged "
                          "contributors to this repository.".format(no),
                          ":dizzy:\n")
        print(msg2)
        for i, name in enumerate(missings):
            author = '--author={}'.format(name)

            cmd = ["git", "shortlog", author]
            if path != Path.cwd():
                # ... we need to modify the git call
                cmd = ["git", "-C", str(path), "shortlog", author]

            commits = run(cmd,
                          stdout=PIPE).stdout.decode().splitlines()
            msg3 = add_emojis(" Number {}: {}\n"
                              "Here is what they have done:\n".format(i+1, name),
                              ":two_hearts:", first=True)
            print(msg3)
            for l in commits[1::]:
                print(l)


def generate_missings(committers,
                      bots,
                      allcontrib_names,
                      allcontrib_logins):
    """
    Find which committers are not mentioned in allcontributors file.

    Args:
        committers: list; names of all people that committed
        bots: list; names of all contributors to ignore
        allcontrib_names: list; names of all contributors in rc file
        allcontrib_logins: list; Github handles of all contributors in rc file

    Returns:
        missings: list; names of all committers who couldn't be matched
    """
    missings = []
    # check acknowledgements
    for name in committers:
        if name != '' and name not in bots:
            match, mismatch = match_authors(name,
                                            allcontrib_names,
                                            allcontrib_logins)
            if mismatch:
                missings.append(mismatch)

    return missings


def emojize():
    """
    Check whether the Python package emoji is installed.
    Returns:
        emoj: bool
    """
    emoj = True
    try:
        import emoji
    except ImportError:
        emoj = False
        pass
    return emoj


def main(path,
         allcontrib_file,
         since=None):
    """
    Query the repository for unacknowledged contributors.
    Basic usage: tools/didweacknowledge [--path path/to/repo/clone] [ --since <hash/tag>]

    """

    committers = get_committers(path, since)
    allcontrib_names, allcontrib_logins = parse_allcontributors(allcontrib_file)
    missings = generate_missings(committers,
                                 bots,
                                 allcontrib_names,
                                 allcontrib_logins)

    more_emojis = add_emojis("\n", ":sparkles:")
    msg = add_emojis("\nRunning the didwegivecredit helper to find out whether "
                     "people have committed to the repository {} and may not be "
                     "acknowledged in the.allcontributorsrc file. \n".format(path.resolve()),
                     ":sparkles:")
    print(more_emojis, msg)
    report_on_missings(missings, path)


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="{}".format(main.__doc__))
    parser.add_argument(
        "-p",
        "--path",
        help="""Provide a path to the root of a Git repository. 
        Default: Current directory""",
        default='.'
    )
    parser.add_argument(
        "-a",
        "--allcontributors",
        help="""Provide a path to the .allcontributorsrc file of your repostory.
        If not provided, it is assumed to be in the root of the provided path
        or current directory"""
    )
    parser.add_argument(
        "-s",
        "--since",
        help="""Specify a commit hash from when on the history should be checked.
        Example: ./didwegivecredit.py --since abb826407d5d7bf76""",
    )
    parser.add_argument(
        "-i",
        "--ignore-committer",
        nargs='+',
        help="""Specify the name of a committer to ignore in this run of the 
        script. To ignore a committer for all subsequent calls of this script,
        add their name to the bots list in the script (useful for bots)."""
    )
    args = parser.parse_args()

    if args.ignore_committer:
        names = args.ignore_committer
        for name in names:
            if name not in bots:
                bots.append(name)
            else:
                print("\n\nNote: I was told to ignore {}," 
                      " but I am already doing this!".format(name))
        print("\n\nCurrently, the following committers are ignored in this " 
              "run:\n{}".format(" \n".join(bots)))

    path = Path(args.path) if args.path else Path('.').resolve()

    if args.allcontributors:
        allcontrib_file = Path(args.allcontributors).resolve()
    else:
        allcontrib_file = path / ".all-contributorsrc"
    try:
        isfile(allcontrib_file)
    except FileNotFoundError:
        print("I couldn't find an .allcontributorsrc file in {}".format(
            allcontrib_file
        ))
        exit(1)

    since = args.since or None

    main(path, allcontrib_file, since)

