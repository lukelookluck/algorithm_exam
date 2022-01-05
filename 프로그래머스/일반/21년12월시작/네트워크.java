class Solution {
    boolean[] check;

    public int solution(int n, int[][] computers) {
        int answer = 0;
        check = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (!check[i]) {
                dfs(i, n, computers);
                answer++;
            }
        }
        return answer;
    }

    private void dfs(int idx, int n, int[][] computers) {
        check[idx] = true;
        for (int i = 0; i < n; i++) {
            if (computers[idx][i] == 1 && !check[i]) {
                dfs(i, n, computers);
            }
        }
    }
}