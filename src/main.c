/*                      INTRODUCTION TO PARALLEL COMPUTING - Prof. VELLA 

    Student: Alan Masutti - 226901 - alan.masutti@studenti.unitn.it

    Assignment 2 - Exercise 2:
      This exercise consists of creating a program for parallel matrix transposition using OpenMP. The
      program must efficiently handle matrices of real numbers. The tasks to be performed are:
      - T1: Serial matrix transposition: [DONE]
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

#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>

#include "ex2.h"

#ifndef COMPILATION_NOTES
    #define COMPILATION_NOTES ""
#endif

int main(int argc, char const *argv[]){
  char hostbuffer[256] = "";
  int hostname;
  int n, bs;

  //Retriving some info about the machine
  // retrieve hostname
  hostname = gethostname(hostbuffer, sizeof(hostbuffer));
  if (hostname == -1) {
    printf("Error when getting hostname\n");
  }

  FILE *matTFile;
  FILE *matBlockTFile;
  matTFile = fopen("./results/matTFile.csv", "r");
  matBlockTFile = fopen("./results/matBlockTFile.csv", "r");
  if(matTFile == NULL){
    printf("Creating 'matT' results file....\n");
    matTFile = fopen("./results/matTFile.csv", "w");
    if(matTFile == NULL){
      printf("Error opening matTFile.csv\n");
    } else{
      fprintf(matTFile, "matrix_size,matT_wallTime[us],matTpar_wallTime[us],hostname,compilation_notes\n");
    }
  }else{
    fclose(matTFile);
    matTFile = fopen("./results/matTFile.csv", "a");
  }

  if(matBlockTFile == NULL){
    printf("Creating 'matBlockT' results file....\n");
    matBlockTFile = fopen("./results/matBlockTFile.csv", "w");
    if(matBlockTFile == NULL){
      printf("Error opening matBlockTFile.csv\n");
    } else{
      fprintf(matBlockTFile,"matrix_size,blockSize,matBlockT_wallTime[us],matBlockTpar_wallTime[us],hostname,compilation_notes\n");
    }
  }else{
    fclose(matBlockTFile);
    matBlockTFile = fopen("./results/matBlockTFile.csv", "a");
  }

  for (n = 16; n <= 4096; n *= 2){
    double *A   = (double *)malloc(n*n*sizeof(double));
    double *At  = (double *)malloc(n*n*sizeof(double));
    double *AtB = (double *)malloc(n*n*sizeof(double));

    for(int i = 0; i < n*n; i++){
      A[i] = randomD(0, 100, 4);
    }

#ifdef DEBUG
    //Print matrix
    printf("Matrix A:\n");
    for(int i = 0; i < n*n; i++){
      printf("%f\t", A[i]);
      if((i+1)%n == 0)
        printf("\n");
    }
#endif
    uint64_t t = matT(A, At, n);
    printf("Dim: %d, Wall Time: %ld us\n", n, t);
    if(matTFile != NULL){
      fprintf(matTFile, "%d,%ld,%ld,%s,%s\n", n, t, 0, hostbuffer, COMPILATION_NOTES);
    }
    for(bs = 4; bs <= n/2; bs*=2){
      t = matBlockT(A, AtB, n, bs);
      printf("\tBlock Size: %d, Block transopose Wall Time: %ld us\n", bs, t);
      if(matBlockTFile != NULL){
        fprintf(matBlockTFile, "%d,%d,%ld,%ld,%s,%s\n", n, bs, t, 0, hostbuffer, COMPILATION_NOTES);
      }
    }
#ifdef DEBUG
    printf("Matrix A trasnposed:\n");
    for(int i = 0; i < n*n; i++){
      printf("%f\t", At[i]);
      if((i+1)%n == 0)
        printf("\n");
    }
#endif
    if (A   != NULL) free(A);
    if (At  != NULL) free(At);
    if (AtB != NULL) free(AtB);
  }
  if(matTFile      != NULL) fclose(matTFile);
  if(matBlockTFile != NULL) fclose(matBlockTFile);
  return 0;
}
