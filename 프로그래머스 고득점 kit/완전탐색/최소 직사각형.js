/** @param {[number,number][]} sizes*/
function solution(sizes) {
  let maxHeight = -Number.MAX_SAFE_INTEGER;
  let maxWidth = -Number.MAX_SAFE_INTEGER;

  sizes.forEach(([w, h]) => {
    const [width, heigth] = w > h ? [w, h] : [h, w];
    if (heigth > maxHeight) maxHeight = heigth;
    if (width > maxWidth) maxWidth = width;
  });

  return maxHeight * maxWidth;
}

console.log(
  solution([
    [60, 50],
    [30, 70],
    [60, 30],
    [80, 40],
  ]) === 4000
);
console.log(
  solution([
    [10, 7],
    [12, 3],
    [8, 15],
    [14, 7],
    [5, 15],
  ]) === 120
);
console.log(
  solution([
    [14, 4],
    [19, 6],
    [6, 16],
    [18, 7],
    [7, 11],
  ]) === 133
);
