function solution(progresses, speeds) {
  let answer = [];

  let day_left = progresses.map((per, i) => Math.ceil((100 - per) / speeds[i]))
  let dev_n = 1;
  let day = [...day_left];
  while (day_left.length > 0) {
    console.log("left", day_left, answer)
    for (let i = 1; i < day_left.length; i++) {
      console.log("for: ", day_left[0], day_left[i])

      if (day_left[0] >= day_left[i]) {
        dev_n++;
        day.shift();
      } else break

    }
    answer.push(dev_n); // 위에서는 [0]을 제외한 만족 조건을 삭제 
    dev_n = 1; //기능갯수 초기화
    day.shift()
    day_left = [...day] //복사
  } return answer;
}

const progresses = [95, 90, 99, 99, 80, 99]
const speeds = [1, 1, 1, 1, 1, 1]
console.log(solution(progresses, speeds))