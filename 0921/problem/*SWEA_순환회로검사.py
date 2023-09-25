# 해당 노드의 최상위 노드를 찾는 함수(부모 노드를 찾는 함수)
def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

# 두 노드를 연결하는(합치는) 함수
def union(a,b):
    pa = find(a)
    pb = find(b)
    if pa != pb: # 두 노드의 루트가 다르다면
        parent[pb] = pa # b의 루트를 a의 루트로 변경

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
parent = [i for i in range(N+1)]
for i in range(N):
    for j in range(i+1,N):
        # 두 노드 (i,j)가 연결되어 있지 않으면 continue
        if arr[i][j] == 0:
            continue
        # 만약 두 노드의 최상위 부모(루트)가 같다면
        if find(i) == find(j):
            print('WARNING')
            exit()

        # 두 노드 연결
        union(i,j)
print('STABLE')