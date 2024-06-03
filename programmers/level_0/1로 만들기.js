// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181880

function solution(num_list) {
  let count = 0;
  let prevArr = num_list;

  while (true) {
    const changedArr = prevArr.map((v, i) => {
      if (v === 1) return 1;
      if (v % 2 === 0) {
        count++;
        return v / 2;
      } else {
        count++;
        return (v - 1) / 2;
      }
    });

    if (changedArr.every((v) => v === 1)) {
      break;
    }

    prevArr = changedArr;
  }
  return count;
}
