# Default target
all: book

# Install build dependencies
deps:
	python -m pip install --upgrade pip
	pip install -r ./website/requirements.txt

# Upgrade python packages and update the requirements files
upgrade:
	python -m pip install --upgrade pip
	pip install pip-tools
	pip-compile --upgrade ./website/requirements.in
	pip-sync ./website/requirements.txt

# Start a webserver serving the book locally
serve:
	cd website && jupyter-book start

# Build the book and export as HTML
book:
	cd website && jupyter-book build --html

# Build the book stopping on errors
strict:
	cd website && jupyter-book build --html --strict

# Build the book in a non-interactive environment (for CI)
ci:
	cd website && jupyter-book build --html --ci

# Write pathways to your local copy of the book
pathways:
	pathways ./website/

# Clean any build outputs and artifacts
clean:
	jupyter-book clean --all --yes ./website/_build
