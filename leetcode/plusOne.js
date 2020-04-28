// leetCode Plus One
function calculate(arr, x) {
    if(arr[x] < 9){
        arr[x] +=1;
        return;
    }
    else {
        arr[x] = 0
        if(x === 0){
            arr.unshift(1);
            return;
        }
        calculate(arr, x-1);
    }
}

var plusOne = function(digits) {
    let length = digits.length;
    calculate(digits, length-1);
    return digits;
};