function solution(array, commands) {
    var answer = [];

    commands.map(c => {
        let temp = array.slice(c[0] - 1, c[1]).sort((a, b) => a - b);
        answer.push(temp[c[2] - 1]);
    })

    return answer;
}