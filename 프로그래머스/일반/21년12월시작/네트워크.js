function solution(n, computers) {
    var answer = 0;
    const check = new Array(n).fill(false);

    function bfs(idx) {
        check[idx] = true;

        for (let i = 0; i < n; i++) {
            if (computers[idx][i] && !check[i]) {
                bfs(i);
            }
        }
    }

    for (let i = 0; i < n; i++) {
        if (!check[i]) {
            answer++;
            bfs(i);
        }
    }
    return answer;
}