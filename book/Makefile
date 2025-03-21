all: pathways

deps:
	python -m pip install --upgrade pip
	pip install -r ./website/requirements.txt

book:
	cd website && jupyter-book build --html

serve:
	cd website && jupyter-book start

strict:
	cd website && jupyter-book build --html --strict

ci:
	cd website && jupyter-book build --html --ci

pathways:
	pathways ./website/
	cd website && jupyter-book build --html

clean:
	jupyter-book clean -a ./website
