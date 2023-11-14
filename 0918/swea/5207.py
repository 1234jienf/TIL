T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = tuple(sorted(list(map(int,input().split()))))
    find = tuple(list(map(int,input().split())))
    cnt = 0

    def binarySearch(target):
        start,end = 0,N-1
        while start <= end :
            mid = (start + end) // 2
            if arr[mid] > target:
                end = mid - 1
            if arr[mid] < target:
                start = mid + 1
            elif arr[mid] == target:
                return True
        return False
    
    for check in find:
        if binarySearch(check):
            cnt += 1
    print(f'#{tc} {cnt}')

