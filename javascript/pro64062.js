function checkStone(stones, mid, k) {
    let now = 0; // 나우 0... now 가 커지거나 같으면 망함?
    for(let i = 0; i < stones.length; i++) {
        if(stones[i] <= mid) {
            now += 1;
        }
        else {
            now = 0;
        }
        if(now >= k) {
            return false;
        } 
    } 
    
    return true;
}
function solution(stones, k) {
    let left = 1;
    let right = 200000000;

    while(left < right - 1) {
        let mid = parseInt((left + right) / 2, 10);
        if (checkStone(stones, mid, k)) {
            left = mid;
        }
        else {
            right = mid;
        }
    }

    return left;
}
let stonse = [2,4,5,3,2,1,4,2,5,1];
let k = 3;
console.log(solution(stonse, k))