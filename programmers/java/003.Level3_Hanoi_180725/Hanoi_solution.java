class Solution {
    public int hanoi(int k, int n, int[][] answer, int first, int second,int third){
        int next;
        if(n==1){
            answer[k][0] = first;
            answer[k][1] = third;
            k++;
            return k;
        }else{
            next = hanoi(k,n-1,answer,first,third,second);
            answer[next][0] = first;
            answer[next][1] = third;
            next++;
            next = hanoi(next,n-1,answer,second,first,third);
        }
        return next;
    }
  public int[][] solution(int n) {
      int[][] answer = new int[(int)Math.pow(2,n) - 1][2];
      int[] ref = {0,n};
      hanoi(ref[0],ref[1],answer,1,2,3);
      return answer;
  }
}