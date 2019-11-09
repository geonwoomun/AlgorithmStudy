function solution(k, room_number) {
    let answer = [];

    let temp = []
    for(let i = 0; i< k; i++){
        temp[i] = 0
    }
    for(let i = 0; i < room_number.length; i++){
        if(temp[room_number[i]-1] == 0){
            answer.push(room_number[i])
            temp[room_number[i]-1] = 1
        }
        else {
            let s = temp.indexOf(0, room_number[i])
            answer.push(s+1)
            temp[s] = 1
        }
    }
    return answer;
}