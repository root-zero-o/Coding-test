// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181891

function solution(num_list, n) {
  const arr1 = num_list.slice(0, n);
  const arr2 = num_list.slice(n);

  return [...arr2, ...arr1];
}
