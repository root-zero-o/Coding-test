// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181901

function solution(n, k) {
  const answer = [];

  for (let i = 1; i <= n; i++) {
    if (i % k === 0) {
      answer.push(i);
    }
  }

  return answer;
}
