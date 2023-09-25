# 내 풀이

T = int(input())

for tc in range(1,T+1):
    N, B = map(int,input().split())

    S = list(map(int,input().split()))
    result = []
    
    def height(n,sum):
        if sum >= B:
            result.append(sum)
            return
        if n == N:
            return
        
        # n을 통해서 인덱스 값-->으로 해서 포문 안씀
        height(n+1, sum + S[n])
        
        height(n+1,sum)

    height(0,0)
    result.sort()
    print(f'#{tc} {result[0] - B}')



# 문풀 - 강사님 풀이

T = int(input())


def recur(level, acc_height):
    global ans
    # 가지 치기
    # 현재까지 탑이 선반 높이를 넘어 간다면,
    # 앞으로 더 볼 필요가 없다.
    if acc_height >= B:
        ans = min(ans,acc_height)
        return
    # 기저 조건
    if level == N:
        return
    
    # 해당 점원을 탑에 쓸 경우
    recur(level + 1, acc_height + S[level])
    # 안 쓸 경우
    recur(level + 1, acc_height)
    # 다음 재귀 함수 호출
    # 돌아왔을 때


for tc in range(1,T+1):
    N, B = map(int,input().split())

    S = list(map(int,input().split()))
    # 1. 백트래킹
    ans = int(1e9)
    recur(0,0)
    print(f'#{tc} {ans - B}')
