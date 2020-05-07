// LeetCode Daily Temperatures

// 2중 포문 속도 엄청 느린 쓰레기 코드..
var dailyTemperatures = function(T) {
    let length = T.length;
    let answer = [];

    for (let i = 0; i < length; i++){
        for (let j = i+1; j < length; j++){
            if(T[i] < T[j]) {
                answer.push(j-i);
                break;
            }
            if(j == length-1) {
                answer.push(0);
            }
        }
    }
    answer.push(0);
    return answer;
};

// 좋은 코드
var dailyTemperatures = function(T) {
    let stack = [];
    let answer = new Array(T.length).fill(0);
    for(let i = 0; i < T.length; i++) {
        while(stack.length && T[i] > T[stack[stack.length-1]]) {
            let temp = stack.pop();
            answer[temp] = i - temp;
        }
        stack.push(i);
    }
    return answer;
 };
