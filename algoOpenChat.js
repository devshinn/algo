function solution(record) {

  var answer = [];
  const user_list = {};
  for (let v of record) {
    const user = v.split(" ")
    if (user[0] === "Enter" || user[0] === "Change") {
      user_list[user[1]] = user[2]
    }
  }

  for (let v of record) {
    const user = v.split(" ")
    if (user[0] === "Enter") {
      answer.push(`${user_list[user[1]]}님이 들어왔습니다.`)
    }

    if (user[0] === "Leave") {
      answer.push(`${user_list[user[1]]}님이 나갔습니다.`)
    }
  }
  return answer;

}

const record = [
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan"]

console.log(solution(record))

//type: Enter, Leave, Change
//output: Enter, Leave

//필요한 것 : {users_id: nickname}

// 입장 퇴장시로그들만 리턴