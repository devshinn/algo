from collections import deque


# def gcd(a, b):
#     print(a, b)
#     if a % b == 0:
#         print('is ok:', a, b)

#         return b
#     else:
#         gcd(b, a % b)
#         print('is end: ', a, b)


# print(gcd(192, 162))


# def bfs(graph, start, visited):

#     queue = deque([start])

#     visited[start] = True

#     while queue:
#         v = queue.popleft()

#         print(v, end='=>')

#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
# graph = []
# n, m = 5, 5


# def dfs(x, y):
#     if(x <= -1 or x >= n or y <= -1 or y >= m):
#         return False
#     if(graph[x][y] == 0):
#         graph[x][y] == 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True

arr = [1, 3, 5, 7, 8, 945, 3, 1, 13, 0, 56, 236, 78978, 345, 78, 99]
#선택정렬
# for i in range(len(arr)):
#     min_index = i

#     for j in range(i+1, len(arr)):
#         if(arr[min_index] > arr[j]):
#             min_index = j

#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)

# 삽입정령
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if(arr[j] > arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
print(arr)
