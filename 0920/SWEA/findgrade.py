# N, M, X = map(int,input().split())

# grade_lst = [[0] * (N+1) for _ in range(N+1)]

# for i in range(M):
#     x,y = map(int,input().split())
#     grade_lst[x][y] = 1

# result = []

# visited = []

# stack = []
# stack.append(x)
# while stack:
#     now = stack.pop()
#     for i in range(1,N+1):
#         if grade_lst[i][x] == 1:
#             result.ap


# 전체 학생 수, 질문 수 , 등수 알고 싶은 학생

n, m , target = map(int,input().split())

upv = [[] for _ in range(n+1)] # 어떤 학생이 다른 학생보다 잘했는지
downv = [[] for _ in range(n+1)] # 어떤 학생 보다 더 잘한 학생

# up : target 보다 못한 학생수, down : target 보다 잘한 학생수
up = 1
down = 1

upused = [False] * (n+1)
downused = [False] * (n+1)

# target 보다 못한 학생들을 탐색하는 dfs 함수
def updfs(node):
    global up
    for next_node in upv[node]: # node 보다 못한 학생들 순회
        if not upused[next_node]: # 아직 방문하지 않았다면
            up += 1 # 학생 수 카운트
            upused[next_node] = True # 방문 표시
            updfs(next_node)
def downdfs(node):
    global down
    for next_node in downv[node]:
        if not downused[next_node]:
            down += 1
            downused[next_node] = True
            downdfs(next_node)

for _ in range(m):
    a, b = map(int,input().split())
    upv[b].append(a) # b보다 a가 잘했다는 정보 저장
    downv[a].append(b) # a보다 b가 잘했다는 정보 저장

updfs(target)
downdfs(target)

print(up)
print(n - down + 1)