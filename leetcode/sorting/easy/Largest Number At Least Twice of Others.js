// 2024.06.26
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

var dominantIndex = function (nums) {
  const sortedNums = [...nums].sort((a, b) => b - a);
  if (sortedNums[0] >= sortedNums[1] * 2) {
    return nums.indexOf(sortedNums[0]);
  } else return -1;
};
