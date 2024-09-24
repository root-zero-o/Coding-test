const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const N = Number(INPUT[0]);
  const lst_N = INPUT[1]
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);
  const M = Number(INPUT[2]);
  const lst_M = INPUT[3].split(" ").map(Number);

  let answer = "";

  const lowerBound = (target, start, end) => {
    while (start < end) {
      let mid = parseInt((start + end) / 2);
      if (lst_N[mid] >= target) end = mid;
      else start = mid + 1;
    }
    return end;
  };

  const upperBound = (target, start, end) => {
    while (start < end) {
      let mid = parseInt((start + end) / 2);
      if (lst_N[mid] > target) end = mid;
      else start = mid + 1;
    }
    return end;
  };

  const countByRange = (leftValue, rightValue) => {
    let rightIndex = upperBound(rightValue, 0, lst_N.length);
    let leftIndex = lowerBound(leftValue, 0, lst_N.length);
    return rightIndex - leftIndex;
  };

  for (let i = 0; i < M; i++) {
    const num = countByRange(lst_M[i], lst_M[i]);
    answer += `${num} `;
  }

  console.log(answer);
}

solution();