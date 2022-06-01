"""
Script to update citation.cff file and validate it then draft a release note.
"""
from datetime import datetime

from ruamel.yaml import YAML

# Configure the YAML parser
yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.allow_duplicate_keys = True
yaml.explicit_start = False
yaml.preserve_quotes = True


def update_citation_file(citation_file_path):
    with open(citation_file_path) as stream:
        file_content = yaml.load(stream)

    major, minor, tiny = file_content["version"].split(".")
    major, minor, tiny = int(major), int(minor), int(tiny)

    # Maybe we want to provide an input to determine what the release version
    # should be? Here we are restricting the patch and minor versions to be less
    # than or equal to 10, but there's nothing in semver practices that enforces this.
    tiny += 1
    if (tiny > 10) and (minor < 10):
        tiny = 0
        minor += 1
    elif (tiny > 10) and (minor > 10):
        minor = 0
        major += 1

    file_content["version"] = f"{major}.{minor}.{tiny}"

    file_content["date-released"] = datetime.today().strftime("%Y-%m-%d")

    with open(citation_file_path, "w") as fp:
        yaml.dump(file_content, fp)


if __name__ == "__main__":
    citation_file_path = "../CITATION.cff"
    update_citation_file(citation_file_path)
