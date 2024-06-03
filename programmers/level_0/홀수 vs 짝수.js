// 2024.06.01
// https://school.programmers.co.kr/learn/courses/30/lessons/181887

function solution(num_list) {
  let odd = 0;
  let even = 0;

  num_list.forEach((v, i) => {
    if (i % 2 === 0) {
      odd += v;
    } else {
      even += v;
    }
  });

  return Math.max(odd, even);
}
