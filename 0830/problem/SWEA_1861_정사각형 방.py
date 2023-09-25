T = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for tc in range(1,T+1):
    N = int(input())

    room_map = [list(map(int,input().split())) for _ in range(N)]

    result = 0
    def room_search(cx,cy,cnt):
        if cnt >= result and :
        now = room_map[cx][cy]
        for k in range(4):
            ny,nx = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and room_map[ny][nx] == now+1:
                room_search


    for i in range(N):
        room_search