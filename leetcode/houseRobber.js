var rob = function(nums) {
    const arr = [];
    const length = nums.length;
    if (length === 0){
        return 0;
    }
    if(length < 2) {
        return nums[0];
    }
    arr[0] = nums[0];
    arr[1] = nums[1];
    if (length >= 3) {
        arr[2] = nums[2] + nums[0];
    }
    for(let i = 3; i < nums.length; i++){
        arr[i] = nums[i] + Math.max(arr[i-2], arr[i-3])
    }
    let answer = Math.max(...arr);
    return answer
};

var rob1 = function(nums) {
    const length = nums.length;
    if (length <= 2) {
        return Math.max(0, ...nums);
    };
    const arr = [];
    arr[0] = nums[0];
    arr[1] = Math.max(nums[0], nums[1]);
    for(let i = 2; i < nums.length; i++){
        arr[i] = Math.max(arr[i-1], nums[i] + arr[i-2]);
    }
    return Math.max(...arr);
};

console.log(rob(
    [1,1,1]))