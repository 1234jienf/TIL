N, M = map(int,input().split())

map_lst = [list(map(int,input().split())) for _ in range(N)]


home = []
chicken = []
for i in range(N):
    for j in range(N):
        if map_lst[i][j] == 1:
            home.append((i,j))
        elif map_lst[i][j] == 2:
            chicken.append((i,j))

cnt = len(chicken)

def cal(tlst):
    sm = 0
    for hi,hj in home:
        mn = 2*N
        for ci,cj in chicken:
            mn = min(mn, abs(hi-ci)+abs(hj-cj))
        sm += mn
    return sm

def dfs(n,tlst):
    if n == cnt:
        if len(tlst) == M:
            ans = min(ans,cal(tlst))
        return
    
    dfs(n+1, tlst+[chicken[n]]) # 유지하는 경우
    dfs(n+1, tlst) # 폐업하는 경우

ans = 2*N*2*N
dfs(0,[])
print(ans)