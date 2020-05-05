var coinChange = function(coins, amount) {
    let answer = 0;
    coins.sort((a,b) => a-b);
    for(let i = coins.length - 1; i >=0; i--) {
        if(i === 0) {
            if(amount % coins[i] === 0) {
                answer += amount / coins[i]
                return answer;
            }
            else {
                return -1;
            }
        }
        if(amount >= coins[i]) {
            answer += parseInt(amount / coins[i]);
            amount = amount % coins[i];
        }
    }
};
let coins = [186,419,83,408];
let amount = 6249;
console.log(coinChange(coins, amount));