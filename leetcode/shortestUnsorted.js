// LeetCode Shortest Unsorted Continuous Subarray
var findUnsortedSubarray = function(nums) {
    const temp = [...nums].sort((a,b)=> a-b);
    let first;
    let last;
    for(let i = 0; i < nums.length; i ++) {
        if(nums[i] !== temp[i]){
            if(first === undefined) {
                first = i;
            }
            last = i;
        }
    }

    return first !== undefined ? last-first + 1 : 0;
};