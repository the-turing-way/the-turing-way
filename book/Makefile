.DEFAULT_GOAL := help
.PHONY: help

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| sed -n 's/^\(.*\): .*## \(.*\)/\1\t\2/p' \
	| column -t -s $$'\t'

deps: ## Install build dependencies
	python -m pip install --upgrade pip
	pip install -r ./requirements.txt

upgrade: ## Upgrade python packages and update the requirements files
	python -m pip install --upgrade pip
	pip install pip-tools
	pip-compile --upgrade
	pip-sync

serve: ## Start a webserver serving the book locally
	cd website && jupyter-book start

book: ## Build the book and export as HTML
	cd website && jupyter-book build --html
	# Temporary hack to remove unused thebe JS
	rm website/_build/html/*thebe*.js

strict: ## Build the book stopping on errors
	cd website && jupyter-book build --html --strict
	# Temporary hack to remove unused thebe JS
	rm website/_build/html/*thebe*.js

ci: ## Build the book in a non-interactive environment (for CI)
	cd website && jupyter-book build --html --ci
	# Temporary hack to remove unused thebe JS
	rm website/_build/html/*thebe*.js

ast: ## Build AST only
	cd website && jupyter-book build

clean: ## Clean any build outputs and artifacts
	jupyter-book clean --all --yes ./website/_build
