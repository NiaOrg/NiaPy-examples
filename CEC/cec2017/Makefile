CC:=gcc
CC_FLAGS:=-std=c99 -O3 -march=native

build: cec17_test_func.c
	${CC} -Wall -fPIC ${CC_FLAGS} -c cec17_test_func.c
	${CC} -shared -W -o cec2017.so cec17_test_func.o -lm

clean: cec2017.so
	rm cec2017.so
