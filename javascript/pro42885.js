// 프로그래머스 구명보트

function solution(people, limit) {
    let answer = 0;
    people.sort((a,b) => a-b);
    let left = 0;
    let right = people.length - 1;

    while(left <= right) {
        if (people[left] + people[right] <= limit) {
            left += 1;
            right -= 1;
        }
        else {
            right -= 1;
        }
        answer += 1;
    }

    return answer;
}

function solution1(people, limit) {
    people.sort((a, b) => a - b)
    let i = 0
    for(let length = people.length-1; i < length; length--) {
        if(people[i] + people[length] <= limit ) i++
    }    
    return people.length-i;
}

let people = [70, 80, 50];
let limit = 100;

console.log(solution(people, limit));