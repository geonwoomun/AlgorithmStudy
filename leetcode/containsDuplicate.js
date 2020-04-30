// leetcode contains Duplicate

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

var containsDuplicate = function(nums) {
    const set = new Set(nums);
    
    return set.size !== nums.length
};