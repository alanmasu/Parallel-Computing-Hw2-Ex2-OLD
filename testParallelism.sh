if test -f "a.out"; then
    rm a.out
fi

export OMP_NUM_THREADS=4
for dim in 512 1024 2048 4096 8192
do
    gcc-7.5.0 ./src/main.c ./src/ex2.c -DN=$dim -DBS=64 -DPRINT -fopenmp -DCOMPILATION_NOTES="\"TEST_PARALLELISM;4\"" -DRUN_DESCRIPTION="\"Test parallelism whit collapse(2)\""
    ./a.out
done

source pytonCharts.sh