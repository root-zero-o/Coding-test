const INPUT = require("fs").readFileSync("/dev/stdin").toString().trim();

function solution() {
  const S = INPUT;

  if (S.indexOf("0") === -1 || S.indexOf("1") === -1) {
    console.log(0);
    return;
  }

  let cnt0 = 0;
  let cnt1 = 0;

  for (let i = 0; i < S.length; i++) {
    if (S[i] === "0") {
      if (S[i + 1] === "0") {
        continue;
      } else {
        cnt0++;
      }
    } else {
      if (S[i + 1] === "1") {
        continue;
      } else {
        cnt1++;
      }
    }
  }

  console.log(Math.min(cnt0, cnt1));
}

solution();