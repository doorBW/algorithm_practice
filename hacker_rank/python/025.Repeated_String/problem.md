# Repeated String

### Interview Preparation Kit

### Warm-up Challenges



문제는 아래 주소에서 만나보실 수 있습니다.

[https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen](https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=warmup&h_r=next-challenge&h_v=zen)



## 풀이 코드

같은 경로상의 solution.py 파일을 확인해주세요.



## 풀이 후기

문자열 s의 길이를 이용한다.

무조건 처음에 준 n값을 전체적으로 탐색하려고 하는건 너무 무리이다.

따라서 s에 대해서 탐색하고, 어차피 문자열 s가 반복되는 것이니 반복횟수만큼만 곱해주면 된다. 이후에 나머지는 직접 처리해준다.