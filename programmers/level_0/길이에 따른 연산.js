// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181879

function solution(num_list) {
  const length = num_list.length;

  if (length >= 11) {
    return num_list.reduce((acc, cur) => acc + cur, 0);
  } else {
    return num_list.reduce((acc, cur) => acc * cur, 1);
  }
}
