const games = ['3:1', '2:2', '1:3'];

const foo = (games) => {
  for (let i = 0; i < games.length; i++) {
    let value = games[i].split(':');
    console.log(value);
  }
};

console.log(foo(games));
