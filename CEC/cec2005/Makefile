PYTHON=python
PVERSION=$(shell $(PYTHON) -c "import sys; print('%d.%d.%d' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro))")

build: cec5_test_func.cpp cec5_test_func.h data.h cec2005.pyx
	$(PYTHON) setup.py build_ext -i
	cp build/lib.linux-x86_64-3.7/cec2005.cpython-37m-x86_64-linux-gnu.so .

clean:
	rm cec2005.cpp
	rm -r build
	rm *.so
