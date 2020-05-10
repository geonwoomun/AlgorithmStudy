function solution(n) {
    
    let left = 1;
    let right = 1;
    let count = 0;
    let result = 0;
    while(left <= right && left <= n){
        if(result === n) {
            count +=1;
            result -= left;
            left +=1;
        }
        else if(result < n) {
            result += right;
            right +=1;
        }
        else {
            result -= left;
            left +=1;
        }
        // console.log(left, right, result, count);
    }
    return count;
}

console.log(solution(15))