# 백준 회의실 배정

'''
import sys
N = int(sys.stdin.readline().rstrip())

st_end = []

for i in range(N):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    dis = e - s
    st_end.append((s,e))

st_end.sort(key= lambda x: (x[1],x[0]))

result = 1
start = st_end[0]
for i in range(1,N):
    if st_end[i][0] >= start[1]:
        start = st_end[i]
        result += 1

print(result)

'''


N = int(input())
conf = []
for i in range(N):
    a,b = map(int,input().split())
    conf.append((a,b))

conf.sort(key = lambda x: (x[1],x[0]))

result = 1
start = conf[0]
for i in range(1,N):
    if conf[i][0] >= start[1]:
        start = conf[i]
        result += 1

print(result)