// 2024.06.17
// https://leetcode.com/problems/find-the-difference/description/

// my solution
var findTheDifference = function (s, t) {
  let mapS = new Map();
  let mapT = new Map();

  for (let i = 0; i < s.length; i++) {
    if (mapS.has(s[i])) {
      mapS.set(s[i], mapS.get(s[i]) + 1);
    } else {
      mapS.set(s[i], 1);
    }
  }

  for (let i = 0; i < t.length; i++) {
    if (mapT.has(t[i])) {
      mapT.set(t[i], mapT.get(t[i]) + 1);
    } else {
      mapT.set(t[i], 1);
    }
  }

  for (let i = 0; i < t.length; i++) {
    if (mapS.get(t[i]) !== mapT.get(t[i])) {
      return t[i];
    }
  }
};

// another solution
var findTheDifference = function (s, t) {
  for (let letter of s) t = t.replace(letter, "");
  return t;
};
// 하나씩 소거해 남는 글자를 return
