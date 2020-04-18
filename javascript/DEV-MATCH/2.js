function calcualteDirection(num) {
    if (num > 3) {
        return 4 - num;
    }
    else if (num < 0) {
        return 4 + num;
    }
    return num;
}
function okayXY(x,y, N) {
    if (x >= 0 && x < N && y >= 0 && y < N) {
        return true;
    }
    return false;
}
function solution(office, r, c, move) {
    const goVaccum = [[1, 0], [0, 1], [-1, 0], [0, -1]]; // 동 남 서 북

    let nowDirection = 3;
    let nowY = r;
    let nowX = c;
    const N = office.length;
    let answer = office[nowY][nowX]; // 첫번째칸 청소하고 시작.
    office[nowY][nowX] = 0;
    
    move.forEach(value => {
        if (value === 'right') {
            nowDirection = calcualteDirection(nowDirection+1);
        }
        else if(value === 'left') {
            nowDirection = calcualteDirection(nowDirection - 1);
        }
        else {
            let [x, y] = goVaccum[nowDirection];
            let [tempX, tempY] = [nowX+x, nowY+y];
            if(okayXY(tempX,tempY, N) && office[tempY][tempX] >= 0){
                nowY = tempY;
                nowX = tempX;
                answer += office[nowY][nowX];
                office[nowY][nowX] = 0;
            }
        }
    })

    return answer;
}

let office = [[5,-1,4],[6,3,-1],[2,-1,1]];
let r = 1;
let c = 0;
let move = ["go","go","right","go","right","go","left","go"];

console.log(solution(office,r,c,move));