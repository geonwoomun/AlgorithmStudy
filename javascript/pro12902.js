function solution(n) {
  const dp = new Array(n + 1).fill(0);
  dp[0] = 1;
  dp[2] = 3;
  let special = 0;
  if (n % 2 === 1) return 0;
  for (let i = 4; i <= n; i += 2) {
    special += dp[i - 4] * 2;
    dp[i] = (dp[i - 2] * 3 + special) % 1000000007;
  }
  return dp[n] % 1000000007;
}

console.log(solution(8));
