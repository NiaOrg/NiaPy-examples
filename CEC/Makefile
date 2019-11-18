MAKE:=make

install: Pipfile
	pipenv install

lab:
	pipenv run jupyter lab

clean: Pipfile.lock
	pipenv --rm
	rm Pipfile.lock
