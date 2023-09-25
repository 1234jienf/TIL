# 분할 함수
def divide(arr):
    if len(arr) <= 1: # 리스트의 길이가 1이하이면 그대로 반환
        return arr

    middle = len(arr) // 2
    left = divide(arr[:middle])
    right = divide(arr[middle:])
    return merge(left,right) # 나눈 두 부분을 병합

# 병합 함수
def merge(left,right):
    global ans
    if right[-1] < left[-1]:
        ans += 1

    result = []
    len_l = len(left)
    len_r = len(right)
    l = r = 0
    while l < len_l or r < len_r:
        # 1. 왼쪽과 오른쪽 리스트 모두 남아있는 경우
        if l < len_l and r < len_r:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r]) # 오른쪽의 원소를 result 에 추가
                r += 1

        # 2. 오른쪽 리스트만 남아있는 경우
        elif l < len_l:
            result.append(left[l])
            l += 1
        # 3. 왼쪽 리스트만 남아있는 경우
        elif r < len_r:
            result.append(right[r])
            r += 1
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    result = divide(arr)
    print(f'#{tc} {result[N//2]} {ans}')