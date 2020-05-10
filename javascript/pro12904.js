function solution(s)
{
    let left = 0;
    let right = s.length;
    let max = 0;
    max = check(s,left, right, max);
    return max;
}

function check(s, left, right, max) {
    if (s.length < 2) return true;
    let mid = Math.floor((left + right) / 2);
    let str1 = s.split('').slice(0, mid).reverse().join('');
    let str2 = s.slice(mid+1);
    if(str1 === str2) {
        max = Math.max(max, str1.length);
    }  
    max = check(s, left, mid-1, max);
    max = check(s, mid+1, right, max);
    return max;
}
console.log(solution('abcdcba'))