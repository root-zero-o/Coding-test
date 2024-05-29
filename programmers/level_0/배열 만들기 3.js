// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181895

function solution(arr, intervals) {
  let answer = [];

  intervals.forEach((v) => {
    const a = arr.slice(v[0], v[1] + 1);
    answer.push(...a);
  });
  return answer;
}
