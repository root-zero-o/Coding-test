// 2024.05.26.
// https://school.programmers.co.kr/learn/courses/30/lessons/181905

function solution(my_string, s, e) {
    let arr = my_string.split('');
    
    arr = [...arr.slice(0, s), ...arr.slice(s, e+1).reverse(), ...arr.slice(e+1, arr.length + 1)];
    
    return arr.join('')
}

