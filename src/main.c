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


int main(int argc, char const *argv[]){
  
  return 0;
}
