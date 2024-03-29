import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m, start = map(int, input().split(" "))

# 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n + 1)]

# visited = [False]*(n+1)
distance = [INF]*(n+1)

# 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split(" "))
    graph[a].append((b, c))


def dijkstra2(start):
    q = []
    heapq.heappush(q, (0, start))
    # 시작 노드에 대해서 초기화
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면

        # 가장 최던 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        print("q: ", q)
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            print('kk: ', i, graph, now)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra2(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환


# def get_smallest_node():
#     min_value = INF
#     index = 0  # 가장 최단 거리가 짧은 노드(index)
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index


# def dijkstra(start):
#     # 시작 노드에 대해서 초기화
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
#     for i in range(n-1):
#         # 현재 최단 거리가 가장 짧은 노드를 꺼내서 ,방문 처리
#         now = get_smallest_node()
#         visited[now] = True
# # 현재 노드와 연결된 다른 노드를 확인
#         for j in graph[now]:
#             cost = distance[now]+j[1]
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if(cost < distance[j[0]]):
#                 distance[j[0]] = cost


# def heapsort(iterable):
#     h = []
#     result = []
#     for v in iterable:
#         heapq.heappush(h, v)

#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))

#     return result
