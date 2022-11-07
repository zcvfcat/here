/** @param {number[]} array @param {number[][]} commands*/
function solution(array, commands) {
  return commands.map(([i, j, k]) => {
    const sortedArray = array.slice(i - 1, j).sort((curr, next) => curr - next)
    return sortedArray[k - 1]
  })
}
