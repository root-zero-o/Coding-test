// 2024.06.10
// https://leetcode.com/problems/valid-anagram/description/

var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  let cur = 0;
  const arrS = s.split("").sort();
  const arrT = t.split("").sort();

  while (cur < s.length) {
    if (arrS[cur] !== arrT[cur]) return false;
    else cur++;
  }
  return true;
};

// another solution
var isAnagram = function (s, t) {
  const counter = new Array(26).fill(0);
  for (let idx = 0; idx < s.length; idx++) {
    counter[s.charCodeAt(idx) - 97]++;
  }
  for (let idx = 0; idx < t.length; idx++) {
    counter[t.charCodeAt(idx) - 97]--;
  }
  for (let idx = 0; idx < 26; idx++) {
    if (counter[idx] != 0) return false;
  }
  return true;
};
