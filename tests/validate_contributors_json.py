import argparse
import json
from pathlib import Path

import jsonschema
import requests


# Get all-contributorsrc schema from Schema Store
schema = requests.get("https://json.schemastore.org/all-contributors.json").json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Validate all-contributorsrc file."
    )

    # Optionally allow the path to the all-contributors file to be specified upon execution
    parser.add_argument(
        "file",
        type=Path,
        nargs="?",
        default=Path(Path(__file__).parent.absolute() / "../.all-contributorsrc"),
        help="Path of the JSON file containing the contributor metadata.",
    )

    args = parser.parse_args()
    if not args.file.is_file():
        msg = f"Could not find 'all-contributorsrc' file at path {args.file}."
        raise FileExistsError(msg)

    # Add _comment item to the schema, as we have added a comment explaining the file
    schema["properties"]["_comment"] = {
        'title': "Comment",
        'type': "string",
    }

    # Run the validation on the contributors metadata file
    with open(args.file) as f:
        contributors_metadata = json.load(f)

        # Run the schema validation on the loaded metadata
        # Will raise a ValidationError if the metadata does not match the schema
        jsonschema.validate(contributors_metadata, schema)
