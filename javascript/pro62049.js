// js 프로그래머스 62049 종이접기

// def reverse(lists):
//     return [bit ^ 1 for bit in lists[::-1]]

// def solution(n):
//     answer = [0]
//     if (n > 1):
//         for i in range(2, n + 1):
//             answer = answer + [0] + reverse(answer)
//     return answer
function reverse(arr) {
    return arr.reverse().map(value => value^1);
}

function solution(n) {
    let answer = [0];
    if(n > 1) {
        for (let i = 2; i < n + 1; i++){
            answer = [...answer, 0, ...reverse(answer)];
        }
    }
    return answer;
}