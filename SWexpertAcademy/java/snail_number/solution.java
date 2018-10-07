import java.util.Scanner;
public class Solution{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int test_case = input.nextInt();
        int n, r, c, v, add;
        for(int test_n=1;test_n<=test_case;test_n++){
            n = input.nextInt();
            v = 1;
            r = 0;
            c = -1;
            add = 1;
            int[][] arr = new int[n][n];
            while(n > 0){
                for(int j=0; j<n; j++){
                    c = c + add;
                    arr[r][c] = v;
                    v++;
                }
                n--;
                if(n == 0) break;
                for(int j=0; j<n; j++){
                    r = r + add;
                    arr[r][c] = v;
                    v++;
                }
                add = add*(-1);
            }
            System.out.println("#"+test_n);
            for(int[] i : arr){
                for(int j : i){
                    System.out.print(""+j+" ");
                }
                System.out.println("");
            }
        }
    }
}
