# Frequency Queries

### Interview Preparation Kit

### Dictionaries and Hashmaps



문제는 아래 주소에서 만나보실 수 있습니다.

[https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen](https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=dictionaries-hashmaps&h_r=next-challenge&h_v=zen)



## 풀이 코드

같은 경로의 solution.py를 확인하세요.



## 풀이 후기

처음에는 딕셔너리를 사용해서 풀었는데 4개의 케이스에서 시간제한이 걸렸다.

코드상으로는 for문 하나로 O(n)처럼 보이지만, 확인해보니 딕셔너리에서 dic.containsKey(or Value) 와 같은 함수들이 대략적으로 n의 복잡도를 가진다고 하니, 결국 O(n^2)의 복잡도 였을 것이다.

그래서 Counter 함수를 import해서 사용했다.

만약 Counter함수를 import할 수 없었다면 어떻게 해야할까?

