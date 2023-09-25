# 유니온 파인드 문제라캄..

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
        parent[pb] = parent[pa] # b의 루트를 a의 루트로 변경
    else:
        parent[pa] = parent[pb]


T = int(input())

for tc in range(1,T+1):
    V, E = map(int,input().split())
    parent = [i for i in range(V)]
    for _ in range(E):
        A, B, W = map(int,input().split())
        union(A,B)
        