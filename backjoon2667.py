
result = []
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [1, 0, 0, -1]
dy = [0, -1, 1,  0]


def bfs(x, y):
    q = [[x, y]]
    graph[y][x] = 0
    count = 1
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
                count += 1
                graph[ny][nx] = 0
                q.append([nx, ny])
    return count


for i in range(n):
    for j in range(n):
        if graph[j][i] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
