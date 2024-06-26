var fairCandySwap = function (aliceSizes, bobSizes) {
  const aliceTotal = aliceSizes.reduce((acc, cur) => acc + cur, 0);
  const bobTotal = bobSizes.reduce((acc, cur) => acc + cur, 0);

  const total = (aliceTotal + bobTotal) / 2;

  let a = 0;
  let b = 0;

  for (let i = 0; i < aliceSizes.length; i++) {
    let diff = total - aliceSizes[i];

    if (diff) {
      if (bobSizes.indexOf(diff) !== -1) {
        a = aliceSizes[i];
        b = bobSizes[aliceSizes.indexOf(total - diff)];
        break;
      }
    }
  }

  return [a, b];
};
