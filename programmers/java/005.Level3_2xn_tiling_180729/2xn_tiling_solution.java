class Solution {
  public int solution(int n) {
      if(n<4) return n;
      int answer = 0;
      int tmp_1 = 2;
      int tmp_2 = 3;
      for(int i=0;i<n-3;i++){
          answer = (tmp_1+tmp_2)%1000000007;
          tmp_1 = tmp_2;
          tmp_2 = answer;
      }
      return answer;
  }
}