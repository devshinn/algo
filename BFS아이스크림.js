const map = [
  [1, 1, 0, 1, 1],
  [0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
]
const m = 6, n = 5;

const chk = create2DArray(m, n) //5 x 4

function create2DArray(rows, columns) {
  var arr = new Array(rows).fill(false);
  for (var i = 0; i < rows; i++) {
    arr[i] = new Array(columns).fill(false);
  }
  return arr;
}

function solution() {
  var count = 0, max = 0;
  for (var j = 0; j < m; j++) {
    for (var i = 0; i < n; i++) {
      if (map[j][i] && !chk[j][i]) {
        chk[j][i] = true
        //전체그림 갯수 +
        // BFS > 그림 크기를 구해준다, 최댓 값 갱신
        count++
        console.log("max: ", max)
        max = Math.max(max, bfs(i, j));
      }
    }
  }
  console.log(count, max);
}
function bfs(x, y) {
  const dy = [0, 1, 0, -1], dx = [1, 0, -1, 0]
  var q = [[y, x]]
  var rs = 1
  while (q.length > 0) {
    console.log('rs   ', q)
    var [ey, ex] = q.shift()
    for (var i = 0; i < 4; i++) {
      var ny = ey + dy[i]
      var nx = ex + dx[i]
      if (0 <= ny && ny < m && 0 <= nx && nx < n) {
        if (map[ny][nx] && !chk[ny][nx]) {
          chk[ny][nx] = true
          q.push([ny, nx])
          rs += 1
        }
      }
    }
  }
  return rs
}
solution()