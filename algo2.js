
function solution(id_list, report, k) {
  var answer = new Array(id_list.length).fill(0);

  const arr = []
  id_list.map((user) => arr.push({
    user_id: user, report_users: [],
    send_check: false
  }))

  for (pair_user of report) {
    pair = pair_user.split(" ")
    arr.map((v, i) => {
      if (v.user_id == pair[1]) {
        arr[i].report_users.push(pair[0])
      }
    })
  }

  arr.map((v) => {
    const users = [...new Set(v.report_users)]
    users.length >= k
      &&
      id_list.map((v, i) => users.includes(v) ? answer[i] += 1 : null)
  })

  return answer;
}

const id_list = ["muzi", "frodo", "apeach", "neo"];
const report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
const k = 2

const result = solution(id_list, report, k)
console.log(result)