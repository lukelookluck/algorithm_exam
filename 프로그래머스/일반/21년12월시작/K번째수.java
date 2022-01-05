import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int x = 0;

        for (int[] c : commands){
            int[] temp = Arrays.copyOfRange(array, c[0] - 1, c[1]);
            Arrays.sort(temp);
            answer[x] = temp[c[2] - 1];
            x++;
        }

        return answer;
    }
}