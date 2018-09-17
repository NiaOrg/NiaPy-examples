PYTHON=python
PVERSION=$(shell $(PYTHON) -c "import sys; print('%d.%d.%d' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro))")
PVERSIONS=$(shell $(PYTHON) -c "import sys; print('%d%d' % (sys.version_info.major, sys.version_info.minor))")

build: cec6_test_func.cpp cec6_test_func.h data.h cec2006.pyx
	$(PYTHON) setup.py build_ext -i
	cp build/lib.linux-x86_64-$(PVERSION)/cec2006.cpython-$(PVERSIONS)m-x86_64-linux-gnu.so .

clean:
	rm cec2006.cpp
	rm -r build
	rm *.so
