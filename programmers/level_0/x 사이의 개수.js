// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181867

function solution(myString) {
  const arr = [];

  myString.split("x").forEach((v) => {
    arr.push(v.length);
  });

  return arr;
}
