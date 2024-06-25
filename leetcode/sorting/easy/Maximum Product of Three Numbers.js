// 2024.06.25.
// https://leetcode.com/problems/maximum-product-of-three-numbers/description/

var maximumProduct = function (nums) {
  nums.sort((a, b) => b - a);
  const largest = nums[0] * nums[1] * nums[2];
  const largestWithNegative =
    nums[0] * nums[nums.length - 1] * nums[nums.length - 2];

  return Math.max(largest, largestWithNegative);
};
