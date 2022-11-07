function solution(participant, completion) {
  const hashedParticipant = {}

  participant.forEach((p) => {
    if (!!hashedParticipant[p]) {
      hashedParticipant[p] += 1
    } else {
      hashedParticipant[p] = 1
    }
  })

  for (const c of completion) {
    hashedParticipant[c] -= 1
    if (hashedParticipant[c] === 0) {
      delete hashedParticipant[c]
    }
  }

  return Object.entries(hashedParticipant)[0][0]
}

console.log(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']) === 'leo')
console.log(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']) === 'vinko')
console.log(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']) === 'mislav')
