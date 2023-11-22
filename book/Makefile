all: pathways

deps:
	python -m pip install --upgrade pip
	pip install -r ./website/requirements.txt

book:
	jupyter-book build ./website

pathways:
	python -m pathways.main pathways ./website/

clean:
	jupyter-book clean -a ./website
