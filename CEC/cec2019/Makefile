PYTHON=python

build: cec19_test_func.cpp cec19_test_func.h cec2019.pyx
	$(PYTHON) setup.py build_ext -i

clean:
	rm cec2019.cpp
	rm -r build
	rm *.so
