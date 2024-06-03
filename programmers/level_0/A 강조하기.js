// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181874

function solution(myString) {
  let answer = "";
  [...myString].forEach((v) => {
    if (v === "a" || v === "A") {
      answer += "A";
    } else {
      answer += v.toLowerCase();
    }
  });

  return answer;
}

// const solution = (s) => s.toLowerCase().replaceAll("a", "A");
