// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181865

function solution(binomial) {
  const [a, op, b] = binomial.split(" ");

  if (op === "+") return +a + +b;
  else if (op === "-") return +a - +b;
  else return +a * +b;
}
