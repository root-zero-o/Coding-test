// 2024.06.01
// https://school.programmers.co.kr/learn/courses/30/lessons/181885

function solution(todo_list, finished) {
  let answer = [];

  finished.forEach((v, i) => {
    if (!v) {
      answer.push(todo_list[i]);
    }
  });

  return answer;
}
