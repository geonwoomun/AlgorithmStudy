// LeetCode MinimumPathSum medium

var minPathSum = function(grid) {
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if(i > 0 && j > 0){
                grid[i][j] = grid[i][j] + Math.min(grid[i][j-1], grid[i-1][j]);
            }
            else{
                if(j > 0){
                    grid[i][j] += grid[i][j-1]; 
                }
                if(i > 0) {
                    grid[i][j] += grid[i-1][j];
                }
            }
        }
    }
    return grid[grid.length-1][grid[0].length-1];
};

minPathSum([[1,2,5],[3,2,1]])