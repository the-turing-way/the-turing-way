import argparse
import json
import sys
from pathlib import Path
from typing import Any

import requests
from jsonschema.validators import Draft202012Validator


def get_schema() -> dict[Any, Any]:
    # Get all-contributorsrc schema from Schema Store
    schema = requests.get("https://json.schemastore.org/all-contributors.json").json()

    # Add _comment item to the schema, as we have added a comment explaining the file
    schema["properties"]["_comment"] = {
        'title': "Comment",
        'type': "string",
    }
    # Undocumented field added by the bot
    schema["properties"]["commitType"] = {
        'title': "Commit type (undocumented)",
        'type': "string",
    }

    return schema


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate all-contributorsrc file."
    )

    # Optionally allow the path to the all-contributors file to be specified upon execution
    parser.add_argument(
        "file",
        type=Path,
        nargs="?",
        default=Path(Path(__file__).parent.absolute() / "../.all-contributorsrc").resolve(),
        help="Path of the JSON file containing the contributor metadata.",
    )

    args = parser.parse_args()
    if not args.file.is_file():
        msg = f"Could not find 'all-contributorsrc' file at path {args.file}."
        raise FileExistsError(msg)

    # Create validator
    schema = get_schema()
    v = Draft202012Validator(schema)

    # Parse the all-contributorsrc file
    with open(args.file) as f:
        all_contributorsrc = json.load(f)

    # Collect validation errors
    errors = list(v.iter_errors(all_contributorsrc))

    if errors:
        print(f"{len(errors)} validation errors found in {args.file}.\n")

        # List errors
        for error in errors:
            print(error.message)
            print(f"At JSON path {error.json_path}\n")

        sys.exit(1)


if __name__ == "__main__":
    main()
