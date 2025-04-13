import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    distance = [INF] * (V + 1)  
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distances = dijkstra(K)

for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])
