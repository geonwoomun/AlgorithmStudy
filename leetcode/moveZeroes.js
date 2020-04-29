// leetcode moveZeroes

var moveZeroes = function(nums) {
    let length = nums.length;
    let i = 0;
    let check = 0;
    while(check < length) {
        if (nums[i] === 0) {
            let temp = nums.splice(i,1)[0];
            nums.push(temp);
            
        }
        else {
            i++;
        }
        check++;
    }
};
