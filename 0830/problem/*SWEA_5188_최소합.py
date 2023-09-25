# T = int(input())


# di = [0,0,1,-1]
# dj = [1,-1,0,0]

# for tc in range(1,T+1):
#     N = int(input())

#     map_lst = [list(map(int,input().split())) for _ in range(N)]
#     result = []
#     def search(x,y,sum):
#         global result
#         if x == N-1 and y == N-1:
#             result.append(sum)
#             return
#         for k in range(4):
#             ni,nj = x + di[k] , y + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 search(ni,nj,sum + map_lst[ni][nj])
    
#     search(0,0,0)
#     result.sort()
#     print(f'{tc} {result[0]}')

T = int(input())

dx = [0,1]
dy = [1,0]

def dfs(x,y):
    global res, tmp
    if res < tmp: # 현재 결과값보다 크면 함수가 끝나도록 -> 시간초과 때문에
        return
    if x == N-1 and y == N-1:
        if res > tmp:
            res = tmp
            return
    for j in range(2):
        nx = x + dx[j]
        ny = y + dy[j]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if (nx,ny) not in visited:
            visited.append((nx,ny)) # visited 함수에 좌표 업로드
            tmp += a[nx][ny]
            dfs(nx,ny)
            tmp -= a[nx][ny] # 원상 복구 --> 이거 잘하자
            visited.remove((nx,ny)) # 좌표 삭제
 

for tc in range(1,T+1):
    N = int(input())
    a = [list(map(int,input().split())) for _ in range(N)]
    # visited 배열 체크
    visited = []
    # res 일단 3000으로 큰 수 설정
    res = 3000
    tmp = a[0][0]
    # 시작 좌표
    dfs(0,0)
    print(f'#{tc} {res}')