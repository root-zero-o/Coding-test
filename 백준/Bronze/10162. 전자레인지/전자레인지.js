const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  // .split(' ')
  .map(Number);

function solution() {
  let T = INPUT[0];
  const time = [300, 60, 10];
  let answer = "";

  if (T % 10 !== -0) {
    console.log(-1);
    return;
  }

  for (let i = 0; i < 3; i++) {
    answer += Math.floor(T / time[i]) + " ";
    T %= time[i];
  }

  console.log(answer);
}

solution();