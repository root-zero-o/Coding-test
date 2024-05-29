// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181894

function solution(arr) {
  const idxArr = [];

  arr.forEach((v, i) => {
    if (v === 2) idxArr.push(i);
  });

  if (idxArr.length === 0) return [-1];
  else if (idxArr.length === 1) return [arr[idxArr[0]]];
  else {
    return arr.slice(idxArr[0], idxArr[idxArr.length - 1] + 1);
  }
}

// lastIndexOf 라는 메서드가 있다 ㅠㅠ
