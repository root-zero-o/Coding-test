// 2024.06.01
// https://school.programmers.co.kr/learn/courses/30/lessons/181881

function solution(arr) {
  let x = 0;
  let prevArr = arr;

  while (true) {
    const changedArr = prevArr.map((v, i) => {
      if (v % 2 === 0 && v >= 50) return v / 2;
      else if (v % 2 === 1 && v < 50) return v * 2 + 1;
      else return v;
    });

    if (changedArr.every((a, i) => a === prevArr[i])) {
      break;
    } else {
      x++;
      prevArr = changedArr;
    }
  }

  return x;
}
