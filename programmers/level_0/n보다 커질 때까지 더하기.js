// 2024.06.01
// https://school.programmers.co.kr/learn/courses/30/lessons/181884

function solution(numbers, n) {
  let total = 0;

  for (let i = 0; i < numbers.length; i++) {
    let cur = total + numbers[i];
    total = cur;
    if (cur > n) {
      break;
    }
  }

  return total;
}
