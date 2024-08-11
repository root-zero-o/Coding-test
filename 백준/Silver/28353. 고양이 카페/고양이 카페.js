const INPUT = require("fs")
.readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const [total, max] = INPUT[0].split(" ").map(Number);
  const cats = INPUT[1].split(" ").map(Number).sort((a,b) => b - a);

  // 투 포인터
  let left = 0;
  let right = total - 1;
  let happy = 0;
  
  while(left < right){
    if(cats[left] + cats[right] > max){
      left++;
    } else {
      happy++;
      left++;
      right--;
    }
  }
  console.log(happy);
}

solution();