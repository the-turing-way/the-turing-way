all: pathways

deps:
	python -m pip install --upgrade pip
	pip install -r ./website/requirements.txt

book:
	jupyter-book build ./website

strict:
	jupyter-book build ./website -W --keep-going

pathways:
	python -m pathways.main pathways ./website/

clean:
	jupyter-book clean -a ./website
