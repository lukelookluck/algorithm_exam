function solution(jobs) {
    var answer = 0;
    let s = -1, n = 0, i = 0;
    const q = [];

    while (i < jobs.length) {
        jobs.map((j) => {
            if (s < j[0] && j[0] <= n) {
                q.push([j[1], j[0]]);
            }
        })

        if (q.length > 0) {
            let x = q.sort(([a, b], [c, d]) => a - c).shift();
            s = n;
            n += x[0];
            answer += n - x[1];
            i++;
        }
        else {
            n++;
        }
    }


    return parseInt(answer / jobs.length);
}