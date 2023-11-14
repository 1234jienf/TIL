# Lab

N, M = map(int,input().split())

map_lst = [list(map(int,input().split())) for _ in range(N)]

di = [1,-1,0,0]
dj = [0,0,1,-1]
virus = []
ans = 0

cnt_virus = 0
cnt_safe = 0

for i in range(N):
        for j in range(M):
            if map_lst[i][j] == 2:
                virus.append((i,j))
                cnt_virus += 1
            elif map_lst[i][j] == 0:
                cnt_safe += 1

def cal(tlst):
    new_virus = 0
    global virus
    while virus:
        now = virus.pop
        for k in range(4):
            ni,nj = now[0] + di[k], now[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and tlst[ni][nj] == 0:
                new_virus += 1
    return new_virus

            
            

def dfs(n,tlst):
    global cnt_safe
    if n == 3:
        ans = max(cnt_safe - cal(tlst),ans)
        return ans
    for i in range(N):
        for j in range(M):
            if map_lst[i][j] == 0:
                map_lst[i][j] = 1
                dfs(n+1,map_lst)
                map_lst[i][j] = 0

print(ans)