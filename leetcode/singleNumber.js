// LeetCode easy singleNumber 
var singleNumber = function(nums) {
    let check = {};

    nums.forEach(v => {
        check[v] = check[v] ? check[v] + 1 : 1;
    })
    return Object.keys(check).reduce((acc, cur) => check[cur] === 1 ? acc + parseInt(cur) : acc, 0);
};

console.log(singleNumber([2,2,1]))