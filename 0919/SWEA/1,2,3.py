N = int(input())

cnt = 0

def func(num):
    global cnt
    if num == N:
        cnt += 1
        return
    if num > N: # num 이 N을 넘어가면 가망이 없다 . # 백트래킹
        return
    # 재귀 구성 : 1,2,3을 더해서 다음 조합으로 넘어가기
    for i in range(1,4):
        func(num + i)

func(0)
print(cnt)