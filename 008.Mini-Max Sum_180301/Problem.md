Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

## Input Format

A single line of five space-separated integers.

## Constraints

Each integer is in the inclusive range ![](http://latex.codecogs.com/gif.latex?%5B1...10%5E9%5D).
Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

## Sample Input

1 2 3 4 5

## Sample Output

10 14

## Explanation

Our initial numbers are 1, 2, 3, 4, and 5. We can calculate the following sums using four of the five integers:

If we sum everything except 1, our sum is !()[http://latex.codecogs.com/gif.latex?2&plus;3&plus;4&plus;5%3D14].
If we sum everything except 2, our sum is !()[http://latex.codecogs.com/gif.latex?1&plus;3&plus;4&plus;5%3D14].
If we sum everything except 3, our sum is !()[http://latex.codecogs.com/gif.latex?1&plus;2&plus;4&plus;5%3D14].
If we sum everything except 4, our sum is !()[http://latex.codecogs.com/gif.latex?1&plus;2&plus;3&plus;5%3D14].
If we sum everything except 5, our sum is !()[http://latex.codecogs.com/gif.latex?1&plus;2&plus;3&plus;4%3D14].
Hints: Beware of integer overflow! Use 64-bit Integer.