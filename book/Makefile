all: pathways

deps:
	python -m pip install --upgrade pip
	pip install -r ./website/requirements.txt

book:
	jupyter-book build ./website

strict:
	jupyter-book build ./website -W --keep-going

pathways:
	pathways ./website/ --build

clean:
	jupyter-book clean -a ./website
