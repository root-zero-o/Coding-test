const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  // .split(' ')

function solution() {

  const N = INPUT[0];
  const arrA = INPUT[1].split(' ').map(Number);
  const arrB = INPUT[2].split(' ').map(Number);

  let gap = 0;

  for(let i = 0; i < N; i++){
    gap += Math.abs(arrA[i] - arrB[i]);
  }

  console.log(gap / 2);
}

solution();