// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181903?language=javascript

function solution(q, r, code) {
  var answer = "";

  [...code].forEach((v, i) => {
    if (i % q === r) {
      answer += v;
    }
  });

  return answer;
}
