var isHappy = function(n) {
    let set = new Set();
    let temp = n
    while(temp !== 1) {
        let strN = String(temp);
        let s = 0;
        for(const num of strN){
            s += Number(num)**2;
        }
        if(set.has(s)) {
            return false;
        }
        else {
            set.add(s);
            temp = s;
        }
    }
    return true;
};

console.log(isHappy(19))