# Extra Long Factorials

사실상 파이썬에서는 아는 사람은 알겠지만, 정수형 범위가 무제한이기 때문에 너무나 쉬운문제가 되어버렸다.

그냥 간단히 파이썬에서 자료형 범위만 짚어보자.

위에서 파이썬에서 정수형 범위가 무제한이라고 했지만 맞는 이야기이기도하고 틀린 이야기이기도 하다. C나 java등을 접해보신분들은 알겠지만 이러한 언어에서는 숫자 3을 가지는 변수 i를 선언할때, int i = 3 이런식으로 선언한다. 즉 우리가 만드는 변수 i는 int라는 자료형을 가지며 그 i에 3을 대입하는 것인데, 파이썬에서는 그렇지 않다. 그냥 단순히 i = 3이라고 하면된다.

그럼 파이썬에서는 int, long 이러한 자료형이 없는 것일까? 아니다!

파이썬에서도 int 가 존재하고 long이 존재한다. 그리고 그 int 는 C나 java와 같이 4바이트로 $-2^{31} ~ 2^{31}+1$ 의 범위를 가지는 것 또한 동일하다.

*범위를 가진다고? 위에서는 무제한 이라며!*

파이썬에서는 int말고도 long이라는 자료형을 갖는데, 이는 범위가 무제한이다.

*나는 long이나 int를 구별한 적이 없는데?*

맞다. 나도 없다 그런적은. 파이썬에서는 숫자(정수)가 int 범위를 넘어가면 자동으로 long으로 변환되기 때문이다. 이를 확인하기 위해서는, $x = 2^{31}+1$ 을 하고, $type(x)와 type(x+1)$ 을 찍어보면 확인할 수 있을 듯하다.

뭐 말나온 김에 다뤄보면 python 에서 실수형 자료형으로는 float로써 크기는 8바이트이다. 물론 이는 무제한이 아니고 범위가 한정되어 있다.

추가적으로 다른 언어도 궁금하다면 [다음 사이트](http://blog.colab.kr/2)를 참고하면 좋을 것 같다.

## To Korean

입력 n에 대해 팩토리얼 값구하는거..



The *factorial* of the integer , written , is defined as:

$n! = n\times(n-1)\times(n-2)\times \cdots \times 3 \times 2\times1$

Calculate and print the factorial of a given integer.

**Note:** Factorials of $n>20$ can't be stored even in a $64-bit$ long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.

**Input Format**

Input consists of a single integer 

**Constraints**

$1\leq n\leq100$

**Output Format**

Print the factorial of $n$.

**Sample Input**

25

**Sample Output**

15511210043330985984000000

**Explanation**

$25!=25\times24\times23\times\cdots\times3\times2\times1$

 