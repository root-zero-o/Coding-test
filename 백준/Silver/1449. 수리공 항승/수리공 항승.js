const INPUT = require("fs")
.readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

function solution() {
  const [N, L] = INPUT[0].split(" ").map(Number);
  const holes = INPUT[1].split(" ").map(Number).sort((a, b) => a - b);

  let tapeStart = 0;
  let tapeEnd = 0;
  let count = 0;

  for(let i = 0; i < N; i++){
    let start = holes[i] - 0.5;
    let end = holes[i] + 0.5;

    if(tapeStart <= start && tapeEnd >= end){
      continue;
    } else {
      count++;
      tapeStart = start;
      tapeEnd = start + L;
    }
  }

  console.log(count)
}

solution();