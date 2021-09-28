PYTHON=python

build: cec21_test_func.cpp cec21_test_func.h cec2021.pyx
	$(PYTHON) setup.py build_ext -i

setup: requirements.txt
	pip3 install -r requirements.txt

clean:
	rm cec2021.cpp
	rm -r build
	rm *.so
