// 2024.06.25.
// https://leetcode.com/problems/array-partition/description/

var arrayPairSum = function(nums) {
    nums.sort((a, b) => a - b);

    let groupedNums = [];
    let answer = 0;
    for(let i = 0; i < nums.length; i++){
        if(i % 2 === 0) groupedNums.push([nums[i], nums[i+1]]);
    }
    groupedNums.forEach((v) => answer += Math.min(v[0], v[1]))

    return answer;
};

// another solution
var arrayPairSum = function(nums) {
    nums.sort((a,b) => a-b)
    var sum = 0
    for(var i = 0; i<nums.length; i+= 2){
        sum += nums[i]
    }
    return sum
};