// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181896

function solution(num_list) {
  let answer = undefined;
  for (let i = 0; i < num_list.length; i++) {
    if (num_list[i] < 0) {
      answer = i;
      break;
    }
  }

  return typeof answer === "number" ? answer : -1;
}
