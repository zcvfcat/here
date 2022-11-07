/** @param {number} N @param {number} number */
function solution(N, number) {
  let ministCnt = Number.MAX_SAFE_INTEGER

  /** @param {number} curr @param {number} cnt */
  function dfs(curr, cnt) {
    if (curr === number) ministCnt = Math.min(cnt, ministCnt)
    if (cnt === 8) return
    console.log(curr)

    dfs(Number(String(curr) + String(N)), cnt + 1)
    dfs(curr + N, cnt + 1)
    dfs(curr - N, cnt + 1)
    dfs(curr * N, cnt + 1)
    dfs(Math.floor(curr / N), cnt + 1)
  }

  dfs(N, 1)

  return ministCnt > 8 ? -1 : ministCnt
}

console.log(solution(5, 12) === 4)
console.log(solution(2, 11) === 3)
