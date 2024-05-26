// 2024.05.26.
// https://school.programmers.co.kr/learn/courses/30/lessons/181913

function solution(my_string, queries) {
    let answer = '';
    let arr = my_string.split('');
    queries.forEach((query) => {
        const [s, e] = query;
        arr = [...arr.slice(0, s), ...arr.slice(s, e+1).reverse(), ...arr.slice(e+1, arr.length)];
    })
    
    answer = arr.join('');
    return answer;
}