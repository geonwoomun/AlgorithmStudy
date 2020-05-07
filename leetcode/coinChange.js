var coinChange = function(coins, amount) {    
    let dp = new Array(amount+1).fill(Infinity);
    coins.sort((a,b)=>a-b); 
    dp[0] = 0;
    for(let i=1; i<=amount; i++){
        for(let coin of coins){
            if(coin<=i){
                dp[i] = Math.min(dp[i], 1+dp[i-coin])
            }else{
                break;
            }
        }
    }
    return dp[amount] < Infinity ? dp[amount] : -1;
};

var coinChange = function(coins, amount) {
    let dp = new Array(amount + 1).fill(amount+1);
    coins.sort((a,b) => a - b);
    dp[0] = 0;
    for(let i = 1; i <= amount; i++) {
        for(let coin of coins) {
            if(coin<=i) {
                dp[i] = Math.min(dp[i], 1 + dp[i-coin]);
            }
            else {
                break;
            }
        }
    }
    return dp[amount] < amount + 1 ? dp[amount] : -1 ;
}

let coins = [186,419,83,408];
let amount = 6249;
console.log(coinChange(coins, amount));