function calculateNumber(num) {
    if (num < 0){
        return Math.abs(num);
    }
    return num;
}
function solution(p,s) {
    let arr = p.split('');
    let answer = arr.reduce((acc, current, index) => {
        let first = Number(current);
        let second = Number(s[index]);
        if (calculateNumber(first - second) > 5) {
            if (first <= 5) {
                return acc + first + 10 - second
            }
            return acc + 10- first + second;
        }
        else {
            return acc + calculateNumber(first - second)
        }
    }, 0)
    return answer;
}
let p = "82195";
let s = "64723";
console.log(solution(p,s));
