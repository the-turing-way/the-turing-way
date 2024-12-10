import os
import re
import argparse
from pull_files import filter_files

HERE = os.getcwd()
ABSOLUTE_HERE = os.path.dirname(HERE)
IGNORE_LIST = ["config.yml", "style.md", "contributors-record.md", "references.bib"]


def parse_args():
    """Construct command line interface for parsing Pull Request number"""
    DESCRIPTION = "Script to check for latin phrases in Markdown files"
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "--pull-request",
        type=str,
        default=None,
        help="If the script is being run on a Pull Request, parse the PR number",
    )

    return parser.parse_args()


def remove_comments(text_string):
    """
    Function to omit  html comment identifiers in a text string using
    regular expression matches.

    Arguments:
        text_string {string} -- The text to be matched

    Returns:
        {string} -- The input text string with html comments removed
    """
    p = re.sub("(?s)<!--(.*?)-->", "", text_string)
    return p


def get_lines(text_string, sub_string):
    """
    Get individual lines in a text file.

    Arguments:
        text_string {string} -- The text string to test
        sub_string {string} -- The conditional string to perform splitting on

    Returns:
        {list} -- A list of split strings
    """
    lines = [line for line in text_string.split("\n") if sub_string in line]
    return lines


def construct_error_message(files_dict):
    """
    Function to construct an error message pointing out where bad latin
    phrases appear in lines of text.

    Arguments:
        files_dict {dictionary} -- Dictionary of failing files containing
                                   bad latin phrases and offending lines

    Returns:
{string} -- The error message to be raised
    """
    error_message = ["Bad latin found in the following files:\n"]

    for file in files_dict.keys():
        error_message.append(
            f"{file}:\t{files_dict[file]['latin_type']}\tfound in line\t[{files_dict[file]['line']}]\n"
        )

    return "\n".join(error_message)


def read_and_check_files(files):
    """
    Function to read in files, remove html comments and check for bad latin phrases.

    Arguments:
        files {list} -- List of filenames to be checked

    Returns:
        {dict} -- Dictionary: Top level keys are absolute filepaths to files
                  that failed the check. Each of these has two keys:
                  'latin_type' containing the unwanted latin phrase, and 'line'
                  containing the offending line.
    """
    failing_files = {}
    bad_latin = ["i.e.", "e.g.", "e.t.c.", " etc", " ie ", "et cetera"]

    for filename in files:
        if os.path.basename(filename) in IGNORE_LIST:
            pass
        else:
            try:
                with open(
                os.path.join(ABSOLUTE_HERE, filename), encoding="utf8",
                errors="ignore") as f:
                    text = f.read()
                    text = remove_comments(text)

                    for latin_type in bad_latin:
                        if latin_type in text.lower():
                            lines = get_lines(text.lower(), latin_type)
                            for line in lines:
                                failing_files[os.path.abspath(filename)] = {
                                    "latin_type": latin_type,
                                    "line": line,
                                }
            except FileNotFoundError:
                pass

    return failing_files


def get_all_files(directory=os.path.join(ABSOLUTE_HERE, "book", "website")):
    """
    Get a list of files to be checked. Ignores image files.

    Keyword Arguments:
        directory {string} -- The directory containing the files to check

    Returns:
        {list} -- List of files to check
    """
    files = []
    filetypes_to_ignore = (".png", ".jpg")

    for rootdir, _, filenames in os.walk(directory):
        for filename in filenames:
            if not filename.endswith(filetypes_to_ignore):
                files.append(os.path.join(rootdir, filename))

    return files


def main():
    """Main function"""
    args = parse_args()

    if args.pull_request is not None:
        files = filter_files(args.pull_request, ignore_suffix=('.jpg', '.png'))
    else:
        files = get_all_files()

    failing_files = read_and_check_files(files)

    if bool(failing_files):
        error_message = construct_error_message(failing_files)
        raise Exception(error_message)


if __name__ == "__main__":
    main()
