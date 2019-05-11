# Jumping on the Clouds

### Interview Preparation Kit

### Warm-up Challenges



문제는 아래 주소에서 만나보실 수 있습니다.

[https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup](https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=warmup)



## 풀이 코드

같은 경로의 solution.py를 확인해주세요 :)



## 풀이 후기

1의 위치를 기준으로 점프 횟수를 구했다.

1이 나타내면 무조건 뛰어야 하는 거고, 최대 +2 점프만 가능하니 1다음에는 무조건 0이 오게되어 있다. 이를 이용해서 점프횟수를 구해서 더하고, 이후에 1때문에 점프하고 끝났을 때 뒤에 0이 더 남아있는지만 체크하면 된다.