"""
Script to update citation.cff file and validate it then draft a release note.
"""
import argparse
from datetime import datetime

def read_from_file(infile):
    with open(infile, "r", encoding="utf8") as fid:
        return fid.readlines()

def int_to_version(major, minor, tiny):
    return f"{major}.{minor}.{tiny}"

def update_citation_file(citation_file_path):
    file_content = read_from_file(citation_file_path)
    for idx, line in enumerate(file_content):
        word_array = line.split(" ")
        if ("version:" in word_array):
            major, minor, tiny = map(int, word_array[1].split("."))

            tiny = tiny + 1
            if (tiny > 10 and minor < 10):
                tiny = 0
                minor = minor + 1
            elif (tiny > 10 and minor > 10):
                minor = 0
                major = major + 1

            version_number_str = str(major) + "." + str(minor) + "." + str(tiny) + "\n"

            file_content[idx] = "version: " + version_number_str
        elif ("date-released:" in word_array):

            file_content[idx] = "date-released: " + "\"" + datetime.today().strftime("%Y-%m-%d") + "\" \n"
        else:
            file_content[idx] = line

    with open(citation_file_path, "w", encoding="utf8") as file:
        file.writelines(file_content)

if __name__ == "__main__":
    citation_file_path = "../CITATION.cff"
    update_citation_file(citation_file_path)



