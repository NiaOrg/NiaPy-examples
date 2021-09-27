PYTHON=python

build: cec13_test_func.cpp cec13_test_func.h cec2013.pyx
	$(PYTHON) setup.py build_ext -i

clean:
	rm cec2013.cpp
	rm -r build
	rm *.so
