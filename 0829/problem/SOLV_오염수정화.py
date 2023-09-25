N = int(input())

arr = list(map(int,input().split()))
ans = 1e9
tmp = []
sum1 = 0
lst = []

def clean(idx,tmp,):
    global arr,ans,sum1,lst
    if len(tmp) == 2:
        if abs(sum(tmp) - 0) < ans:
            ans = abs(sum(tmp))
            lst = tmp[ : ]
        elif abs(sum(tmp) - 0) == ans:
            if abs(tmp[0] + tmp[1]) > sum1:
                ans = abs(sum(tmp))
                sum1 = abs(tmp[0] + tmp[1])
                lst = tmp[ : ]
        return lst
    if idx == N:
        return lst
    tmp.append(arr[idx])
    clean(idx+1,tmp)
    tmp.remove(arr[idx])
    clean(idx+1,tmp)


clean(0,tmp)
print(lst[0],lst[1])