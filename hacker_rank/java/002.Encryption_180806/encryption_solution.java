import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the encryption function below.
    static String encryption(String s) {
        String answer = "";
        int s_len = s.length();
        int num_1 = 0;
        while(!((Math.pow(num_1,2)<s_len)&(s_len<=Math.pow(num_1+1,2)))){
            num_1++;
        }
        int num_2 = num_1+1;
        if(num_2 * num_1 < s_len) num_1++;
        String encryption[][] = new String[num_1][num_2];
        for(int i=0;i<num_1;i++){
            for(int j=0;j<num_2;j++){
                try{
                    encryption[i][j] = s.substring(i*(num_2)+j,i*(num_2)+j+1);
                }catch(Exception e){
                    encryption[i][j] = "";
                }
            }
        }
        for(int j=0;j<num_2;j++){
            for(int i=0;i<num_1;i++){
                answer += encryption[i][j];
            }
            answer += " ";
        }
        System.out.println(answer);
        
        return answer;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        String result = encryption(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
