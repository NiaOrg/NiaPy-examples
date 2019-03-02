PYTHON=python
PVERSION=$(shell $(PYTHON) -c "import sys; print('%d.%d.%d' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro))")
PVERSIONS=$(shell $(PYTHON) -c "import sys; print('%d%d' % (sys.version_info.major, sys.version_info.minor))")

build: cec19_test_func.cpp cec19_test_func.h cec2019.pyx
	$(PYTHON) setup.py build_ext -i
	cp build/lib.linux-x86_64-$(PVERSION)/cec2018.cpython-$(PVERSIONS)m-x86_64-linux-gnu.so .

clean:
	rm cec2019.cpp
	rm -r build
	rm *.so
