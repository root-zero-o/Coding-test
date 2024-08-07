const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const N = INPUT[0];
  const arr = INPUT[1].split(" ").map(Number);

  let count = 1;
  let cur = arr[0];

  for (let i = 1; i < N; i++) {
    if (arr[i] >= cur) {
      count++;
    }
    cur = arr[i];
  }

  console.log(count);
}

solution();