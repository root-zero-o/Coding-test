// 2024.06.04
// https://school.programmers.co.kr/learn/courses/30/lessons/181861

function solution(arr) {
    const answer = [];
    arr.forEach((v) => {
        let a = 0;
        while(a < v){
            answer.push(v);
            a++
        }
    })
    
    return answer;
}

// 이런 방법이,,
// function solution(arr) {
//     return arr.reduce((list, num) => [...list, ...new Array(num).fill(num)], []);
// }