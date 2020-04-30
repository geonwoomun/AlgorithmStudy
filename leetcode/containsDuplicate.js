// leetcode contains Duplicate

// 내가 푼 코드
var containsDuplicate = function(nums) {
    const count = {};
    for (let i = 0; i < nums.length; i++) {
        if (count[nums[i]]) {
            return true;
        }
        count[nums[i]] = 1;
    }
    return false;
};

// 이거 좋네... 좋은 코드
var containsDuplicate = function(nums) {
    const set = new Set(nums);
    
    return set.size !== nums.length
};