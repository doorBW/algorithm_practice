# Count Triplets

### Interview Preparation Kit

### Dictionaries and Hashmaps



문제는 아래 주소에서 만나보실 수 있습니다.

[https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps](https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=dictionaries-hashmaps)



## 풀이 코드

같은 경로의 solution.py를 확인해주세요.



## 풀이 후기

꽤나 어려웠던 문제,,

첫번째 풀이와 두번째 풀이 모두 시간복잡도에 부딪혔다..

도저히 O(n)으로 줄이지를 못하겠어서 discussion을 봤는데 정말 대단한 사람들이 많다.

현재 풀이에 성공한 코드를 간략히 설명하면,

arr에서 차례대로 val을 꺼낸다.



그리고 해당 val는 총 3가지의 역할을 할 수 있게 된다.

코드 순으로 설명하면, val가 triplets의 세번째 요소역할이다.

third_dic에 확인하여 존재하는 값 만큼 cnt를 높여주면된다.



두번째로는 val가 triplets의 두번째 요소의 역할을 할 수 있다.

두번째 요소는 세번째 요소의 후보군을 만들어 낼 수 있다.



세번째로는 val가 triplets의 첫번째 요소의 역할을 하는 것이다.

즉 triplets의 시작을 알리는 요소 역할을 하게 된다.



특정 val는 무조건 triplets의 시작으로 등록되는데, 이는 결국 두번째 요소의 후보군을 만들어 내는 역할을 한다. 즉 r=2일때 1이란 값이 왔으면 1이 triplets의 시작이므로 second_dic[2] = 1을 초기화한다.

이후 2라는 값이 온다. 2는 먼저 자신이 triplets의 세번째 요소 역할을 할 수 있는지 확인한다. third_dic의 key에 2가 없으므로 세번째 요소 역할을 할 수 없다. 그런데 second_dic의 key를 확인해보면 2가 존재한다. 즉 2는 두번째 요소역할을 할 수 있고 이는 세번째 요소의 후보군을 만들어 내는 역할을 한다. 이에 따라서 third_dic[4] = 1을 초기화 한다.

이후에 또 2라는 값이 오면 동일한 과정을 반복해서 third_dic[4] = 2가 된다.

또한 2는 첫번째 요소 역할을 할 수 있으므로 second_dic[4]=1을 초기화한다.



이후 4라는 값을 꺼내어 확인한다. 4는 third_dic의 key에 존재하므로 세번째 요소 역할을 할 수 있고 third_dic[4] = 2 만큼 역할을 할 수 있으므로 cnt에 2를 더한다. 이후 second_dic의 key에도 4가 존재하므로 third_dic[8] = 1로 초기화 하고, 동일하게 4는 첫번째 요소역할도 할 수 있으므로 second_dic[8] = 1 로 초기화 한다.