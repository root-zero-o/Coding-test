// 2024.06.09
// https://school.programmers.co.kr/learn/courses/30/lessons/181855

function solution(strArr) {
    let obj = {};
    
    strArr.forEach((v) => {
        const length = v.length;
        if(typeof obj[length] === 'number'){
            obj[length] ++
        } else {
            obj[length] = 1
        }
    })
    
    return Object.values(obj).sort((a, b) => b - a)[0]
}