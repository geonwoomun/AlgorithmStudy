const Node = function () {
  this.keys = new Map();
  this.end = false;
  this.count = 0;
  this.plusCount = function () {
    this.count += 1;
  };
  this.setEnd = function () {
    this.end = true;
  };
  this.isEnd = function () {
    return this.end;
  };
};

const Trie = function () {
  this.root = new Node();

  this.add = function (input, node = this.root) {
    if (input.length === 0) {
      node.setEnd();
      return;
    } else if (!node.keys.has(input[0])) {
      node.keys.set(input[0], new Node());
    }
    node.plusCount();
    return this.add(input.substr(1), node.keys.get(input[0]));
  };

  this.isSubWord = function (word) {
    let node = this.root;
    while (word.length > 0) {
      if (!node.keys.has(word[0])) {
        return false;
      } else {
        node = node.keys.get(word[0]);
        word = word.substr(1);
      }
    }
    return node.count > 0 ? true : false;
  };

  this.isWord = function (word) {
    let node = this.root;
    while (word.length > 1) {
      if (!node.keys.has(word[0])) {
        return false;
      } else {
        node = node.keys.get(word[0]);
        word = word.substr(1);
      }
    }
    return node.keys.has(word) && node.keys.get(word).isEnd() ? true : false;
  };

  this.print = function () {
    let words = new Array();
    let search = function (node = this.root, string) {
      if (node.keys.size !== 0) {
        for (let letter of node.keys.keys()) {
          search(node.keys.get(letter), string.concat(letter));
        }
        if (node.isEnd()) {
          words.push(string);
        }
      } else {
        string.length > 0 ? words.push(string) : undefined;
        return;
      }
    };
    search(this.root, new String());
    return words.length > 0 ? words : null;
  };
};

const myTrie = new Trie();
myTrie.add('ball');
myTrie.add('bat');
myTrie.add('doll');
myTrie.add('dark');
myTrie.add('do');
myTrie.add('sense');
console.log('doll', myTrie.isWord('doll'));
console.log('dor', myTrie.isWord('dor'));
console.log('do', myTrie.isSubWord('do'));
console.log('doll', myTrie.isSubWord('doll'));
console.log('zzz', myTrie.isSubWord('zzz'));
console.log('ol', myTrie.isSubWord('ol'));
console.log(myTrie.print());
