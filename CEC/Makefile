MAKE:=make

install: Pipfile
	pipenv install

lab:
	pipenv run jupyter lab

uninstall: Pipfile.lock
	pipenv --rm
	rm Pipfile.lock
