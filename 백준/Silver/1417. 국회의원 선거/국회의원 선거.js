const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  // .split(' ')
  .map(Number);

function solution() {
  const N = INPUT[0];
  if (N === 1) {
    console.log(0);
    return;
  }

  const arr = INPUT.slice(1);

  let count = 0;
  let target = arr[0];
  let last = arr.slice(1).sort((a, b) => b - a);

  while (true) {
    if (target > last[0]) {
      break;
    } else {
      target++;
      last[0]--;
      count++;
      last.sort((a, b) => b - a);
    }
  }

  console.log(count);
}

solution();