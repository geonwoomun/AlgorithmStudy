function solution(participant, completion) {
    const complete = {};
    let answer = '';
    participant.forEach(person => {
        if (complete[person]) {
            complete[person] += 1;
        }
        else {
            complete[person] = 1;
        }
    });
    completion.forEach(person => {
        complete[person] -= 1;
    });
    Object.keys(complete).forEach(person => {
        if (complete[person] > 0) {
            answer = person;
        }
    })
    return answer;
}

let p = ["leo","kiki", "eden"];
let complete = ["eden", "kiki"];
console.log(solution(p, complete));