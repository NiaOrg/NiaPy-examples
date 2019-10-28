PYTHON=python
PVERSION=$(shell $(PYTHON) -c "import sys; print('%d.%d.%d' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro))")
PVERSIONS=$(shell $(PYTHON) -c "import sys; print('%d%d' % (sys.version_info.major, sys.version_info.minor))")

build: cec15_test_func.cpp cec15_test_func.h
	$(PYTHON) setup.py build_ext --inplace

clean:
	rm cec2015.cpp
	rm -r build
	rm *.so
