// leetcode    findAllNumbers ~~

var findDisappearedNumbers = function(nums) {
    const arr = new Array(nums.length+1).fill(0);
    for(let i = 0; i < nums.length; i++) {
        arr[nums[i]]++;
    }
    let answer = [];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] === 0){
            answer.push(i);
        }
    }
    return answer;
};

console.log(findDisappearedNumbers([1,1]))