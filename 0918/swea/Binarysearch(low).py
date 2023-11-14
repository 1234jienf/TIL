n = int(input())

arr = tuple(sorted(list(map(int,input().split()))))


k = int(input())
find = tuple(map(int,input().split()))

def binarySearch(target):
    start, end = 0, n # 시작점 끝점 초기화
    while start <= end :
        mid = (start + end) // 2
        # 1. 왼쪽 부분 탐색, 중간점의 값이 찾고자 하는 값보다 큰 경우
        if arr[mid] > target:
            end = mid - 1
        # 2. 오른쪽 부분 탐색 , 중간점의 값이 찾고자 하는 값보다 작은 경우
        if arr[mid] < target:
            start = mid + 1
        # 3. 탐색 종료, 중간점의 값이 찾고자 하는 값과 같은 경우
        elif arr[mid] == target:
            return True
        
    return False # 탐색이 종료 됐는데도 찾지 못한 경우

for b in find:
    if binarySearch(b):
        print('0', end = '')
    else:
        print('X', end = '')

