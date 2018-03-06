There are two kangaroos on a number line ready to jump in the positive direction (i.e, toward ![](http://latex.codecogs.com/gif.latex?%5Cinfty)). Each kangaroo takes the same amount of time to make a jump, regardless of distance. That is, if kangaroo one jumps 3 meters and kangaroo two jumps 5 meters, they each do it in one second, for example.

Given the starting locations and jump distances for each kangaroo, determine if and when they will land at the same location at the same time.

## Input Format

- 4 space-separated integers 
	-![](http://latex.codecogs.com/gif.latex?x_1%2Cv_1%2Cx_2%2Cv_2) : starting locations ![](http://latex.codecogs.com/gif.latex?x_%7Broo%7D) and meters per jump ![](http://latex.codecogs.com/gif.latex?v_%7Broo%7D) for kangaroos 1 and 2
	- ![](http://latex.codecogs.com/gif.latex?0%5Cleq%20x_1%3C%20x_2%5Cleq%2010000)
	- ![](http://latex.codecogs.com/gif.latex?1%5Cleq%20v_1%2C%20v_2%5Cleq%2010000)

## Output Format

Print YES if they can land on the same location at the same time. Otherwise, print NO.

## Sample Input 0

0 3 4 2
## Sample Output 0

YES
## Explanation 0

The two kangaroos jump through the following sequence of locations: 
![](https://s3.amazonaws.com/hr-assets/0/1516005283-e74e76ff0c-kangaroo.png)
The kangaroos meet after 4 jumps.

## Sample Input 1

0 2 5 3
## Sample Output 1

NO
## Explanation 1

Kangaroo 2 is travelling faster than kangaroo 1, so they will never meet.