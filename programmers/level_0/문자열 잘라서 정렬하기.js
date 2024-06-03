// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181866

function solution(myString) {
  return myString
    .split("x")
    .filter((v) => v.length > 0)
    .sort();
}
