// 프로그래머스 예산

function solution(budgets, M) {
    let low =  0;
    let high = Math.max(...budgets);
    let mid;
    let answer = 0;
    
    while(low <= high ) {
        mid = parseInt((low + high) / 2, 10);
        let temp = budgets.reduce((prev, current) => {
            if (current > mid) {
                return prev + mid;
            }
            return prev + current;
        }, 0);
        if (temp > M ) {
            high = mid - 1;
        }  else {
            answer = answer > mid ? answer : mid;
            low = mid + 1;
        }
    }
    return answer;
}

const budgets = [120, 110, 140, 150];
const M = 485;

console.log(solution(budgets, M));