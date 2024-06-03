// 2024.06.04
// https://school.programmers.co.kr/learn/courses/30/lessons/181871

function solution(myString, pat) {
  let count = 0;
  let str = myString;

  [...myString].forEach(() => {
    const idx = str.indexOf(pat);
    if (idx > -1) {
      count++;
      str = str.slice(idx + 1);
    }
  });

  return count;
}
