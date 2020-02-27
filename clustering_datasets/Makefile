install: Pipfile
	pipenv install
	pipenv run jupyter labextension install @jupyter-widgets/jupyterlab-manager
	pipenv run jupyter labextension install jupyter-matplotlib
	pipenv run jupyter labextension install @jupyterlab/toc
	pipenv run jupyter labextension install @oriolmirosa/jupyterlab_materialdarker
	pipenv run jt -t onedork -lineh 110 -nfs 10 -fs 10 -tfs 10 -cellw 80%

run:
	pipenv run jupyter lab

lab:
	pipenv run jupyter lab

notebook:
	pipenv run jupyter notebook

console:
	pipenv run ipython

clean: Pipfile.lock
	pipenv --rm
	rm Pipfile.lock

all: install run 
