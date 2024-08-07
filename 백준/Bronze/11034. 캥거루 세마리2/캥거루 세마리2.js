const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  let answer = "";
  for (let i = 0; i < INPUT.length; i++) {
    let gap = [];
    const testCase = INPUT[i].split(" ");
    for (let j = 0; j < 2; j++) {
      gap.push(testCase[j + 1] - testCase[j] - 1);
    }
    answer += Math.max(...gap) + "\n";
  }

  console.log(answer);
}

solution();
