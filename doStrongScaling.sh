if test -f "a.out"; then
    rm a.out
fi
echo "Doing Strong Scaling"
for i in {0..4}
do
    echo "- $i -------------------"
    echo "Serial Code"
    gcc-7.5.0 ./src/main.c ./src/ex2.c -DCOMPILATION_NOTES="\"STRONG_SCALING;SERIAL_CODE\"" -DN=4096 -DBS=256 -DPRINT
    ./a.out
    echo "-------------------"
    echo ""
    for i in 1 2 4 8 16 32 64
    do  
        echo "Parallel Code with $i threads"
        echo "-------------------"
        gcc-7.5.0 ./src/main.c ./src/ex2.c -DCOMPILATION_NOTES="\"STRONG_SCALING;$i\"" -fopenmp -DN=4096 -DBS=256 -DPRINT
        export OMP_NUM_THREADS=$i
        ./a.out
        echo "-------------------"
        echo ""
    done
done

source pytonStrongScalingCharts.sh
echo "Done Strong Scaling"
echo "-------------------"