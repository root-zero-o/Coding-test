// 2024.06.01
// https://school.programmers.co.kr/learn/courses/30/lessons/181886

function solution(names) {
  let answer = [];

  names.forEach((v, i) => {
    if (i % 5 === 0) {
      answer.push(v);
    }
  });

  return answer;
}

// for (let i = 0; i < names.length; i += 5) {
//   answer.push(names[i]);
// }
//
// for문 사용해 index를 5씩 건너뛰는 것이 더 효율적이다.
