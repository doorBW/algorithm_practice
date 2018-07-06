# Organizing Containers of Balls



## To Korean



-----



David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.

As an example, David has $n=2$ containers and $2$ different types of balls, both of which are numbered from $0$ to $n-1 = 1$. The distribution of ball types per container are described by an $n\times n$ matrix of integers, $M[container][type]$. For example, consider the following diagram for $M=[[1,4],[2,3]]$:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1485811368-9e78c98652-swapping-balls.png)

In a single operation, David can *swap* two balls located in different containers.

The diagram below depicts a single swap operation:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1485811849-e97b84e218-swapping-balls-ps-1.png)

David wants to perform some number of swap operations such that:

- Each container contains only balls of the same type.
- No two balls of the same type are located in different containers.

You must perform $q$ queries where each query is in the form of a matrix, $M$. For each query, print `Possible` on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print `Impossible`.

**Input Format**

The first line contains an integer $q$, the number of queries.

Each of the next $q$ sets of lines is as follows:

1. The first line contains an integer $n$, the number of containers (rows) and ball types (columns).
2. Each of the next $n$ lines contains $n$ space-separated integers describing row $M[i]$.

**Constraints**

- $1\leq q \leq 10$
- $1\leq n \leq100$
- $0\leq M[container][type]\leq10^9$

**Scoring**

- For $33\%$ of score, $1\leq n \leq10$.
- For $100\%$ of score, $1\leq n \leq100$.

**Output Format**

For each query, print `Possible` on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print `Impossible`.

**Sample Input 0**

```
2
2
1 1
1 1
2
0 2
1 1
```

**Sample Output 0**

```
Possible
Impossible
```

**Explanation 0**

We perform the following $q=2$ queries:

1. The diagram below depicts one possible way to satisfy David's requirements for the first query:![image](https://s3.amazonaws.com/hr-challenge-images/0/1485813936-37f8a37dad-swapping-balls-sample-0-0.png)
   Thus, we print `Possible` on a new line.
2. The diagram below depicts the matrix for the second query:![image](https://s3.amazonaws.com/hr-challenge-images/0/1485814141-d283776840-swapping-balls-sample-0-2.png)
   No matter how many times we swap balls of type $t_0$ and $t_1$ between the two containers, we'll never end up with one container only containing type $t_0$ and the other container only containing type $t_1$. Thus, we print `Impossible` on a new line.





## Solution explain

```
1. Swaps that happen between any 2 buckets are always of equal value (you can exchange 1 for 1 but not 2 for 1, ratio should always be 1:1), therefore the number of balls in each bucket will always remain the same. 

2. We need to make sure that the total number of balls in each container should equal the number of balls of any type 't' for a fair trade(1:1 ratio). This is done to check whether there are any type 't' balls that satisfy the requirements of the solution (i.e. we want all balls of a single type 't' in only one container).

3. Calculate the number of balls in each container(sum of rows) and store it in a list.

4. Calculate the number of balls of each type(sum of columns) and store it in a list.

5. Sort the two lists and compare them. If they are equal then a solution exists otherwise, no solution exists.

Try theses cases to see and understand the pattern:

Possible:

2
1 0
0 1

2
1 2
2 1

3
0 4 0
2 0 1
1 0 2

4
1 2 3 4
2 1 4 3
3 4 2 1
4 3 1 2

4
0 0 5 0
4 0 0 0
0 2 0 1
0 1 0 2

Impossible:

2
2 1
0 0

2
2 1
0 1

3
1 2 3
3 2 1
2 3 1

3
1 0 0
0 2 0
0 2 0

4
1 2 1 3
2 1 3 1
1 3 2 1
3 2 1 1

Note: For more test cases try Solved Sudoku puzzles.

Here is Python2 Solution:
```