// 2024.06.10
// https://leetcode.com/problems/majority-element/description/

// my solution
var majorityElement = function(nums) {
    const n = Math.ceil(nums.length / 2) - 1;
    nums.sort((a, b) => b - a);
    return nums[n]
};

// another solution 1
// time : O(N) / space : O(N)
var majorityElement = function(nums){
    const hash = {};
    let res = 0;
    let majority = 0;

    for(let n of nums){
        hash[n] = 1 + (hash[n] || 0);

        if(hash[n] > majority){
            res = n;
            majority = hash[n]
        }
    }

    return res;
}

