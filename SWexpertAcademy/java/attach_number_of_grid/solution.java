import java.util.Scanner;
import java.util.HashSet;
public class Solution{
    public static HashSet<String> hash = new HashSet<String>();
    public static void cal(String[][] metrix, int x, int y, String k){
        if(x < 0 || y < 0 || x > 3 || y > 3) return;
        if(k.length() == 6) hash.add(k+metrix[x][y]);
        else {
            k = k + metrix[x][y];
            if(x+1 < 4) cal(metrix, x+1, y, k);
            if(x-1 > -1) cal(metrix, x-1, y, k);
            if(y-1 > -1) cal(metrix, x, y-1, k);
            if(y+1 < 4) cal(metrix, x, y+1, k);
        }
    }
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int T = Integer.parseInt(input.nextLine());
        int answer = 0;
        for(int i=1;i<=T;i++){
            String[][] metrix = new String[4][4];
            for(int j=0;j<4;j++) metrix[j] = input.nextLine().split(" ");
            for(int j=0;j<4;j++){
                for(int k=0;k<4;k++){
                    cal(metrix, j, k, "");
                }
            }
            System.out.println("#"+i+" "+hash.size());
            hash.clear();
        }
    }
    
}
