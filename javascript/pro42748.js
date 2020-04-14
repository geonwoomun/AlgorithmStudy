function ascSort(a,b) {
    return a - b;
}
function solution(array, commands) {
    const answer = commands.map(value => {
        let temp = array.slice(value[0]-1, value[1]);
        temp.sort(ascSort);
        return temp[value[2]-1]
    });
    return answer;
}
let array = [1,5,2,6,3,7,4]
let commansds = [[2,5,3], [4,4,1], [1,7,3]]

console.log(solution(array, commansds))