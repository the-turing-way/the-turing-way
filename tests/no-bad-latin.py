#!/usr/bin/env python3
import os
import re
import sys


script_dir = os.path.dirname(__file__)
directory_to_check = os.path.join(script_dir, "../book/content/")


def remove_comments(text_string):
    """Function to omit  html comment identifiers in a text string using
	regular expression matches

	Arguments:
		text_string {string} -- The text to be matched

	Returns:
		{string} -- The input text string with html comments removed
	"""
    p = re.sub("(?s)<!--(.*?)-->", "", text_string)
    return p


def get_lines(text_string, sub_string):
    """Get individual lines in a text file

	Arguments:
		text_string {string} -- The text string to test
		sub_string {string} -- The conditional string to perform splitting on

	Returns:
		{list} -- A list of split strings
	"""
    lines = [line for line in text_string.split("\n") if sub_string in line]
    return lines


def get_files(directory):
    """Get a list of files to be checked. Ignores image files.

	Arguments:
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


def read_and_check_files(files):
    """Function to read in files, remove html comments and check for bad latin
	phrases

	Arguments:
		files {list} -- List of filenames to be checked

	Returns:
		{dict} -- Dictionary: Top level keys are absolute filepaths to files
		          that failed the check. Each of these has two keys:
				  'latin_type' containing the unwanted latin phrase, and 'line'
				  containing the offending line.
	"""
    failing_files = {}
    bad_latin = ["i.e.", "e.g.", "e.t.c.", " etc", " ie", "et cetera"]

    for filename in files:
        with open(filename, encoding="utf8", errors="ignore") as f:
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

    return failing_files


def construct_error_message(files_dict):
    """Function to construct an error message pointing out where bad latin
	phrases appear in lines of text

	Arguments:
		files_dict {dictionary} -- Dictionary of failing files containing the
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


def main():
    files = get_files(directory_to_check)
    failing_files = read_and_check_files(files)

    if bool(failing_files):
        error_message = construct_error_message(failing_files)
        raise Exception(error_message)


if __name__ == "__main__":
    main()
