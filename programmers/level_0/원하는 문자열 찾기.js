// 2024.06.03
// https://school.programmers.co.kr/learn/courses/30/lessons/181878

function solution(myString, pat) {
  const smMyString = myString.toLowerCase();
  const smPat = pat.toLowerCase();

  return smMyString.includes(smPat) ? 1 : 0;
}
