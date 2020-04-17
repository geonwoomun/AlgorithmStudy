// 프로그래머스 위장

function solution(clothes) {
    let answer = 1;
    let temp = {};

    clothes.forEach(element => { // clothes 가 처음 이면 안 입는 것 + 자기꺼, 원래 있엇으면 자기거만 더해주면된다.
        if (temp[element[1]]){
            temp[element[1]] += 1
        }
        else {
            temp[element[1]] = 2
        }
    });

    answer = Object.keys(temp).reduce((acc, current) => acc * temp[current], answer) - 1; // 옷을 입을 수 잇는 경우의 수를 구하기 위해 곱해주고, 모두 안 입는 경우(1)를 빼준다.
    return answer;
}