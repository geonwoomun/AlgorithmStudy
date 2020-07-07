/**
 * @param {number[][]} grid
 * @return {number}
 */

var islandPerimeter = function (grid) {
  const height = grid.length;
  const width = grid[0].length;
  const move = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  let count = 0;

  function dfs(nowH, nowW) {
    grid[nowH][nowW] += 1;

    for (let i = 0; i < 4; i++) {
      let [mx, my] = move[i];
      let [moveW, moveH] = [nowW + mx, nowH + my];
      if (
        moveW < 0 ||
        moveH < 0 ||
        moveW > width - 1 ||
        moveH > height - 1 ||
        grid[moveH][moveW] === 0
      )
        count++;
      else {
        if (grid[moveH][moveW] === 1) {
          dfs(moveH, moveW);
        }
      }
    }
  }

  for (let h = 0; h < height; h++) {
    for (let w = 0; w < width; w++) {
      if (grid[h][w] === 1) {
        dfs(h, w);
        return count;
      }
    }
  }
  return 0;
};

const grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0],
];

console.log(islandPerimeter(grid));
