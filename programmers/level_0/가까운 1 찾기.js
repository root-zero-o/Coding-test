// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181898

function solution(arr, idx) {
  let answer = undefined;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 1 && i >= idx) {
      answer = i;
      break;
    }
  }

  return typeof answer === "number" ? answer : -1;
}

// 같거나 큰이 되어야 함(문제 오타)
