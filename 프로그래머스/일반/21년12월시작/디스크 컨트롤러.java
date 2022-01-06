import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0, s = -1, n = 0, i = 0;
        PriorityQueue<int[]> q = new PriorityQueue<int[]> (new Comparator<int[]> () {
            public int compare(int[] a, int[] b) {
                if (a[1] < b[1])
                    return -1;
                return 1;
            }
        });

        while (i < jobs.length) {
            for (int[] j : jobs) {
                if (s < j[0] && j[0] <= n) {
                    q.add(j);
                }
            }

            if (q.size() > 0){
                int[] x = q.poll();
                s = n;
                n += x[1];
                answer += n - x[0];
                i++;
            }
            else {
                n++;
            }
        }



        return Math.floorDiv(answer, jobs.length);
    }
}

