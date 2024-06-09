// 2024.06.09
// https://school.programmers.co.kr/learn/courses/30/lessons/181854

function solution(arr, n) {
    if(arr.length % 2 === 1){
        return arr.map((v, i) => {
            if(i % 2 === 0){
                return v + n
            } else return v
        })
    } else {
        return arr.map((v, i) => {
            if(i % 2 === 1){
                return v + n
            } else return v
        })
    }
}