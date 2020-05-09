// 프로그래머스 level2 올바른 괄호

function solution(s){
    const stack = [];
    for(const p of s) {
        if(p === '(') {
            stack.push(p);
        }
        if(p === ')') {
            if(!stack.length) {
                return false;
            } 
            stack.pop();
        }
    }

    return !stack.length;
}