import java.util.Scanner;
public class Solution{
    static int answer;
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
//        int test_case_num = Integer.parseInt(input.nextLine());
        int left_2, left_1, check, right_1, right_2;
        for(int i=1;i<=10;i++){
            int answer = 0;
            int max = 0;
            int tmp = 0;
            int building_num = input.nextInt();
            left_2 = input.nextInt();
            left_1 = input.nextInt();
            check = input.nextInt();
            right_1 = input.nextInt();
            right_2 = input.nextInt();
            //System.out.println(""+left_1+"@"+check+"@"+right_1);
            for(int j=2; j<building_num-2; j++){
                if(max < left_2) max = left_2;
                if(max < left_1) max = left_1;
                if(max < right_2) max = right_2;
                if(max < right_1) max = right_1;
                tmp = (check - max > 0) ? check-max : 0;
                answer += tmp;
                left_2 = left_1;
                left_1 = check;
                check = right_1;
                right_1 = right_2;
                if (j == building_num-3) break;
                right_2 = input.nextInt();
                max= 0;
                tmp = 0;
            }
            
            System.out.println("#"+i+" "+answer);
        }
    }
}
