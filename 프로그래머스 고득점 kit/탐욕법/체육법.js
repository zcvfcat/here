/** @param {number} n @param {number[]} lost @param {number[]} reserve */
function solution(n, lost, reserve) {
  const person = Array.from({ length: n + 1 }, () => 1)
  lost.forEach((n) => (person[n] -= 1))
  reserve.forEach((n) => (person[n] += 1))

  for (let i = 1; i <= n; i++) {
    if (person[i] === 2 && person[i - 1] === 0) {
      person[i - 1] += 1
      person[i] -= 1
    } else if (person[i] === 2 && person[i + 1] === 0) {
      person[i + 1] += 1
      person[i] -= 1
    }
  }
  return person.filter((p, i) => i !== 0 && p >= 1).length
}
console.log(solution(5, [2, 4], [1, 3, 5]) === 5)
console.log(solution(5, [2, 4], [3]) === 4)
console.log(solution(3, [3], [1]) === 2)
