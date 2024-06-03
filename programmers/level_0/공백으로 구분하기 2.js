// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181868

function solution(my_string) {
  return my_string.split(" ").filter((v) => v.length > 0);
}

// function solution(my_string) {
//   return my_string.trim().split(/ +/);
// }
