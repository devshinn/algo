import sys
input = sys.stdin.readline

graph = []
for i in range(10):
    graph.append(list(map(int, input().split())))

x = 1
y = 1

while True:
    if graph[y][x] == 2 or x == y == 8:
        graph[y][x] = 9
        break
    if graph[y][x] == 0:
        graph[y][x] = 9

    if graph[y][x+1] != 1:
        x += 1
        continue

    elif graph[y+1][x] != 1:
        y += 1
        continue

for row in graph:
    for v in row:
        print(v, end=" ")
    print("")
