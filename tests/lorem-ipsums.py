#!/usr/bin/env python
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


def main():
    """Main function
	Checks for rogue "lorem ipsum"s in book content files and removes html
	comment identifiers from the files.

	Raises:
		Exception: Raises an exception if "lorem ipsum" is found in a book
					content file
	"""
    failed = []
    for root_dir, _, file_names in os.walk(directory_to_check):
        for file_name in file_names:
            file = open(
                os.path.join(root_dir, file_name), encoding="utf8", errors="ignore"
            )
            text = file.read()
            text = remove_comments(text)
            if "lorem ipsum" in text.lower():
                failed.append(file.name)

    if len(failed) != 0:
        error_message = '"Lorem ipsum"s found in the following files:\n' + "\n".join(
            failed
        )
        raise Exception(error_message)


if __name__ == "__main__":
    main()
