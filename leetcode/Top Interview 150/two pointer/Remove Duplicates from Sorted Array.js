// 2024.07.08.
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

// my solution
var removeDuplicates = function (nums) {
  let idx = 1;
  let val = nums[0];

  for (i = 1; i < nums.length; i++) {
    if (val !== nums[i]) {
      nums[idx] = nums[i];
      idx++;
      val = nums[i];
    }
  }
  return idx;
};

// time: O(N)
// space: O(1)
