let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let answer = 0;
let flag = false;

while(n >= 0){
    // n이 0이 되었거나 5로 나누어 떨어지는 값인 경우
    if(n === 0 || n % 5 === 0){
        answer += parseInt(n / 5);
        console.log(answer)
        flag = true;
        break;
    }
    n -= 3;
    answer += 1;
}

if(!flag){
    console.log(-1)
}