gcc-7.5.0 ./src/main.c -DN=4096 -DBS=2 -fopenmp
export OMP_NUM_THREADS=4
./a.out