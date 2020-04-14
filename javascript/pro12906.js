// 쉬운거부터 익숙해지기! 
// 프로그래머스 level1 같은 숫자는 싫어

function solution(arr) {
    let answer = [];
    let lastValue;
    arr.map((value) => {
        if (lastValue !== value){
            answer.push(value)
        }
        lastValue = value
    })
    
    return answer;
}