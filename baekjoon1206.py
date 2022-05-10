import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    y, x = map(int, input().split())
    graph[y][x] = graph[x][y] = 1

visited = [0]*(N+1)

# print(*result)


def dfs(v):
    visited[v] = 1

    print(v, end=' ')
    for i in range(1, N+1):
        if(visited[i] == 0 and graph[v][i] == 1):
            dfs(i)


def bfs(v):
    q = []
    q.append(v)
    # visited.append(v)
    visited[v] = 0
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):

            if(visited[i] == 1 and graph[v][i] == 1):
                q.append(i)
                visited[i] = 0


dfs(V)
print()
bfs(V)
