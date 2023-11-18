gcc-7.5.0 ./src/main.c ./src/ex2.c -DCOMPILATION_NOTES="\"SERIAL_CODE\""
./a.out
source graphEnv/bin/activate
python3 utils/chart.py
deactivate