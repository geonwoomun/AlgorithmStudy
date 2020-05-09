// LeetCode CheckStraightLine
var checkStraightLine = function(coordinates) {
    if(coordinates.length <= 2) return true;

    // coordinates.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
    let xrate = coordinates[1][0] - coordinates[0][0];
    let yrate = coordinates[1][1] - coordinates[0][1];
    
    for(let i = 3; i < coordinates.length; i++) {
        let x = coordinates[i][0] - coordinates[0][0];
        let y = coordinates[i][1] - coordinates[0][1];
        if(xrate * y !== yrate * x ) return false;
    }
    return true;
};

  

