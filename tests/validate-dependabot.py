import argparse
import json
import sys
from pathlib import Path
from typing import Any

import requests
import yaml
from jsonschema.validators import Draft202012Validator

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate Dependabot configuration."
    )

    # Optionally allow the path to the all-contributors file to be specified upon execution
    parser.add_argument(
        "file",
        type=Path,
        nargs="?",
        default=Path(Path(__file__).parent.absolute() / "../.github/dependabot.yaml").resolve(),
        help="Path to the Dependabot configuration",
    )

    args = parser.parse_args()
    if not args.file.is_file():
        msg = f"Could not find file at path {args.file}."
        raise FileExistsError(msg)

    # Create validator
    schema = requests.get("https://www.schemastore.org/dependabot-2.0.json").json()
    v = Draft202012Validator(schema)

    # Parse the Dependabot config
    with open(args.file) as f:
        all_contributorsrc = yaml.load(f, Loader=Loader)

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
