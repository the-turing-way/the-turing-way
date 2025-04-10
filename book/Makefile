all: pathways

deps:
	python -m pip install --upgrade pip
	pip install -r ./website/requirements.txt

upgrade:
	python -m pip install --upgrade pip
	pip install pip-tools
	pip-compile --upgrade ./website/requirements.in
	pip-sync ./website/requirements.txt

book:
	cd website && jupyter-book build --html

serve:
	cd website && jupyter-book start

strict:
	cd website && jupyter-book build --html --strict

ci:
	cd website && jupyter-book build --html --ci --strict --link-checker=false

pathways:
	pathways ./website/

clean:
	jupyter-book clean -a ./website
