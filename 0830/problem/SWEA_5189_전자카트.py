T = int(input())

for tc in range(1,T+1):
    N = int(input())
    map_lst = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]

    ans = 1e9
    def dfs(n,res,now):
        global ans
        if n == N :
            # 마지막에 1번으로 돌아오기
            res += map_lst[now][0]
            if ans > res:
                ans = res
                return
        if res > ans:
            return
        for j in range(1,N):
            if now != j and not visited[j]:
                visited[j] = 1
                dfs(n+1,res + map_lst[now][j],j)
                visited[j] = 0

    dfs(1,0,0)
    print(f'#{tc} {ans}')


'''
첫번째 풀이 -> 마지막에 1로 돌아오는거 고려를 못함
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    map_lst = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N+1)]

    ans = 1e9
    def dfs(n,res):
        global ans
        if n == N:
            ans = min(ans,res)
            return
        for j in range(N):
            if n != j and not visited[j]:
                visited[j] = 1
                dfs(n+1,res + map_lst[n][j])
                visited[j] = 0

    dfs(0,0)
    print(f'#{tc} {ans}')

''' 