// LeetCode Backsapce String Compare

var backspaceCompare = function(S, T) {
    let Sstack = [];
    let Tstack = [];

    for(const element of S) {
        if(element === '#') {
            if(Sstack.length) Sstack.pop();
        }
        else {
            Sstack.push(element);
        }
    }

    for(const element of T) {
        if(element === '#') {
            if(Tstack.length) Tstack.pop();
        }
        else {
            Tstack.push(element);
        }
    }

    return Sstack.join('') === Tstack.join('');
};