function solution(lines) {
  let answer = [];
  let new_lines = [];
  lines.forEach(line => {
    const [date, hour, taken] = line.split(" ");
    const start = new Date(date + " " + hour).getTime();
    const time = taken.replace("s", "") * 1000 - 1;
    new_lines.push([start, time])
  })

  var start_index = 0;
  for (var i = start_index; i < lines.length; i++) {
    let proccess = 1;
    for (let index = i + 1; index < new_lines.length; index++) {
      start_index = index;

      let start = new_lines[index][0] - new_lines[index][1];
      if (start - new_lines[i][0] < 1000) {
        proccess += 1
      } else {

        break
      };
    }
    answer.push(proccess);
  }
  return Math.max(...answer)
}