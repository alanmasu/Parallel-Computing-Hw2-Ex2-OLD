# Introduction to parallel computing - Homework 2 - Exercise 2
## Compiling and running the code
After download this repository on the UniTN cluster, we must request for an interactive session with the following command:
```bash
qsub -I -q short_cpuQ
```
Then we must load the modules for the Intel compiler:
```bash
module load gcc-7.5.0
```
So I have created some script that allow us to compile and run the code. The important scripts are:
- `env-configurations.sh`: set the python virtual environment for making the plots.
  This script will not execute heavy code or heavy computation; it will only set the environment.
- `doStrongScaling.sh`: compile the code with GCC and make a strong scaling test. As the previus script, it needs `env-configurations.sh` to be executed before for the same reasons.
- `pythonStrongScaling.sh`: this script only use the python virtual environment to make the plots of the strong scaling test. It needs `env-configurations.sh` but will not execute the main program.
- `pythonCharts.sh`: this script only use the python virtual environment to make the plot of the WallTime over the matrix size. It needs `env-configurations.sh` but will not execute the main program.