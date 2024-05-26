// 2024.05.26.
// https://school.programmers.co.kr/learn/courses/30/lessons/181908

function solution(my_string, is_suffix) {
    
    const length = my_string.length;
    const suffixs = [];
    
    new Array(length).fill(undefined).forEach((v, i) => {
        suffixs.push(my_string.slice(i, length + 1));
    });
    
    return suffixs.indexOf(is_suffix) !== -1 ? 1 : 0
}

// const solution = (str, suff) => str.endsWith(suff) ? 1 : 0
// 이런게 있네..