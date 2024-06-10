// 2024.06.09
// https://leetcode.com/problems/merge-sorted-array/description/

var merge = function(nums1, m, nums2, n) {    
    for(let i = m, j = 0; j < n; i++, j++){
        nums1[i] = nums2[j]
    }
    nums1.sort((a,b) => a-b)
};

// nums1을 변형시켜 공간 복잡도를 O(1)로 최소화하는 문제
// 시간 복잡도 : O(NlogN)

// another solution
var merge = function(nums1, m, nums2, n) {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;
    
    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
};

// 시간 복잡도 : O(N)