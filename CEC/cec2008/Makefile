PYTHON=python

build: cec8_test_func.cpp cec8_test_func.h data.h cec2008.pyx
	$(PYTHON) setup.py build_ext -i

clean:
	rm cec2008.cpp
	rm -r build
	rm *.so
