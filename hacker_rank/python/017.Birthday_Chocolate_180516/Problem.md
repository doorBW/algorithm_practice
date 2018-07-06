# Birthday Chocolate

## To Korean

먼저, input으로는 총 3줄이 들어온다.

첫번째 줄에는 정수로된 하나의 숫자(=n), 두번째 줄에는 정수로 이루어진 n개의 숫자들(스페이스로 구분되어 코드상에서는 배열(또는 리스트)로 읽음), 세번째 줄에는 스페이스로 구분된 2개의 정수

문제에서 말하길, Lily와 Ron, 두 친구가 나오는데 제대로된 해석인지 모르겠지만(문제 푸는데는 맞는 해석인 것 같다.) Lily가 Ron에게 자기가 가지고 있는 초코렛을 나누어 주려고한다.

하단의 이미지를 보면 알겠지만, 초콜렛에 숫자가 적혀있다고 생각하자. 그리고 각 숫자는 우리가 input의 두번째 줄에서 받은 숫자들이다.

즉,

![image](https://s3.amazonaws.com/hr-assets/0/1489060874-a04ddb06cf-choco4.png)

이러한 이미지라면, 먼저 5개로 나누어진 초콜렛이므로 input의 첫번째 줄(=n)은 5이었을 것이며 그 다음 두번째 줄의 입력은 1 2 1 3 2 이다.

그리고 세번째 줄에서는 두개의 정수가 나오는데 첫번째 값이 Ron의 생일중 day 값이고 두번째 값이 Ron의 생일 중 month이다. 사실 그게 '일'이고 '월'이고는 큰 의미가 없는 듯하다..

일단 우리가 알아야 할것은 이 Lily라는 애가 굳이.. 이상한 방법으로 초콜렛을 주겠단다...Ron의 생일, day 와 month 값에 대해서 초콜릿에서 month값만큼 이어서 더해 d가 되는 방법으로 주려고 하는데, 이때 몇가지 방법이 있는지 구하는 것이 목표이다.

즉, 위에서 보인 이미지를 토대로 생각해보면, 먼저 input은 다음과 같이 들어왔던 것이다.

5

1 2 1 3 2

3 2

즉, 1 2 1 3 2 순서로 적힌 초콜릿에서 연속된 2개의 초콜릿을 더해 3의 값이 되는 방법을 구해야 한다. 이때는 첫번째와 두번째 초콜릿 1+2 라는 방법1과 두번째와 세번째 초콜릿 2+1이라는 방법2로 총 2개가 존재하므로 2를 반환해야 한다.

나름 풀어서 설명했는데 보다 자세히 알고자 하면 아래의 본문을 읽어보면 된다.



Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment mathches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, $s=[2,2,1,3,2]$. She wants to find segments summing to Ron's birth day, $d=4$ with a length equalling his birth month,$m=2$ . In this case, there are two segments meeting her criteria: $[2,2] and [1,3]$.

**Input Format**

The first line contains an integer $n$, the number of squares in the chocolate bar. 
The second line contains  space-separated integers $s[i]$, the numbers on the chocolate squares where $0\leq i<n$. 

The third line contains two space-separated integers, $d$ and $m$, Ron's birth day and his birth month.

**Constraints**

- $1\leq n \leq 100$
- $1\leq s[i] \leq 5$, where ($0\leq i < n$)
- $1\leq d \leq 31$
- $1\leq m\leq 12$

**Output Format**

Print an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.

**Sample Input 0**

```
5
1 2 1 3 2
3 2
```

**Sample Output 0**

```
2
```

**Explanation 0**

Lily wants to give Ron $m=2$ squares summing to $d=3$. The following two segments meet the criteria:

![image](https://s3.amazonaws.com/hr-assets/0/1489060874-a04ddb06cf-choco4.png)

**Sample Input 1**

```
6
1 1 1 1 1 1
3 2
```

**Sample Output 1**

```
0
```

**Explanation 1**

Lily only wants to give Ron $m=2$ consecutive squares of chocolate whose integers sum to $d=3$. There are no possible pieces satisfying these constraints:

![image](https://s3.amazonaws.com/hr-assets/0/1489060978-e33d905668-choco5.png)

Thus, we print $0$ as our answer.

**Sample Input 2**

```
1
4
4 1
```

**Sample Output 2**

```
1
```

**Explanation 2**

Lily only wants to give Ron $m=1$ square of chocolate with an integer value of $d=4$. Because the only square of chocolate in the bar satisfies this constraint, we print $1$ as our answer.

