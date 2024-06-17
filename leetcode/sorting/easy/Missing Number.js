// 2024.06.17
// https://leetcode.com/problems/missing-number/description/

var missingNumber = function (nums) {
  let arr = new Array(nums.length + 1).fill(-1);

  for (let i = 0; i < nums.length + 1; i++) {
    arr[nums[i]] = nums[i];
  }

  for (let i = 0; i < arr.length + 1; i++) {
    if (arr[i] === -1) return i;
  }
  return 0;
};

// time : O(N)
// space : O(N)
