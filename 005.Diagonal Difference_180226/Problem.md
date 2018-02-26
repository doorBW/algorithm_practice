Given a square matrix, calculate the absolute difference between the sums of its diagonals.

## Input Format

The first line contains a single integer,  denoting the number of rows and columns in the matrix . 
The next  lines denote the matrix 's rows, with each line containing  space-separated integers describing the columns.

## Constraints
![](http://latex.codecogs.com/gif.latex?-100%3C%5Cleq%20Elements%5C%20in%5C%20the%5C%20matrix%5Cleq%20100)

## Output Format

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

## Sample Input

3

11 2 4

4 5 6

10 8 -12

## Sample Output

15

## Explanation

The primary diagonal is:

11

   5
   
     -12
     
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
     
   5
   
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19 
Difference: |4 - 19| = 15

## Note:
|x| is the absolute value of x
