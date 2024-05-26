// 2024.05.26.
// https://school.programmers.co.kr/learn/courses/30/lessons/181914

function solution(number) {
    return number.split('').reduce((acc, cur) => acc + Number(cur), 0) % 9
}