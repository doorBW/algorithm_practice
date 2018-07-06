You will be given two arrays of integers. You will be asked to determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

## Function Description

Complete the getTotalX function in the editor below. It has two parameters:

1. Integer Array, a, denoting the elements in the set A.
2. Integer Array, b, denoting the elements in the set B.
The function must return a long integer denoting the number of integers between the two sets.

## Constraints

- ![](https://latex.codecogs.com/gif.latex?1%5Cleq%20n%2Cm%5Cleq%2010)
- ![](https://latex.codecogs.com/gif.latex?1%5Cleq%20a_i%5Cleq%20100)
- ![](https://latex.codecogs.com/gif.latex?1%5Cleq%20b_i%5Cleq%20100)

## Raw Input Format

The first line contains two space-separated integers describing the respective values of , the number of elements in array , and , the number of elements in array b. 
The second line contains  distinct space-separated integers describing ![](https://latex.codecogs.com/gif.latex?a_0%2Ca_1%2C%20...%2C%20a_%7Bn-1%7D). 
The third line contains  distinct space-separated integers describing ![](https://latex.codecogs.com/gif.latex?b_0%2Cb_1%2C%20...%2C%20b_%7Bm-1%7D).

## Sample Input 0

2 3
2 4
16 32 96

## Sample Output 0

3

## Explanation 0

2 and 4 divide evenly into 4, 8, 12 and 16. 
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element of A is a factor and each is a factor of all elements of B.