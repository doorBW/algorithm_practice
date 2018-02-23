

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet ![](http://latex.codecogs.com/gif.latex?A%20%3D%20%28a_0%2Ca_1%2Ca_2%29), and the rating for Bob's challenge to be the triplet ![](http://latex.codecogs.com/gif.latex?B%20%3D%20%28b_0%2Cb_1%2Cb_2%29).

Your task is to find their comparison points by comparing ![](http://latex.codecogs.com/gif.latex?a_0) with ![](http://latex.codecogs.com/gif.latex?b_0), ![](http://latex.codecogs.com/gif.latex?a_1) with ![](http://latex.codecogs.com/gif.latex?b_1), and ![](http://latex.codecogs.com/gif.latex?a_2) with ![](http://latex.codecogs.com/gif.latex?b_2).

If ![](http://latex.codecogs.com/gif.latex?a_i%3Eb_i), then Alice is awarded 1 point.
If ![](http://latex.codecogs.com/gif.latex?a_i%3Cb_i), then Bob is awarded 1 point.
If ![](http://latex.codecogs.com/gif.latex?a_i%3Db_i), then neither person receives a point.
Comparison points is the total points a person earned.

Given A and B, can you compare the two challenges and print their respective comparison points?

## Input Format

The first line contains 3 space-separated integers, ![](http://latex.codecogs.com/gif.latex?a_0%2C%20a_1%2C%20and%5C%20a_2), describing the respective values in triplet A. 

The second line contains 3 space-separated integers,![](http://latex.codecogs.com/gif.latex?b_0%2C%20b_1%2C%20and%5C%20b_2), describing the respective values in triplet B.

## Constraints
- ![](http://latex.codecogs.com/gif.latex?1%3C%3D%28a_i%29%3C%3D100)
- ![](http://latex.codecogs.com/gif.latex?1%3C%3D%28b_i%29%3C%3D100)

## Output Format

Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

## Sample Input

5 6 7
3 6 10

## Sample Output

1 1 
## Explanation

In this example:

- ![](http://latex.codecogs.com/gif.latex?A%3D%28a_0%2Ca_1%2Ca_2%29%20%3D%20%285%2C6%2C7%29)
- ![](http://latex.codecogs.com/gif.latex?B%3D%28b_0%2Cb_1%2Cb_2%29%20%3D%20%283%2C6%2C10%29)


Now, let's compare each individual score:

- ![](http://latex.codecogs.com/gif.latex?a_0%3Eb_0), so Alice receives 1 point.
- ![](http://latex.codecogs.com/gif.latex?a_1%3Db_1), so nobody receives a point.
- ![](http://latex.codecogs.com/gif.latex?a_2%3Cb_2), so Bob receives 1 point.
Alice's comparison score is 1, and Bob's comparison score is 1. Thus, we print 1 1 (Alice's comparison score followed by Bob's comparison score) on a single line.
