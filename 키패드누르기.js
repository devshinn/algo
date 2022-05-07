const key = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
["*", 0, "#"]]
const direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

function solution(numbers, hand) {
  var answer = ""

  var l_bef = "*"
  var r_bef = "#"

  for (var num of numbers) {
    if ([1, 4, 7].includes(num)) {
      answer += "L"
      l_bef = num

    } else if ([3, 6, 9].includes(num)) {
      answer += "R"
      r_bef = num

    } else {
      var l = position(l_bef, num)
      var r = position(r_bef, num)
      if (l === r) {

        hand === "right" ? (answer += "R", r_bef = num) : (answer += "L", l_bef = num)
      } else {
        r ? (answer += "R", r_bef = num) : (answer += "L", l_bef = num)
      }
    }
  }
  return answer
}

function position(befNum, num) {
  var x = null
  var y = null

  for (var j = 0; j < 4; j++) {
    const i = key[j].indexOf(befNum)
    if (i !== -1) {
      // num == 8 && console.log('팔일때: ', i, j)
      return dirCheck(i, j, num)

    }
  }

}

function dirCheck(i, j, num) {
  var value = false
  for (dir of direction) {
    var x = dir[0] + i; var y = dir[1] + j
    if (x >= 0 && y >= 0 && x < 3 && y < 4 && key[y][x] === num) {
      return [x, y]
    }
  }
  return value
}

function pointLength(a,b){
  return Math.sqrt(
    Math.pow(Math.abs(a[0]) - Math.abs(b[0]),2) + Math.pow(Math.abs(a[1]) - Math.abs(b[1]),2)
  )
}

const numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
const hand = "left"

console.log(solution(numbers, hand))