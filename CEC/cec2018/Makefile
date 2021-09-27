PYTHON=python

build: cec18_test_func.cpp cec18_test_func.h cec2018.pyx
	$(PYTHON) setup.py build_ext -i

clean:
	rm cec2018.cpp
	rm -r build
	rm *.so
