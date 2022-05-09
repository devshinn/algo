function solution(board, moves) {
  var answer = 0;
  var cart = [];


  for (let x of moves) {
    var item = pick(x)
    // console.log(cart, item)

    if (item != 0) {
      cart.unshift(item);
      if (cart[0] == cart[1]) {
        answer += 2
        cart.shift()
        cart.shift()
      }
    }
  }


  function pick(x) {
    var value = 0
    for (let j = 0; j < board.length; j++) {
      if (board[j][x - 1]) {
        value = board[j][x - 1];
        board[j][x - 1] = 0;
        // console.log(value, board[j][x - 1]);
        return value
      }
    }
    return 0;
  }

  return answer;
}
const board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1]]
const moves = [1, 5, 3, 5, 1, 2, 1, 4]
console.log(solution(board, moves))
// board[3][0] = true
// console.log(board)
