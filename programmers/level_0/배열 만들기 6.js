// 2024.06.04
// https://school.programmers.co.kr/learn/courses/30/lessons/181859

function solution(arr) {
    const stk = [];
     
     let i = 0;
     while(i < arr.length){
         if(stk.length === 0) {
             stk.push(arr[i]);
             i++
         }
         else {
             if(stk[stk.length - 1] === arr[i]){
                 stk.pop();
                 i++
             } else{
                 stk.push(arr[i]);
                 i++
             }
         }
     }
     
     return stk.length > 0 ? stk : [-1]
 }