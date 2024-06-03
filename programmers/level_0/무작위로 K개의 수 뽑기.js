// 2024.06.04
// https://school.programmers.co.kr/learn/courses/30/lessons/181858

function solution(arr, k) {
    let answer = Array.from(new Set(arr)).slice(0, k);
   
    while(k - answer.length > 0){
        answer.push(-1)
    }

    return answer;
}