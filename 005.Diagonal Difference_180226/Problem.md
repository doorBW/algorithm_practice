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

![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Balign*%7D%2011%20%26%5C%5C%20%26%5C%205%20%5C%5C%20%26%20-12%20%5Cend%7Balign*%7D)
     
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Balign*%7D%20%26%20%5C%20%5C%204%20%5C%5C%20%265%20%5C%5C%2010%20%26%20%5Cend%7Balign*%7D)

Sum across the secondary diagonal: 4 + 5 + 10 = 19 
Difference: |4 - 19| = 15

## Note:
|x| is the absolute value of x
