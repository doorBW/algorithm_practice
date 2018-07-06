Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

## Input Format

The first line of the input consists of an integer n. 
The next line contains n space-separated integers contained in the array.

## Output Format

Print the integer sum of the elements in the array.

## Constraints 
![](http://latex.codecogs.com/gif.latex?1%5Cleq%20n%5Cleq%2010)

![](http://latex.codecogs.com/gif.latex?0%5Cleq%20ar%5Bi%5D%5Cleq%2010%5E%7B10%7D)

## Sample Input

5

1000000001 1000000002 1000000003 1000000004 1000000005

## Output

5000000015

## Note:

The range of the 32-bit integer is ![](http://latex.codecogs.com/gif.latex?%28-23%5E%7B31%7D%29%20to%20%282%5E%7B31%7D-1%29%20or%5B-2147483648%2C2147483647%5D).
When we add several integer values, the resulting sum might exceed the above range. You might need to use long long int in C/C++ or long data type in Java to store such sums.
