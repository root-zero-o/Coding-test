// 2024.06.25.
// https://leetcode.com/problems/relative-ranks/description/

var findRelativeRanks = function(score) {
    const ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"];
    const sortedScore = [...score].sort((a, b) => b - a);

    return score.map((v, i) => {
        const index = sortedScore.indexOf(v);
        if(index < 3) return ranks[index];
        else return `${index+1}`
    })
};

// time: O(nlogn);
// space : O(n)