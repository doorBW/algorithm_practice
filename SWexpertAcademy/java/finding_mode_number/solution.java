import java.util.Scanner;
public class Solution{
    static int max;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int test_num = input.nextInt();
        for(int num=1; num<=test_num; num++){
            input.nextInt();
            int[] num_arr = new int[101];
            int max = 0;
            //int n;
            for(int i=0;i<1000;i++){
                int n = input.nextInt();
                if(++num_arr[n] >= num_arr[max]){
                    max = n;
                }
            }
            System.out.println("#"+num+" "+max);
        }
    }
}
