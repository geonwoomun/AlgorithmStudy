// leetcode best time to buy and sell stock

var maxProfit = function(prices) {
    let length = prices.length;
    let answer = 0;
    for (let i = 0; i < length-1; i++) {
        for(let j = i + 1; j< length; j++) {
            if (prices[i] < prices[j]){
                answer = Math.max(answer, prices[j] - prices[i]);
            }
        }
    }
    return answer;
};

const maxProfit = prices => {
    let maxDiff = 0;
    let highestMax = 0;
    for (let i = prices.length-1; i >= 0; i--) {
        highestMax = Math.max(prices[i], highestMax);
        const diff = highestMax - prices[i];
        maxDiff = Math.max(maxDiff,diff);
    }
    return maxDiff
};