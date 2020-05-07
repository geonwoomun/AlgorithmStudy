var findComplement = function(num) {
    let temp = num.toString(2);
    let a = '';
    for(const s of temp) {
        a += s === '1' ? "0" : "1";
    }
    return parseInt(a, 2);
};

let a = 1
console.log(a.toString(2));