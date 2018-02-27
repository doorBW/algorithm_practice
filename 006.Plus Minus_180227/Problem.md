Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

## Note:
This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to ![](http://latex.codecogs.com/gif.latex?10%5E%7B-4%7D) are acceptable.

## Input Format

The first line contains an integer, N, denoting the size of the array. 
The second line contains N space-separated integers describing an array of numbers !()[http://latex.codecogs.com/gif.latex?%28a_0%2Ca_1%2Ca_2%2C%20...%20%2Ca_%7Bn-2%7D%2Ca_%7Bn-1%7D%29].

## Output Format

You must print the following 3 lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeroes in the array compared to its size.
## Sample Input

6

-4 3 -9 0 4 1         

## Sample Output

0.500000
0.333333
0.166667

## Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array. 
The respective fractions of positive numbers, negative numbers and zeroes are !()[http://latex.codecogs.com/gif.latex?3/6%20%3D%200.500000%2C%20%5C%202/6%20%3D%200.333333%20%5C%20and%5C%201/6%3D0.166667] , respectively.