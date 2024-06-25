// 2024.06.26
// https://leetcode.com/problems/set-mismatch/description/

var findErrorNums = function(nums) {
    let dup = 0;
    let missing = 0;

    const frequency = new Map();
    for(let num of nums){
        frequency.set(num, (frequency.get(num) || 0) + 1);
    }

    for(let i = 1; i <= nums.length; i++){
        if(frequency.get(i) === 2){
            dup = i
        }

        else if(!frequency.has(i)){
            missing = i
        }
    }
    return [dup, missing]
};

// sort는 보통 hashMap 사용해서 나온 횟수를 구해 풀거나
// pointer를 활용하는 듯