// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181897

function solution(n, slicer, num_list) {
  const [a, b, c] = slicer;

  if (n === 1) {
    return num_list.slice(0, b + 1);
  } else if (n === 2) {
    return num_list.slice(a);
  } else if (n === 3) {
    return num_list.slice(a, b + 1);
  } else {
    const arr = num_list.slice(a, b + 1).filter((v, i) => i % c === 0);
    return arr;
  }
}
