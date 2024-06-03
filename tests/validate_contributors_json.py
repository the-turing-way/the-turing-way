import argparse
import json
from pathlib import Path
import jsonschema


def validate_contributor_metadata(contributors_filepath: Path):
    """Check if the the specified file is error-free JSON, and its content matches the
    all-contributors schema. If not, then raise a JSONDecodeError or ValidationError respectively.

    Keyword Arguments:
        contributors_filepath {Path} -- Filepath of the JSON file containing contributors' metadata
    """

    # Load the schema specification that the all-contributors JSON must follow
    contributor_schema = None
    with open("./tests/all-contributors.schema.json") as f:
        contributor_schema = json.load(f)

    # Try to load the all-contributors metadata
    # Will raise a JSONDecodeError if there's a problem parsing the JSON
    contributors_metadata = None
    with open(contributors_filepath) as f:
        contributors_metadata = json.load(f)

    # Run the schema validation on the loaded metadata
    # Will raise a ValidationError if the metadata does not match the schema
    jsonschema.validate(contributors_metadata, contributor_schema)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to validate the array of contributor objects in the all-contributors JSON file")

    # Optionally allow the path to the all-contributors file to be specified upon execution
    parser.add_argument(
        "--all-contributors-filepath",
        type=str,
        default="./.all-contributorsrc",
        help="Path of the JSON file containing the contributor metadata",
    )
    args = parser.parse_args()
    all_contributors_filepath = Path(args.all_contributors_filepath)
    if not all_contributors_filepath.exists():
        raise FileExistsError(f"Could not find 'all-contributorsrc' file at path {all_contributors_filepath}")

    # Run the validation on the contributors metadata file
    validate_contributor_metadata(all_contributors_filepath)
