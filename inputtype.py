import queue
import sys

# 공백으로 구분된 2개 숫자 입력 받기
N, M = map(int,sys.stdin.readline().split())

# 2차원 리스트 입력 받기
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
stirn2 = [list(sys.stdin.readline().split()) for _ in range(N)]

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()

# stack 출구 한개
array = []
array.append()
array.pop()

# queue
from collections import deque
queue = deque()

queue.append()
queue.popleft() #왼쪽부터 삭제