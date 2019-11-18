MAKE:=make

install: Pipfile
	pipenv install

lab:
	pipenv run jupyter lab

build17:
	cd cec2017
	$(MAKE) -C build

clean: Pipfile.lock
	pipenv --rm
	rm Pipfile.lock
