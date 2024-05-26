// 2024.05.26.
// https://school.programmers.co.kr/learn/courses/30/lessons/181911

function solution(my_strings, parts) {
    let answer = '';
    
    parts.forEach((part,i) => {
        const [s, e] = part;
        answer += my_strings[i].split('').slice(s, e+1).join('');
    })
    
    return answer;
}