// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181899

function solution(start, end_num) {
  const answer = [];

  for (let i = end_num; i <= start; i++) {
    answer.push(i);
  }

  return answer.sort((a, b) => b - a);
}
