function dfs(grid, move, i, j) {
    grid[i][j] = -1;
    for(let s = 0; s < 4; s++) {
        let [x, y] = move[s];
        let cx = i + x;
        let cy = j + y;
        if(cx >= 0 && cy >= 0 && cx < grid.length && cy < grid[0].length && grid[cx][cy] === "1") {
            dfs(grid, move, cx, cy);
        }
    }
};
var numIslands = function(grid) {
    const move = [[0,1], [1, 0],[-1,0], [0,-1]];
    let count = 0;
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            if(grid[i][j] === "1") {
                dfs(grid, move,  i, j);
                count += 1;
            }
        }
    }
    return count;
};