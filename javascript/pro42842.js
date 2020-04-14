// 프로그래머스 level2 카펫

function solution(brown, red) {
    const answer = [];
    let temp = brown + red
    // 가로길이는 세로 길이와 같거나, 세로길이보다 길다.
    let height = 3;
    let width = parseInt(temp / height)

    while (width >= height) {
        if ((width - 2) * (height - 2) == red) {
            answer.push(width);
            answer.push(height);
            break;
        }
        width -= 1
        height = parseInt(temp / width)
    }
    return answer;
}


console.log(parseInt(10/3))