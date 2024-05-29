// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181900

function solution(my_string, indices) {
  let arr = [...my_string];

  indices.forEach((v) => {
    arr[v] = "";
  });

  return arr.join("");
}
