import java.util.Scanner;
public class Solution{
    static int answer;    
    public static void main(String[] arg){
        Scanner input = new Scanner(System.in);
        int dump;
        int max = 0;
        int min = 101;
        int[] b_arr = new int[100];
        int max_idx = 0;
        int min_idx = 0;
        for(int test_case=1;test_case<=10;test_case++){
            answer = 0;
            dump = input.nextInt();
            for(int i=0;i<100;i++) b_arr[i] = input.nextInt();
            for(int t=0;t<dump;t++){
                max = 0;
                min = 101;
                for(int i=0;i<100;i++){
                    if(b_arr[i] > max){
                        max = b_arr[i];
                        max_idx = i;
                    }
                    if(b_arr[i] < min){
                        min = b_arr[i];
                        min_idx = i;
                    }
                }
                b_arr[max_idx] = max - 1;
                b_arr[min_idx] = min + 1;
        	}
            max = 0;
            min = 101;
            for(int i=0;i<100;i++){
                if(b_arr[i] > max){
                    max = b_arr[i];
                }
                if(b_arr[i] < min){
                    min = b_arr[i];
                }
            }
            answer = max-min;
            System.out.println("#"+test_case+" "+answer);
        }
    }
    
}
