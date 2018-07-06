class Solution {
  public String solution(String s) {
      String answer = "";
      int temp;
      if (s.length()%2 == 0){
          temp = s.length() / 2;
          answer = s.substring(temp-1,temp+1);    
      }else{
          temp = s.length() / 2;
          answer = s.substring(temp,temp+1);
      }
      
      return answer;
  }
}