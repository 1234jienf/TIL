T = int(input())

# 현재 플레이어가 각 방향을 보고 있을 떄, 좌상, 우상, 좌하, 우하 에 있는 사과를 먹기 위해 우회전을 해야 하는 횟수
turncnt = [
    # 좌상 우상 좌하 우하
    [3, 1, 3, 2],  # 상 (현재 보고 있는 방향)
    [2, 3, 1, 3],  # 하
    [1, 2, 3, 3],  # 좌
    [3, 3, 2, 1]  # 우 
]
# 현재 플레이어가 각 방향을 보고 있을 때, 좌상, 우상, 좌하, 우하에 있는 사과를 먹은 후 보게 될 방향
# 0 = 상 1 = 하 2 = 좌 3 = 우
nextdir = [
    # 좌상 우상 좌하 우하
    [2, 3, 2, 1],  # 상
    [0, 3, 2, 3],  # 하
    [0, 3, 1, 1],  # 좌
    [0, 0, 2, 1]  # 우
]

for tc in range(1, T + 1):
    N = int(input())

    map_lst = [list(map(int, input().split())) for _ in range(N)]
    apple_info = []
    for i in range(N):
        for j in range(N):
            if map_lst[i][j] != 0:
                apple_info.append([map_lst[i][j], (i, j)])
    apple_info.sort()
    check = 0
    cnt = 0
    cnt_def = 0


    def bfs(now, dir, end, cnt, cnt_def):
        if cnt_def != len(apple_info):
            ci, cj = now[0], now[1]  # 현재 내가 있는 위치
            ni, nj = end[0], end[1]  # 다음 내가 가야할 위치
            if ni > ci and nj > cj:  # 우하의 위치
                cnt += turncnt[dir][3]
                dir = nextdir[dir][3]  # 다음 내가 보게 될 방향
            if ni < ci and nj > cj:  # 우상의 위치
                cnt += turncnt[dir][1]
                dir = nextdir[dir][1]  # 다음 내가 보게 될 방향
            if ni < ci and nj < cj:  # 좌상의 위치
                cnt += turncnt[dir][0]
                dir = nextdir[dir][0]  # 다음 내가 보게 될 방향
            if ni > ci and nj < cj:  # 좌하의 위치
                cnt += turncnt[dir][2]
                dir = nextdir[dir][2]  # 다음 내가 보게 될 방향
            now = end
            if now == apple_info[-1][-1]:
                global check
                check = cnt
                return
            else:
                end = apple_info[cnt_def + 1][-1]
                cnt_def += 1
                bfs(now, dir, end, cnt, cnt_def)


    end = apple_info[0][-1]
    bfs((0, 0), 3, end, cnt, cnt_def)
    print(f'#{tc} {check}')