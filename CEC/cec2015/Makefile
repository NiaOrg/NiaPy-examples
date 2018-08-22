PYTHON=python
PVERSION=$(shell $(PYTHON) -c "import sys; print('%d.%d.%d' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro))")

build: cec15_test_func.cpp cec15_test_func.h
	$(PYTHON) setup.py build_ext -i
	cp build/lib.linux-x86_64-3.7/cec2015.cpython-37m-x86_64-linux-gnu.so .

clean:
	rm cec2015.cpp
	rm -r build
	rm *.so
