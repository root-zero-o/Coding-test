// 2024.06.25
// https://leetcode.com/problems/longest-harmonious-subsequence/description/

// my solution
var findLHS = function (nums) {
  let obj = {};

  for (let i = 0; i < nums.length; i++) {
    obj[nums[i]] = (obj[nums[i]] || 0) + 1;
  }

  let answer = 0;
  let keys = Object.keys(obj).sort((a, b) => a - b);

  for (let i = 0; i < keys.length - 1; i++) {
    const first = keys[i];
    const second = keys[i + 1];

    if (second - first === 1) {
      if (obj[first] + obj[second] > answer) {
        answer = obj[first] + obj[second];
      }
    }
  }

  return answer;
};

// another solution
// 방식은 같은 것 같다
var findLHS = function (nums) {
  let map = {},
    res = 0;

  for (let n of nums) map[n] = ~~map[n] + 1;

  for (let n in map) if (map[+n + 1]) res = Math.max(res, map[n] + map[+n + 1]);

  return res;
};
