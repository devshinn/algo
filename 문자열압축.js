

function solution(s) {

  let outList = []
  for (let len = 1; len <= s.length / 2; len++) {
    var ss = ""
    let repeatNum = 1;
    for (let i = 0; i <= s.length - len; i += len * repeatNum) {
      repeatNum = 1;
      let word = s.substr(i, len);
      console.log(len, i)
      if (word == s.substr(i + len, len)) { //len 길이만큼 반복 여부 확인 //2번 이상 반복
        repeatNum += 1
        for (var term = i + len * 2; term <= s.length - len; term += len) { // 3번이상 반복갯수확인
          if (word == s.substr(term, len)) {
            repeatNum += 1
          } else break; //반복이 더이상 없을시 
        }
      }
      len * repeatNum <= 2 ? repeatNum = 1 : null

      ss += (len * repeatNum > 2) && (repeatNum > 1) ? repeatNum + word : word



    }
    outList.push(ss)
  }
  return outList
  // return Math.min(...outList);
}

const s = "xababcdcdababcdcd"

console.log(solution(s))