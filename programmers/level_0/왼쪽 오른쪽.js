// 2024.05.29.
// https://school.programmers.co.kr/learn/courses/30/lessons/181890#

function solution(str_list) {
  const idxL = str_list.indexOf("l");
  const idxR = str_list.indexOf("r");

  if (idxL === -1 && idxR === -1) return [];
  if (idxL === -1) return str_list.slice(idxR + 1);
  if (idxR === -1) return str_list.slice(0, idxL);
  if (idxL < idxR) {
    return str_list.slice(0, idxL);
  } else {
    return str_list.slice(idxR + 1);
  }
}
