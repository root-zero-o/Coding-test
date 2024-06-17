// 2024.06.24
//  https://leetcode.com/problems/intersection-of-two-arrays/description/

// my solution
var intersection = function (nums1, nums2) {
  let arr = [];

  let set = Array.from(new Set(nums1));

  for (let i = 0; i < set.length; i++) {
    if (nums2.includes(set[i])) arr.push(set[i]);
  }
  return arr;
};

// another solution
var intersection = function (nums1, nums2) {
  let result = new Set();
  for (let i = 0; i < nums2.length; i++) {
    if (nums1.includes(nums2[i])) {
      result.add(nums2[i]);
    }
  }
  return [...result];
};
