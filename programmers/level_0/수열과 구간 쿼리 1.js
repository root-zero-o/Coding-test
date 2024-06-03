// 2024.06.01
// https://school.programmers.co.kr/learn/courses/30/lessons/181883

function solution(arr, queries) {
  let answer = [...arr];

  queries.forEach((query) => {
    const [s, e] = query;

    answer = answer.map((v, i) => {
      if (i >= s && i <= e) {
        return v + 1;
      } else {
        return v;
      }
    });
  });

  return answer;
}

// function solution(arr, queries) {
//   for (let [s, e] of queries) for (let i = s; i <= e; i++) arr[i]++;
//   return arr;
// }
//
// for문으로 index s부터 e까지만 반복
