import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the gridSearch function below.
    static String gridSearch(String[] G, String[] P) {
        // G를 입력배열, P를 목표배열이라 하겠음
        int G_width = G[0].length(); // 입력배열의 가로길이 -> 목표배열 한줄씩 탐색시 사용됨. 
        int G_height = G.length; // 입력배열의 세로길이 -> 목표배열 탐색 중에 입력배열의 높이를 넘어가면 NO를 반환
        int P_width = P[0].length(); // 목표배열의 가로길이
        int P_height = P.length; // 목표배열의 세로길이 -> 목표배열 탐색 중에 목표배열의 높이를 넘어가면 YES를 반환
        int start_num = -1; 
        // 탐색중인 목표배열의 1 행이 13일떄, 입력배열에 01300130 과 같이 중복되서 나타날 수 있음
        // 이때 입력배열의 한줄에 대해 각각 검사하기 위해 사용하기도 하며
        // 목표배열의 1행이 위와 같이 13이고, 2행이 27일때, 입력배열이 다음과 같을 수 있음
        // 01300130
        // 99992799
        // 이러한 경우를 위해 각 입력배열의 각줄에 목표배열의 행이 포함되는지 여부뿐아니라,
        // 그 시작 인덱스가 일치하는지 알아야 하기 때문에 이때 start_num이 사용됨
        int count_from = -1;
        int count = 0;
        // count_from과 count변수는 입력배열의 탐색하고자 하는 목표배열의 행에 대해
        // 입력배열의 한 행에 몇개나 같은 문자열이 포함되어있는지를 저장함.
        // 즉, 위와 같이 01300130 같은 경우 count가 2가 되어서
        // 각각에 대해서 탐색을 진행해야 하기 때문에 탐색문을 2번 실행하게함
        for(int j=0;j<G_height;j++){ // 입력배열의 한 행씩 탐색을 진행함
            if(G[j].contains(P[0])){ // 어찌되었는 목표배열의 첫번째 행이 입력배열에 존재할때 탐색을 시작해야함
                count = 0; 
                start_num = -1;
                // count와 start_num 초기화, count_from은 아래 while문을 통해서 자동적으로 초기화가 됨
                while((count_from = G[j].indexOf(P[0], count_from + 1))>=0){
                    // G[j]에 P[0]가 어느 인덱스에서 시작되는지 확인, 이때 그 뒤에 count_from+1 인자를 줌으로써
                    // G[j]의 count_from+1 인덱스 이후로 부터 확인을 하는 것,
                    // 존재한다면 양수값을 주기때문에 count 값을 하나 증가,
                    // 존재하지 않는다면 -1을 반환하므로 count_from이 초기화 되는 기능이 됨
                    count++;
                }
                // 실질적인 탐색문 시작
                for(int i=0;i<count;i++){
                    start_num = G[j].indexOf(P[0], start_num+1); // G[j]에서 P[0]가 포함된 인덱스를 구함
                    for(int k=0;k<P_height;k++){ // 이제 모든 목표배열행에 대해 탐색할 것
                        if((G[j+k].contains(P[k]))&(start_num == G[j+k].indexOf(P[k],start_num))){
                            // 목표배열의 다음행이 입력배열의 다음행에 포함되어있는지 확인하면서
                            // 그 시작위치가 동일한지 확인 -> else: 즉, 그게 아니면 목표배열의 첫행에 대해 재탐색
                            if(k+1 == P_height){
                                // k가 증가하다가 목표배열의 높이를 넘어가면 모든 목표배열에 대해 탐색이 된 것이므로
                                // YES를 반환
                                return "YES";
                            }else if(j+k+1 == G_height){
                                // k가 증가하다가 목표배열의 높이를 넘어가기 전에 입력배열의 높이를 넘어가면
                                // 입력배열에 목표배열이 완전하게 존재하지 않는 것이기 때문에 NO를 반환
                                return "NO";
                            }
                        }else{
                            break;
                        }
                    }
                }
            }
        } // 해당 for문이 끝난 것은 입력배열에 목표배열이 포함되어 있지 않다는 뜻이기에 NO를 반환함
        return "NO";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String[] RC = scanner.nextLine().split(" ");

            int R = Integer.parseInt(RC[0]);

            int C = Integer.parseInt(RC[1]);

            String[] G = new String[R];

            for (int i = 0; i < R; i++) {
                String GItem = scanner.nextLine();
                G[i] = GItem;
            }

            String[] rc = scanner.nextLine().split(" ");

            int r = Integer.parseInt(rc[0]);

            int c = Integer.parseInt(rc[1]);

            String[] P = new String[r];

            for (int i = 0; i < r; i++) {
                String PItem = scanner.nextLine();
                P[i] = PItem;
            }

            String result = gridSearch(G, P);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
