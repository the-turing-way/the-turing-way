# Default target
all: book

# Install build dependencies
deps:
	python -m pip install --upgrade pip
	pip install -r ./dependencies.lock

# Upgrade python packages and update the requirements files
upgrade:
	python -m pip install --upgrade pip
	pip install pip-tools
	pip-compile --upgrade ./dependencies.in
	pip-sync ./dependencies.lock

# Start a webserver serving the book locally
serve:
	cd website && jupyter-book start

# Build the book and export as HTML
book:
	cd website && jupyter-book build --html
	cd pt-br && jupyter-book build --html

# Build the book stopping on errors
strict:
	cd website && jupyter-book build --html --strict
	cd pt-br && jupyter-book build --html --strict

# Build the book in a non-interactive environment (for CI)
ci:
	cd website && jupyter-book build --html --ci
	cd pt-br && jupyter-book build --html --ci

# Clean any build outputs and artifacts
clean:
	jupyter-book clean --all --yes ./**/_build
