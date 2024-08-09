
const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
// .split(' ')

function solution() {
  const row1 = INPUT[0].split(" ").map(Number);
  const total = row1[0];

  if (total === 0) {
    console.log(0);
    return;
  }

  const weight = row1[1];
  const books = INPUT[1].split(" ").map(Number);

  let count = 1;
  let cur = 0;

  for (let i = 0; i < total; i++) {
    if (cur + books[i] <= weight) {
      cur += books[i];
    } else {
      count++;
      cur = books[i];
    }
  }

  console.log(count);
}

solution();
