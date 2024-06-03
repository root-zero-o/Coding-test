// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181870

function solution(strArr) {
  return strArr.filter((v) => {
    if (!v.includes("ad")) return v;
  });
}
