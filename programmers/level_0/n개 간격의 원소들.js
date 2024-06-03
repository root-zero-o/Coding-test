// 2024.06.01
// https://school.programmers.co.kr/learn/courses/30/lessons/181888

function solution(num_list, n) {
  const answer = [];
  num_list.forEach((v, i) => {
    if (i % n === 0) {
      answer.push(v);
    }
  });
  return answer;
}
