CC:=g++

build: cec17_test_func.cpp cec17_test_func.h
	$(CC) -O3 -fPIC -shared -o cec2017.so cec17_test_func.cpp cec17_test_func.h

clean: cec2017.so
	rm cec2017.so
