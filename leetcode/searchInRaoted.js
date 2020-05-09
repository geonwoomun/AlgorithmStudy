// Leetcode ..
var search = function(nums, target) {
    let left = 0;
    let right = nums.length-1;
    while(left < right) {
        let mid = Math.floor((left + right) / 2);
        if(nums[mid] === target) return mid;
        if(nums[left] === target) return left;
        if(nums[right] === target) return right;

        if(nums[mid] > nums[left]) {
            if(target > nums[left] && target < nums[mid]) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }

        else if (nums[mid] < nums[right]) {
            if (target > nums[mid] && target < nums[right]){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        else {
            return - 1;
        }
    }
    return nums[left] === target ? left : -1;
};

let nums = [4,5,6,7,0,1,2];
let target = 0;
console.log(search(nums, target));