/** @param {number} n @param {[number,number][]} edge*/
function solution(n, edge) {
  const g = Array.from({ length: n + 1 }, () => new Set([]))
  const visited = Array.from({ length: n + 1 }, () => 0)
  visited[1] = 1

  edge.forEach(([v, e]) => {
    g[v].add(e)
    g[e].add(v)
  })

  const q = [1]

  while (q.length > 0) {
    const curr = q.shift()
    for (const next of g[curr]) {
      if (!visited[next]) {
        visited[next] = visited[curr] + 1
        q.unshift(next)
      }
    }
  }

  const maximum = Math.max(...visited)
  return visited.filter((e) => e === maximum).length
}

console.log(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ]) === 3
)
