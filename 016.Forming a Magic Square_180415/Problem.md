We define a magic square to be an ![](https://latex.codecogs.com/gif.latex?n%5Ctimes%20n) matrix of distinct positive integers from 1 to ![](https://latex.codecogs.com/gif.latex?n%5E2) where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a ![](https://latex.codecogs.com/gif.latex?3%5Ctimes%203) matrix s of integers in the inclusive range [1,9]. We can convert any digit a to any other digit b in the range [1,9] at cost of ![](https://latex.codecogs.com/gif.latex?%5Cleft%20%7Ca-b%20%5Cright%20%7C). Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

**Note:** The resulting magic square must contain distinct integers in the inclusive range [1,9].

For example, we start with the following matrix :

5 3 4
1 5 8
6 4 2

We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2

This took three replacements at a cost of .

##Input Format

Each of the lines contains three space-separated integers of row s[i].

##Constraints

- ![](https://latex.codecogs.com/gif.latex?s%5Bi%5D%5Bj%5D%5Cin%20%5B1%2C9%5D)

##Output Format

Print an integer denoting the minimum cost of turning matrix  into a magic square.

##Sample Input 0

4 9 2
3 5 7
8 1 5

##Sample Output 0

1

##Explanation 0

If we change the bottom right value, ![](https://latex.codecogs.com/gif.latex?s%5B2%5D%5B2%5D), from 5 to 6 at a cost of ![](https://latex.codecogs.com/gif.latex?%5Cleft%20%7C5-6%20%5Cright%20%7C%20%3D%201), s becomes a magic square at the minimum possible cost.

##Sample Input 1

4 8 2
4 5 7
6 1 6

##Sample Output 1

4

##Explanation 1

Using 0-based indexing, if we make

- ![](https://latex.codecogs.com/gif.latex?s%5B0%5D%5B1%5D%5Crightarrow%209)at a cost of ![](https://latex.codecogs.com/gif.latex?%5Cleft%20%7C%209-8%20%5Cright%20%7C%3D1)
- ![](https://latex.codecogs.com/gif.latex?s%5B1%5D%5B0%5D%5Crightarrow%203)at a cost of ![](https://latex.codecogs.com/gif.latex?%5Cleft%20%7C%203-4%20%5Cright%20%7C%3D1)
- ![](https://latex.codecogs.com/gif.latex?s%5B2%5D%5B0%5D%5Crightarrow%208)at a cost of ![](https://latex.codecogs.com/gif.latex?%5Cleft%20%7C%208-6%20%5Cright%20%7C%3D2),

then the total cost will be ![](https://latex.codecogs.com/gif.latex?1+1+2%3D4).