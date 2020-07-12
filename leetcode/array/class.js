// class App {
//   constructor(name, age) {
//     this.name = name;
//     this.age = age;
//   }
// }

// const app = new App('문건우', 26);

// console.log(app.name);
// console.log(app.age);

function Student(name, age) {
  if (!new.target) {
    throw new Error('new 키워드를 사용해주세요!');
  }
  this.name = name;
  this.age = age;
}

try {
  const student = new Student('문건우', 26);
  console.log(student);
  console.log(student.name, student.age);
} catch (e) {
  console.error(e);
}
console.log('1234');
