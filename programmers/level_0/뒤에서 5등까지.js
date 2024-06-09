// 2024.06.09
// https://school.programmers.co.kr/learn/courses/30/lessons/181853

function solution(num_list) {
    let arr = num_list.sort((a, b) => a - b);
    
    return arr.slice(0, 5)
}