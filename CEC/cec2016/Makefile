PYTHON=python

build: cec16_test_func.cpp cec16_test_func.h cec2016.pyx
	$(PYTHON) setup.py build_ext -i

clean:
	rm cec2016.cpp
	rm -r build
	rm *.so
