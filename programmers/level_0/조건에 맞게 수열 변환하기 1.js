// 2024.06.01
// https://school.programmers.co.kr/learn/courses/30/lessons/181882

function solution(arr) {
  arr.forEach((v, i) => {
    if (v % 2 === 0 && v >= 50) {
      arr[i] = v / 2;
    } else if (v % 2 === 1 && v < 50) {
      arr[i] = v * 2;
    }
  });

  return arr;
}
