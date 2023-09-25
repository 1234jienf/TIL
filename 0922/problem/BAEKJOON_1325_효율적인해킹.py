N, M = map(int,input().split())

arr = [ ([0] * (N+1)) for _ in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    arr[a][b] = 1

    