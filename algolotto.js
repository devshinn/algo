
function solution(w, h) {
  var answer = 1;
  const total = w * h;
  const w_div = []; const h_div = [];

  for (var i = 1; i <= w; i++) {
    w % i === 0 && w_div.push(w / i)
  }

  for (var i = 1; i <= h; i++) {
    h % i === 0 && h_div.push(h / i)
  }

  for (num of w_div) {
    if (h_div.includes(num)) {
      answer = total - (h + w - num);
      break
    }
  }

  return answer;
}
console.log(solution(8, 12)) 