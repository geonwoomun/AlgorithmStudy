// leetcode firstUnizueCharacter

var firstUniqChar = function (s) {
  if (s.length === 1) return 0;
  for (let i = 0; i < s.length; i++) {
    if (s.indexOf(s[i]) === s.lastIndexOf(s[i])) {
      return i;
    }
  }
  return -1;
};

var firstUniqChar = function (s) {
  var map = new Map();
  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      map.set(s[i], 2);
    } else {
      map.set(s[i], 1);
    }
  }

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i]) && map.get(s[i]) === 1) {
      return i;
    }
  }
  return -1;
};
