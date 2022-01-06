import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> q = new PriorityQueue<>();

        for (int x : scoville)
            q.add(x);

        while (q.peek() < K && q.size() > 1) {
            q.add(q.poll() + q.poll() * 2);
            answer++;
        }

        if (q.size() <= 1 && q.peek() < K)
            return -1;

        return answer;
    }
}