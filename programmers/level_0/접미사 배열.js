// 2024.05.26.
// https://school.programmers.co.kr/learn/courses/30/lessons/181909

function solution(my_string) {
    let answer = [];
    new Array(my_string.length).fill(undefined).forEach((v, i) => {
        answer.push(my_string.slice(i, my_string.length + 1))
    })
    
    return answer.sort()
}