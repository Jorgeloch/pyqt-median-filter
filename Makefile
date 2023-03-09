.PHONY : clean

all : libmediana.so

libmediana.so : mediana.o
	gcc -shared -o libmediana.so mediana.o

mediana.o : mediana.c
	gcc -c -fPIC mediana.c -o mediana.o

clean :
	-rm -vf mediana.so mediana.o