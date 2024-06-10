// 2024.06.10
// https://leetcode.com/problems/contains-duplicate/description/

var containsDuplicate = function (nums) {
  let hash = {};
  let answer = false;

  for (let i = 0; i < nums.length; i++) {
    hash[nums[i]] = (hash[nums[i]] || 0) + 1;
    if (hash[nums[i]] > 1) {
      answer = true;
      break;
    }
  }
  return answer;
};

// another solution
var containsDuplicate = function (nums) {
  const s = new Set(nums);
  return s.size !== nums.length;
};
