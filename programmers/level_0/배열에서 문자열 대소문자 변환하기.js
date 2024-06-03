// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181875

function solution(strArr) {
  return strArr.map((v, i) => {
    if (i % 2 === 0) {
      return v.toLowerCase();
    } else {
      return v.toUpperCase();
    }
  });
}
