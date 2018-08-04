class Solution {
  public int solution(int n, int[] money) {
      int answer = 0;
      int numOfMoney = money.length;
      
      long[] table = new long[n+1];
      for(int i=0;i<=n;i++){ // dp table init
            table[i] = (i % money[0] == 0) ? 1 : 0;
          // 첫번째 동전으로 i원이 나누어 떨어지면 1, 아니면 0
      }
      
      for(int i=1;i<numOfMoney;i++){
          for(int j=money[i];j<=n;j++){
              table[j] += table[j-money[i]];
          }
      }
      answer = (int)(table[n] % 1000000007);
      return answer;
  }
}