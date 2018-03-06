Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Sam’s two children, Larry and Rob, decide to play a game in which they each climb a tree and throw fruit at their (Sam’s) house. Each fruit that lands on the house scores one point for the one who threw it. Larry climbs the tree on the left (the apple), and Rob climbs the one on the right (the orange).

We’ll use the following diagram to describe the challenge:

![](https://s3.amazonaws.com/hr-challenge-images/25220/1474218925-f2a791d52c-Appleandorange2.png)

For simplicity, we’ll assume all of the landmarks are on a number line. Larry climbs the apple tree at point , and Rob climbs the orange tree at point . Sam’s house stands between points  and . Values increase from left to right.

You will be given a list of distances the fruits are thrown. Negative distances indicate travel left and positive distances, travel right. Your task will be to calculate the scores for Larry and Rob and report them each on a separate line.

## Input Format

- 2 space-separated integers

	- s and t, left and right sides of Sam’s house
	- ![](http://latex.codecogs.com/gif.latex?1%5Cleq%20s%2Ct%5Cleq%2010%5E5)

- 2 space-separated integers

	- a and b, Larry’s and Rob’s positions in the trees
	- ![](http://latex.codecogs.com/gif.latex?1%5Cleq%20a%2Cb%5Cleq%2010%5E5)

- 2 space-separated integers
	- m and n, number of apples and oranges thrown
	- ![](http://latex.codecogs.com/gif.latex?1%5Cleq%20m%2Cn%5Cleq%2010%5E5)

- m space-separated integers

	- distances ![](http://latex.codecogs.com/gif.latex?n_i) that each apple falls from b
	- ![](http://latex.codecogs.com/gif.latex?-10%5E5%5Cleq%20m_i%5Cleq%2010%5E5)

- n space-separated integers
	- distances  that each orange falls from 
	- ![](http://latex.codecogs.com/gif.latex?-10%5E5%5Cleq%20n_i%5Cleq%2010%5E5)

## Output Format

2 space-separated integers on a line: Larry’s score followed by Rob’s score.

## Sample Input 0

7 11
5 15
3 2
-2 2 1
5 -6

## Sample Output 0

1 1
Explanation 0

The first apple falls at position 5-2=3 
The second apple falls at position 5+2=7 
The third apple falls at position 5+1=6 
The first orange falls at position 15+5=20 
The second orange falls at position 15-6=9 

Only one fruit (the second apple) falls within the region between 7 and 11, so Larry’s score is 1. 
Only the second orange falls within the region between 7 and 11, so Rob’s score is 1.