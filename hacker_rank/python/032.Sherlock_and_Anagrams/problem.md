# Sherlock and Anagrams
### Interview Preparation Kit
### Dictionaries and Hashmaps

문제는 아래 주소에서 만나보실 수 있습니다.

https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

## 풀이 코드
같은 경로의 solution.py 파일을 확인해주세요.

## 풀이 후기
파이썬에서 hash()함수를 사용해본적이 거의 없는 것 같은데 이번에 사용해보게 되었다.
aba aab를 같은 문자로 인식하게끔 해야하는데 처음에는 set을 생각했다. 순서가 없는 자료형이기 때문에 하지만 set에서는 중복 또한 없어서 aba와 ab조차 같은 것으로 판단하게 되어 문제에 알맞지 않다.
그래서 생각한 것이 hash함수이다. 각 문자열에 대해 유니크한 숫자값으로 반환해주기 때문에 aba와 aab에 대해 각 문자열의 hash값의 합은 같다.
이를 이용하면 되고 마지막에 카운트를 더할 때 코드 기준으로 v 값이 3이였다면 중복된 문자열이 3개라는 의미이기에 3개중 2개의 조합, 3C2를 계산해야 한다.