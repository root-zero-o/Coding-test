// 2024.06.17
// https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

// my solution
var intersect = function (nums1, nums2) {
  let obj = {};
  let answer = [];

  for (let i = 0; i < nums1.length; i++) {
    obj[nums1[i]] = (obj[nums1[i]] || 0) + 1;
  }

  for (let i = 0; i < nums2.length; i++) {
    if (obj[nums2[i]]) {
      answer.push(nums2[i]);
      obj[nums2[i]]--;
    }
  }

  return answer;
};

// another solution
var intersect = function (nums1, nums2) {
  const map = new Map();
  for (const n of nums1) {
    if (map.has(n)) {
      map.set(n, map.get(n) + 1);
    } else {
      map.set(n, 1);
    }
  }
  const result = [];
  for (const n of nums2) {
    if (map.has(n) && map.get(n) > 0) {
      result.push(n);
      map.set(n, map.get(n) - 1);
    }
  }
  return result;
};

// 같은 원리로 hash map 사용
