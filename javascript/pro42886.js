// 프로그래머스 저울 

function solution(weight) {
    weight.sort((a,b) => a-b);
    let temp = 1;
    weight.forEach(value => {
        if (temp < value ) {
            return;
        }
        temp += value;
    })
    return temp;
}

let weight = [3,1,6,2,7,30,1];
console.log(solution(weight))