// def solution1(prices):
//     answer = [0 for _ in range(len(prices))]
//     stack = []
//     for i in range(len(prices)):
//         while len(stack) != 0 and prices[i] < prices[stack[len(stack) -1]]:
//             temp = stack.pop()
//             answer[temp] = i - temp
//         stack.append(i)
//     while len(stack):
//         temp = stack.pop()
//         answer[temp] = len(prices) - temp - 1

//     return answer

// print(solution1([1,2,3,2,3]))

function solution(prices) {
    let answer = new Array(prices.length).fill(0);
    let stack = [];
    let length = prices.length;
    for(let i = 0; i < length; i++) {
        while(stack.length && prices[i] < prices[stack[stack.length - 1]]) {
            let temp = stack.pop();
            answer[temp] = i - temp;
        }
        stack.push(i)
    }
    while(stack.length) {
        let temp = stack.pop();
        answer[temp] = length - temp - 1;
    }
    return answer;
}

console.log(solution([1,2,3,2,1]))