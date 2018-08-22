PYTHON=python
PVERSION=$(shell $(PYTHON) -c "import sys; print('%d.%d.%d' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro))")
PVERSIONS=$(shell $(PYTHON) -c "import sys; print('%d%d' % (sys.version_info.major, sys.version_info.minor))")

build: cec16_test_func.cpp cec16_test_func.h cec2016.pyx
	$(PYTHON) setup.py build_ext -i
	cp build/lib.linux-x86_64-$(PVERSION)/cec2016.cpython-$(PVERSIONS)m-x86_64-linux-gnu.so .

clean:
	rm cec2016.cpp
	rm -r build
	rm *.so
