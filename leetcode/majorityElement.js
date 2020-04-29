// leetcode Majority Element

var majorityElement = function(nums) {
    const count = {};
    const point = nums.length / 2;
    for (let i = 0; i < nums.length; i++) {
        count[nums[i]] = count[nums[i]] + 1 || 1;
        if(count[nums[i]] > point) return nums[i];
    };
}

console.log(majorityElement([3,2,3]))