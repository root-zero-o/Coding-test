// 2024.06.09
// https://school.programmers.co.kr/learn/courses/30/lessons/181856

function solution(arr1, arr2) {
    const l1 = arr1.length;
    const l2 = arr2.length;
    const total1 = arr1.reduce((acc, cur) => acc + cur, 0);
    const total2 = arr2.reduce((acc, cur) => acc + cur, 0);
    
    if(l1 !== l2){
        if(l1 > l2) return 1;
        if(l2 > l1) return -1;
    } else {
        if(total1 > total2) return 1;
        if(total2 > total1) return -1;
        else return 0
    }
}