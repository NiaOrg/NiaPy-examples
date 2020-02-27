MAKE:=make

install: Pipfile
	pipenv install

lab:
	pipenv run jupyter lab

shell:
	pipenv shell

uninstall:
	pipenv --rm
	-rm Pipfile.lock
