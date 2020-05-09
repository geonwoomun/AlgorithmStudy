function solution(n, money) {
    const dp = new Array(n+1).fill(0);
    for(let i = 0; i <= n; i++) {
        dp[i] = (i % money[0] === 0) ? 1 : 0;
    }
    for(let i = 1; i < money.length; i++) {
        for(let j = money[i]; j <= n; j++) {
                dp[j] += dp[j-money[i]];
        }
    }
    return dp[n];
}

console.log(solution(5, [1,2,5]))

// 4 ->  1, 1, 1, 1,  1, 1, 2,/ 2,