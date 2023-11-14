T = int(input())


def dfs(month, acc_cost):
    global ans

    if acc_cost > ans:
        return
    
    # 기저 조건
    if month > 12:
        ans = min(ans,acc_cost)
        return
    
    # 1일 이용권으로 모두 구입
    dfs(month+1, acc_cost+ (months[month] * cost_day))

    # 1달 이용권 구입
    dfs(month+1,acc_cost+cost_month)

    # 3달 이용권 구입
    dfs(month+3, acc_cost+ cost_month3)
