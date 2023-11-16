/*                      INTRODUCTION TO PARALLEL COMPUTING - Prof. VELLA 

    Student: Alan Masutti - 226901 - alan.masutti@studenti.unitn.it

    Assignment 2 - Exercise 2:
      This exercise consists of creating a program for parallel matrix transposition using OpenMP. The
      program must efficiently handle matrices of real numbers. The tasks to be performed are:
      - T1: Serial matrix transposition:
            Implement a serial matrix transpose algorithm for matrices of real numbers. Define a function
            matT that takes an input matrix A and returns its transpose. Define a second function matBlockT
            that takes an input matrix A and returns its transpose, calculating the transpose in blocks as
            shown in the picture.
      - T2: Parallel matrix transpose:
            Parallelize the matrix transpose operation using OpenMP for matrices of real numbers. Create a
            matTpar function that takes the same input as the serial version and parallelizes the algorithm.
            Experiment with OpenMP directives to improve performance. Explore different algorithms to
            find the most efficient one.
      - T3: Parallel transpose of block matrices:
            Implement a parallel matrix transpose by dividing the matrix into blocks and transposing these
            blocks. Create a function matBlockTpar that takes the same input as the serial version, divides
            the matrix into blocks, and computes its transpose using the block division. Each block must be
            transposed, and the final transposed matrix is constructed from these blocks. Experiment with
            different block sizes and different OpenMP directives to optimize performance.
      - T4: Performance analysis:
            Evaluate the performance and scalability of both parallel matrix transpose methods (with blocks
            and without blocks). Calculate the speedup and efficiency gains for different matrix sizes and
            thread counts. Consider for this task the time of the routine and compute the bandwidth as performance metrics. Identify possible bottlenecks or problems and propose optimizations. Compare the performance of normal transpose and block-based transpose. Discuss
            the differences that may appear in parallelization algorithms when you are working with dense
            or sparse matrices.

    Notes:

*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <stdint.h>

double randomD(int min, int max, int prec){ 
  prec = 10 * prec; 
  return (rand() % (max * prec - min * prec + 1) + min * prec) / (double)prec; 
}

uint64_t matT (double *A, double *B, int n){
  int r, c;
  struct timespec start, end;
  
  clock_gettime(CLOCK_MONOTONIC, &start);
  for (r = 0; r < n; r++){
    for (c = 0; c < n; c++){
      B[c*n+r] = A[r*n+c];
    }
  }
  clock_gettime(CLOCK_MONOTONIC, &end);
  return (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_nsec - start.tv_nsec) / 1000;
}

uint64_t matBlockT(double *A, double *B, int n, int bs){
  struct timespec start, end;
  int r, c, br, bc;
  clock_gettime(CLOCK_MONOTONIC, &start);
  for (r = 0; r < n; r += bs){
    for (c = 0; c < n; c += bs){
      for (br = r; br < r+bs; br++){
        for (bc = c; bc < c+bs; bc++){
          B[bc*n+br] = A[br*n+bc];
        }
      }
    }
  }
  clock_gettime(CLOCK_MONOTONIC, &end);
  return (end.tv_sec - start.tv_sec) * 1000000 + (end.tv_nsec - start.tv_nsec) / 1000;
}
int main(int argc, char const *argv[]){
  int n, bs;
#ifndef N
  do{
    printf("Insert the size of the matrix: ");
    scanf("%d", &n);
  }while(n != 0);
#else
  n = N;
#endif

#ifndef BS
  do{
    printf("Insert the block size: ");
    scanf("%d", &bs);
  }while(bs != 0);
#else
  bs = BS;
#endif

  double *A  = (double *)malloc(n*n*sizeof(double));
  double *At = (double *)malloc(n*n*sizeof(double));

  for(int i = 0; i < n*n; i++){
    A[i] = randomD(0, 100, 4);
  }

  //Print matrix
  printf("Matrix A:\n");
  for(int i = 0; i < n*n; i++){
    printf("%f\t", A[i]);
    if((i+1)%n == 0)
      printf("\n");
  }

  uint64_t t = matT(A, At, n);
  printf("Time for serial transpose: %ld us\n", t);

  printf("Matrix A trasnposed:\n");
  for(int i = 0; i < n*n; i++){
    printf("%f\t", At[i]);
    if((i+1)%n == 0)
      printf("\n");
  }

  return 0;
}
