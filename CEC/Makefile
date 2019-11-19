MAKE:=make

install: Pipfile
	pipenv install

lab:
	pipenv run jupyter lab

shell:
	pipenv shell

uninstall: Pipfile.lock
	pipenv --rm
	rm Pipfile.lock
