PYTHON=python
PVERSION=$(shell $(PYTHON) -c "import sys; print('%d.%d.%d' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro))")
PVERSIONS=$(shell $(PYTHON) -c "import sys; print('%d%d' % (sys.version_info.major, sys.version_info.minor))")

build: cec8_test_func.cpp cec8_test_func.h data.h cec2008.pyx
	$(PYTHON) setup.py build_ext -i
	8cp build/lib.linux-x86_64-$(PVERSION)/cec2008.cpython-$(PVERSIONS)m-x86_64-linux-gnu.so .

clean:
	rm cec2008.cpp
	rm -r build
	rm *.so
