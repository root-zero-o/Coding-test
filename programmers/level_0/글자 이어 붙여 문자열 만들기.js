// 2024.05.26.
// https://school.programmers.co.kr/learn/courses/30/lessons/181915

function solution(my_string, index_list) {
    let answer = '';
    
    index_list.forEach((index) => {
        answer += my_string[index]
    })
    
    return answer;
}