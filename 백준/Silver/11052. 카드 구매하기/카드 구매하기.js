const INPUT = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  // .map(Number);

function solution() {
  N = Number(INPUT[0])
  cards = [0, ...INPUT[1].split(' ').map(Number)]
  dp = new Array(N+1).fill(0)

  for(let i = 1; i < N+1; i++){
    for(let j = 1; j <i+1; j++){
      dp[i] = Math.max(dp[i], dp[i-j] + cards[j])
    }
  }

  console.log(dp[N])
}

solution();