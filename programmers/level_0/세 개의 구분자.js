// 2024.06.04
// https://school.programmers.co.kr/learn/courses/30/lessons/181862

function solution(myStr) {
    const arr =  [...myStr].map((v) => v === 'a' || v === 'b' || v === 'c' ? ' ' : v).join('').split(' ').filter((v) => v.length > 0)
    return arr.length > 0 ? arr : ["EMPTY"]
}