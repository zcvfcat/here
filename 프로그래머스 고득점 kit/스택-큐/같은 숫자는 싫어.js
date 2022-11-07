function solution(arr) {
  const reArranged = [arr[0]]
  let prev = arr[0]

  for (let i = 1; i < arr.length; i++) {
    const v = arr[i]
    if (prev !== v) {
      reArranged.push(v)
      prev = v
    }
  }

  return reArranged
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]) === [1, 3, 0, 1])
console.log(solution([4, 4, 4, 3, 3]) === [4, 3])
