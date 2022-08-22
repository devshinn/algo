import sys

from numpy import NaN
from regex import B

# N,M = map(int, input().split())
# board = [list(input()) for _ in range(N)]
N,M = 5,5
board = [
  ['#', '#', '#', '#', '#'], 
  ['#', '.', '.', 'B', '#'], 
  ['#', '.', '#', '.', '#'], 
  ['#', 'R', 'O', '.', '#'], 
  ['#', '#', '#', '#', '#']]
result = 0
dx = [1,0, -1, 0]
dy = [0,1, 0, -1]
x= NaN; y=NaN
tyarget_x=NaN; target_y= NaN
for j in range(M): #y
  for i in range(N): #x
    if(board[j][i] =="R"):
      x,y = i,j
    if(board[j][i] == "O"):
      target_x, target_y = i,j