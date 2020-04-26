// 프로그래머스 탑 

function solution(heights) {
    const answer = [];
    for (let i = heights.length-1; i >= 0; i--) {
        let check = false;
        for (let j = i-1; j >= 0; j--) {
            if(heights[i] < heights[j]) {
                answer.unshift(j+1);
                check = true;
                break;
            }
        }
        if (!check) {
            answer.unshift(0);
        }
    }
    return answer;
}

function solution1(heights) {
    return heights.map((v, i) => {
        while (i) {
            i--;
            if (heights[i] > v) {
                return i + 1;
            }
        }
        return 0;
    })
}