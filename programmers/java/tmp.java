import java.util.Arrays;
class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        int numOfWorks = works.length;
        int remain_n = 0;
        int sumOfWorks = 0;
        int quotient = 0;
        int remain = 0;
        
        // 1.처음에 들어온 모든 작업의 합이 n보다 작으면 0을 반환한다.
        for(int i=0; i<numOfWorks; i++){
            sumOfWorks += works[i];
        }
        if(sumOfWorks <= n) return 0;
        // 1.끝
        
        // 2.정렬 후 
        Arrays.sort(works);
        if(works[numOfWorks-1] - works[numOfWorks-2] > n){
            works[numOfWorks-1] -= n;
        }else{
            for(int count=0; count<n; count++){
                if(works[0] == works[numOfWorks-1]) {
                    remain_n = n-count;
                    break;
                }
                works[numOfWorks-1]--;
                Arrays.sort(works);
            }
        }
        if(works[0] == works[numOfWorks-1]){
            sumOfWorks = works[0]*numOfWorks;
            if(sumOfWorks > remain_n){
                sumOfWorks -= remain_n;    
            }else return 0;
            quotient = sumOfWorks/numOfWorks;
            remain = sumOfWorks%numOfWorks;
            if(remain == 0) return (quotient*quotient)*numOfWorks;
            else{
                return remain*((quotient+1)*(quotient+1))+(numOfWorks-remain)*(quotient*quotient);
            }
        }else{
            for(int i=0; i<numOfWorks; i++){
                answer += (works[i]*works[i]);
            }
        }
        return answer;
    }
}