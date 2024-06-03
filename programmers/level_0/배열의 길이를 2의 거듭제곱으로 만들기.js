// 2024.06.04
// https://school.programmers.co.kr/learn/courses/30/lessons/181857

function solution(arr) {
    let length = 2 ** (Math.ceil(Math.log2(arr.length)))
    
    return [...arr, ...new Array(length - arr.length).fill(0)]
}

// 로그 !!