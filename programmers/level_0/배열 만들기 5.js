// 2024.05.26.
// https://school.programmers.co.kr/learn/courses/30/lessons/181912

function solution(intStrs, k, s, l) {
    let answer = [];
    intStrs.forEach((intStr) => {
        let num = Number(intStr.split('').slice(s, s+l).join(''));
        if(num > k){
            answer.push(num)
        }
    })
    
    return answer;
}