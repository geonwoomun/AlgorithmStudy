var findAnagrams = function(s, p) {
    let length = p.length;
    let check = {}
    for(let v of p) {
        check[v] = check[v] ? check[v] + 1 : 1;
    }

    let answer = [];
    let temp = {};
    let now = 0;
    let firstIndex = 0;
    for(let i = 0; i < s.length; i++){
        let v = s[i];
        now += 1;
        temp[v] = temp[v] ? temp[v] + 1 : 1;
        if(now === length) {
            if(checkObject(temp, check)) {
                answer.push(firstIndex);
            } 
            if(temp[s[firstIndex]] && temp[s[firstIndex]] > 1) {
                temp[s[firstIndex]] -= 1;
            }
            else {
                delete temp[s[firstIndex]];
            }
            firstIndex += 1;
            now -=1;
        }
    }
    return answer;
};

function checkObject(s, t){
    let check = true;
    for(let key in s) {
        if(s[key] !== t[key]) {
            check = false;
            break;
        }
    }
    return check;
}

// let a = {a: 1, b:2, c:3};
// let c = {a:1, b:2, c: 3}
// console.log(checkObject(a,c));



var findAnagrams = function(s, p) {
    let length = p.length;
    let check = new Map();
    for(let v of p) {
        if(check.has(v)){
            check.set(v, check.get(v) + 1);
        }
        else {
            check.set(v, 1);
        }
    }

    let answer = [];
    let temp = new Map();
    let now = 0;
    let firstIndex = 0;
    for(let i = 0; i < s.length; i++){
        let v = s[i];
        now += 1;
        if(temp.has(v)) {
            temp.set(v, temp.get(v) + 1);
        }
        else {
            temp.set(v, 1);
        }
        if(now === length) {
            if(checkObject(temp, check)) {
                answer.push(firstIndex);
            } 
            if(temp.has(s[firstIndex]) && temp.get(s[firstIndex]) > 1) {
                temp.set(s[firstIndex], temp.get(s[firstIndex]) - 1);
            }
            else {
                temp.delete(s[firstIndex]);
            }
            firstIndex += 1;
            now -=1;
        }
    }
    return answer;
};

function checkObject(s, t){
    let check = true;
    for(let key of s.keys()) {
        if(s.get(key) !== t.get(key)) {
            check = false;
            break;
        }
    }
    return check;
}

let s = "cbaebabacd";
let p = "abc";


console.log(findAnagrams(s,p));