if test -f "a.out"; then
    rm a.out
fi

gcc-7.5.0 ./src/main.c ./src/ex2.c -DN=8 -DBS=2 -DDEBUG -DPRINT -fopenmp 
echo "---------"
export OMP_NUM_THREADS=1
./a.out
echo "---------"
export OMP_NUM_THREADS=2
./a.out
echo "---------"
export OMP_NUM_THREADS=4
./a.out