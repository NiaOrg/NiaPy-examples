PYTHON=python

build: cec15_test_func.cpp cec15_test_func.h cec2015.pyx
	$(PYTHON) setup.py build_ext -i

clean:
	rm cec2015.cpp
	rm -r build
	rm *.so
