PYTHON=python

build: cec14_test_func.cpp cec14_test_func.h cec2014.pyx
	$(PYTHON) setup.py build_ext -i

clean:
	rm cec2014.cpp
	rm -r build
	rm *.so
