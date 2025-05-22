#!/usr/bin/env python3
import sys
import json
import tomllib
import traceback
import argparse
from pathlib import Path

from unist import *

# --- Path Configuration ---
SCRIPT_DIR = Path(__file__).resolve().parent
FIGURES_DIR = SCRIPT_DIR / "figures"
TOML_IMG_PATH = FIGURES_DIR / "images_metadata.toml"

# --- Styling Configuration ---
LAYOUT_STYLE = {
    "display": "inline-block",
    "borderRadius": 8,
    "color": "white",
    "padding": 5,
    "margin": 5,
}

DEFAULT_STYLE = {
    "background": "#009e9cff",
    **LAYOUT_STYLE,
}  # Default style for all tags


# --- Data Loading ---
def load_image_data(toml_path: Path = TOML_IMG_PATH) -> list:
    """
    Load image metadata from a TOML file.

    Parameters
    ----------
    toml_path : pathlib.Path, optional
        Path to the TOML file containing image metadata. Defaults to `TOML_IMG_PATH`.

    Returns
    -------
    list of dict
        A list of dictionaries, each containing metadata for an image.

    Raises
    ------
    FileNotFoundError
        If the TOML file is not found at the specified path.

    tomllib.TOMLDecodeError
        If the TOML file cannot be parsed properly.
    """
    print(f"Loading image data from {toml_path}", file=sys.stderr, flush=True)
    try:
        with toml_path.open("rb") as f:
            data = tomllib.load(f)
        return data.get("images", [])
    except FileNotFoundError:
        print(f"Error: Image data file not found at {toml_path}", file=sys.stderr)
        return []
    except tomllib.TOMLDecodeError as e:
        print(f"Error parsing TOML file {toml_path}: {e}", file=sys.stderr)
        return []


# --- Image Rendering ---
def render_image(image_data: dict) -> dict:
    """
    Render a single image as a MyST card component.

    Parameters
    ----------
    image_data : dict
        Dictionary containing image metadata, with keys like 'filename', 'alt-text', and 'tags'.

    Returns
    -------
    dict or None
        A dictionary representing a MyST card node, or None if an error occurred during rendering.

    Raises
    ------
    KeyError
        If required keys are missing in the image_data dictionary.

    Exception
        For any other unexpected error during rendering (printed to stderr).
    """
    try:
        # Extract image data from the toml file
        filename = image_data["filename"]
        alt_text = image_data.get("alt-text", "")
        tags = image_data.get("tags", [])
        image_path = FIGURES_DIR / filename
        rel_image_path = image_path.absolute().as_posix()

        # Build tags for the card
        tag_spans = [span([text(tag_name)], style=DEFAULT_STYLE) for tag_name in tags]

        # Create the card components
        children = [
            image(str(rel_image_path), alt=alt_text),
            div(tag_spans),
        ]

        # Add alt-text as a card description if it exists
        if alt_text:
            children.append({"type": "cardDescription", "children": [text(alt_text)]})

        return {
            "type": "card",
            "children": children,
        }
    except Exception as err:
        print(
            f"\n\nError rendering image: {image_data.get('filename', 'Unknown')}",
            file=sys.stderr,
        )
        traceback.print_exception(err, file=sys.stderr)
        return None


def render_images() -> list:
    """
    Load image metadata and render all images

    Returns
    -------
    list of dict
        A list of successfully rendered MyST card nodes.
    """
    # Load image data if they have a filename
    images_data = [img for img in load_image_data() if "filename" in img]
    print(f"Found {len(images_data)} images to render.", file=sys.stderr, flush=True)
    rendered_images = [render_image(data, this_dir) for data in images_data]
    # Use the pool to map render_image over the list of images, filtering out any None results
    return [card for card in rendered_images if card is not None]


# --- MyST Directive and Transform Logic ---
def run_directive(name: str, data: dict) -> list:
    """
    Process a custom directive in a MyST document.

    Parameters
    ----------
    name : str
        The name of the directive to process.

    data : dict
        Parsed MyST document in unist-compatible JSON format.


    Returns
    -------
    list of dict
        A list containing a single placeholder node for the directive.

    Raises
    ------
    AssertionError
        If the provided directive name is not 'image-gallery-dir'.
    """
    assert name == "image-gallery-dir"
    return [
        {
            "type": "image-gallery-dir",
            "children": [],
            "this-dir": data.get("options", {}).get("this-dir"),
        }
    ]


def run_transform(name, data) -> dict:
    """
    Replace directive nodes in a MyST document with a rendered image grid.

    Parameters
    ----------
    name : str
        The name of the transform to run.

    data : dict
        Parsed MyST document in unist-compatible JSON format.

    Returns
    -------
    dict
        Transformed MyST document with nodes replaced by rendered image cards.
    """
    # Find custom 'image-gallery-dir' nodes
    gallery_nodes = find_all_by_type(data, "image-gallery-dir")

    if not gallery_nodes:
        print(
            "No 'image-gallery-dir' directive found in the document.",
            file=sys.stderr,
            flush=True,
        )
        return data

    # Render all image cards
    children = render_images()

    # Replace each 'image-gallery-dir' node with grid of cards
    for node in gallery_nodes:
        node.clear()
        node.update(grid([1, 1, 1, 2], children))
        node["children"] = children

    return data


# --- Plugin Specification for MyST ---
imageGalleryDirective = {
    "name": "image-gallery-dir",
    "doc": "A directive for embedding a gallery of images with alt text and tags.",
    "options": {
        "this-dir": {
            "type": "string",
            "doc": "Path to the directory of the file embedding the gallery",
        }
    },
}

imageGalleryTransform = {
    "stage": "document",
}

PLUGIN_SPEC = {
    "name": "Image Gallery Plugin",
    "directives": [imageGalleryDirective],
    "transforms": [imageGalleryTransform],
}

# --- Main Execution Block ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--role")
    group.add_argument("--directive")
    group.add_argument("--transform")
    args = parser.parse_args()

    if args.directive:
        # Validate/process the directive
        data = json.load(sys.stdin)
        json.dump(run_directive(args.directive, data), sys.stdout)
    elif args.transform:
        # Run the document transformation
        data = json.load(sys.stdin)
        json.dump(run_transform(args.transform, data), sys.stdout)
    elif args.role:
        raise NotImplementedError("Roles are not implemented for this plugin.")
    else:
        # Get the plugin specification
        json.dump(PLUGIN_SPEC, sys.stdout)
