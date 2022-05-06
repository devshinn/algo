function solution(w, m, k) {
  let answer = 0
  let check = true
  while (check) {
    check = w > 2 === m > 1
    w -= 2; m -= 1;
    if (w + m > k) {
      answer += 1
    } else return answer
  }
  return answer
}
console.log(solution(100, 1, 1))
