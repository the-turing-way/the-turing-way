all: pathways

deps:
	python -m pip install --upgrade pip
	pip install -r ./website/requirements.txt

book:
	cd website && jupyter-book build --html

strict:
	cd website && jupyter-book build --html --strict

ci:
	cd website && jupyter-book build --html --ci

pathways:
	pathways --build ./website/

clean:
	jupyter-book clean -a ./website
