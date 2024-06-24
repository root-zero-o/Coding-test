// 2024.06.24.
// https://leetcode.com/problems/third-maximum-number/description/

var thirdMax = function (nums) {
  let first = -Infinity;
  let second = -Infinity;
  let third = -Infinity;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > first) {
      third = second;
      second = first;
      first = nums[i];
    } else if (nums[i] > second && nums[i] < first) {
      third = second;
      second = nums[i];
    } else if (nums[i] > third && nums[i] < second) {
      third = nums[i];
    }
  }

  return third === -Infinity ? first : third;
};

// time : O(N) - 88.71%
// space : O(1) - 99.25%
