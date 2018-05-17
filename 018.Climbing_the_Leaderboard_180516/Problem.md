# Climbing the Leaderboard

## To Korean



Alice is playing an arcade game and wants to climb to the top of the leaderboard. Can you help her track her ranking as she plays? The game uses [Dense Ranking](https://en.wikipedia.org/wiki/Ranking#Dense_ranking_.28.221223.22_ranking.29), so its leaderboard works like this:

- The player with the highest score is ranked number  on the leaderboard.
- Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

We want to determine Alice's rank as she progresses up the leaderboard. For example, the four players on the leaderboard have high scores of $100, 90, 90,$ and $80$. Those players will have ranks $1, 2, 2,$ and $3$, respectively. If Alice's scores are $70, 80$  and $105$, her rankings after each game are $4^{th}, 3^{rd}$  and $1^{st}$.

You are given an array, $scores$, of *monotonically decreasing* leaderboard scores, and another array, , of Alice's scores for the game. You must print  integers. The $j^{th}$ integer should indicate the current rank of alice after her $j^{th}$ game.

**Input Format**

The first line contains an integer , the number of players on the leaderboard. 
The next line contains  space-separated integers $scores[i]$, the leaderboard scores in decreasing order. 
The next line contains an integer, , denoting the number games Alice plays. 
The last line contains  space-separated integers $alice[j]$, her game scores.

**Constraints**

- $1\leq n \leq 2 \times 10^5$
- $1\leq m \leq 2 \times 10^5$
- $0\leq scores[i]\leq 10^9$ for $0\leq i <n$
- $0\leq alice[j]\leq10^9$ for $0\leq j <m$
- The existing leaderboard, $scores$, is in *descending* order.
- Alice's scores $alice$, are in *ascending* order.

**Subtask**

For $60\%$ of the maximum score:

- $1\leq n \leq 200$
- $1\leq m \leq200$

**Output Format**

Print  integers. The $j^{th}$ integer should indicate the rank of alice after playing the $j^{th}$ game.

**Sample Input 0**

```
7
100 100 50 40 40 20 10
4
5 25 50 120
```

**Sample Output 0**

```
6
4
2
1
```

**Explanation 0**

Alice starts playing with 7 players already on the leaderboard, which looks like this:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481263702-9b5e9abd56-climbingrank.png)

After Alice finishes game 0, her score is 5 and her ranking is 6:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481263847-2443e11cea-climbingrank1.png)

After Alice finishes game 1, her score is 25 and her ranking is 4:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481264155-cb76495070-climbingrank3.png)

After Alice finishes game 2, her score is 50 and her ranking is tied with Caroline at 2:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481264229-a216b3a974-climbingrank4.png)

After Alice finishes game 3, her score is 120 and her ranking is 1:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481264323-30f93fa8de-climbingrank5.png)