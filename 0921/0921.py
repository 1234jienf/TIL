# MST 알고리즘

import heapq

def prim(start):
    heap = []
    # MST 에 포함되었는지 여부
    MST = [0] * V

    # 가중치, 정점 정보
    heapq.heappush(heap,(0, start))
    # 누적합 저장
    sum_weight = 0

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 갈 수 있는 노드라면 pass
        if MST[v]:
            continue
        # 방문 체크
        MST[v] = 1

        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))
    
    return sum_weight



V, E = map(int,input().split())

graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f,t,w = map(int,input().split())
    graph[f][t] = w
    graph[t][f] = w

result = prim(0)
print(f'최소 비용 = {result}')

# KRUSKAL 알고리즘


# 모든 간선들 중 비용이 가장 적은 걸 우선으로 고르자
V, E = map(int,input().split())
edge = []
for _ in range(E):
    f,t,w = map(int,input().split())
    edge.append([f,t,w])

# w를 기준으로 정렬
edge.sort(key=lambda x:x[2])

# 사이클 발생 여부를 union find로 해결
parents = [i for i in range(V)]

def find_set(x):
    if parents[x] == x:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        print('사이클 발생')
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

cnt = 0
sum_weight = 0
for f,t,w in edge:
    # 사이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        union(f,t)
        # MST 구성이 끝나면
        if cnt == V:
            break
print(f'최소 비용 = {sum_weight}')


# 다익스트라 알고리즘

# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자
import heapq


# 입력
n, m = map(int,input().split())
# 인접리스트
graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int,input().split())
    graph[f].append([t,w])



# 1. 누적 거리를 계속 저장
INF = int(1e9)  # 최대값으로 1억 
distance = [INF] * n

start = 0

def dijkstra(start):
    # 2. 우선 순위 큐
    pq = []
    heapq.heappush(pq,(0,start))
    distance[start] = 0

    while pq:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 +  누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node 로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존 보다 크네?
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost,next_node))

dijkstra(0)
print(distance)