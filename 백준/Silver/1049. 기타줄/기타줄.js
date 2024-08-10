const INPUT = require("fs")
.readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

function solution() {
  const [line, brand] = INPUT[0].split(" ").map(Number);
  const rows = INPUT.slice(1);

  let minSet = 1000;
  let minLine = 1000;

  for(let i = 0; i < brand; i++){
    const [s, l] = rows[i].split(" ").map(Number);
    if(s < minSet) minSet = s;
    if(l < minLine) minLine = l;
  }

  const max = Math.ceil(line / 6);
  const costs = [];
  let curSet = 0;
  
  while(curSet <= max){
    let curCost = 0;
    curCost += minSet * curSet;
    if(line > 6 * curSet){
      curCost += minLine * (line - 6 * curSet)
    }
    costs.push(curCost)
    curSet++;
  } 

  console.log(Math.min(...costs))
}

solution();