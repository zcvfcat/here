function solution(numbers, target) {
  let ans = 0

  /** @param {number[]} currNumbers */
  function dfs(currNumbers, acc) {
    if (currNumbers.length === 0) {
      if (acc === target) ans += 1
      return
    }

    const [curr, ...nextNumbers] = currNumbers
    dfs(nextNumbers, acc + curr)
    dfs(nextNumbers, acc - curr)
  }
  dfs(numbers, 0)

  return ans
}

console.log(solution([1, 1, 1, 1, 1], 3) === 5)
console.log(solution([4, 1, 2, 1], 4) === 2)
