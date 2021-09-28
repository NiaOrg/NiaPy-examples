PYTHON=python

build: cec17_test_func.cpp cec17_test_func.h cec2017.pyx
	$(PYTHON) setup.py build_ext -i

clean:
	rm cec2017.cpp
	rm -r build
	rm *.so
