// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181864

function solution(myString, pat) {
  let str = "";
  [...myString].forEach((v) => {
    if (v === "A") str += "B";
    else str += "A";
  });

  return str.includes(pat) ? 1 : 0;
}
