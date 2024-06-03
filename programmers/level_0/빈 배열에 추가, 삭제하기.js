// 2024.06.04
// https://school.programmers.co.kr/learn/courses/30/lessons/181860

function solution(arr, flag) {
    let X = [];
    
    flag.forEach((v, i) => {
        if(v){
            X = [...X, ...new Array(arr[i] * 2).fill(arr[i])]
        } else {
           X = X.slice(0, X.length - arr[i])
        }
    })
    
    return X;
}