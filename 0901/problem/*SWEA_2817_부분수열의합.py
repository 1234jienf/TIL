#A1,A2,...,AN N개의 자연수 -> 최소 1개 이상의 수를 택해 합이 K가 되는 경우의 수

# 1번 풀이
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))

    cnt = 0         # 합이 K가 되는 경우의 수
    for i in range(1<<N):       # 부분 집합을 표시하는 i
        s = 0       # 부분집합의 합
        for j in range(N):      # j번 비트
            if i & (1<<j):      # i의 j번 비트 검사
                s += arr[j]     # 0이 아니면 j번 원소가 부분집합에 포함됨
        if s == K:
            cnt += 1
    print(f'{tc} {cnt}')


# 2번 풀이
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0

    def f(i,N,s,K):
        global cnt
        if i == N:
            if s == K:
                cnt += 1
        else:
            f(i+1,N,s+arr[i],K)
            f(i+1,N,s,K)

    f(0,N,0,K)
    print(f'#{tc} {cnt}')
