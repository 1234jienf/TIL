# 0921 풀이 
# 복습 한번 더 진행 필요

# 1. 풀이 (while 문 풀이)
def check(lst):
    # counter = [0] * 10
    counter = [0 for _ in range(10)]
    # babygin 이었을 때 갯수 세어주기 위해서 변수 설정
    is_babygin = 0
    # 예를 들어서 숫자 6일 들어오면 6번째 counter의 인덱스에 +1 한다.
    # 그니깐 숫자의 갯수를 세어주는 거네 .. 똑똑하노,,,
    for number in lst:
        counter[number] += 1

    idx = 0
    while idx < len(counter):
        # triplet 체크해주기
        if counter[idx] >= 3:
            # triplet 인 카드를 체크해준 후 3 장 버리기
            counter[idx] -= 3
            is_babygin += 1
        # run 체크 해주기
        # 아래에 비교해주는 idx 가 +2 이니깐 8 이전까지만..
        if idx < 8:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                # run 체크 해준 후 해당 카드 3 장 버리기
                counter[idx] -= 1
                counter[idx + 1] -= 1
                counter[idx+2] -= 1
                is_babygin += 1

        # 만약 triplet 하나 run 하나로 인해 2 가 채워지면 return 1
        if is_babygin == 2:
            return 1
        # idx 값 하나씩 더해줘서 계속 while 문으로 반복 돌리는게 ㄹㅇ...
        idx += 1

    if is_babygin != 2:
        return 0

T = int(input())

for tc in range(1,T+1):
    card_lst = list(map(int,input()))
    
    result = check(card_lst)
    if result == 1:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')


#2. 풀이
T = int(input())

for tc in range(1,T+1):
    zero_list = [0 for _ in range(10)]
    numbers = input()
    is_babygin = 0

    # 숫자 카운트 증가
    for i in numbers:
        zero_list[int(i)] += 1
    # 같은게 3개이면 +1
    for j in range(len(zero_list)):
        # 만약 전부 다 같아서 6이면 베이비진 = 2
        if zero_list[j] == 6:
            is_babygin = 2
            break
        if 3 <= zero_list[j] < 6:
            is_babygin += 1
            zero_list[j] -= 3

    # 만약 베이비진 = 2 가 아니면
    if is_babygin != 2:
        # 연속해서 있는 경우 베이비진 + 1
        for k in range(len(zero_list) -2):
            # 만약 1231232인 경우
            if zero_list[k] == 2 and zero_list[k+1] ==2 and zero_list[k+2] == 2:
                is_babygin = 2
                break
            # 아닌 경우
            if 0 < zero_list[k] and 0< zero_list[k+1] and 0< zero_list[k+2]:
                is_babygin += 1
                zero_list[k] -= 1
                zero_list[k+1] -= 1
                zero_list[k+2] -= 1

        # 베이비 진이 2 면 1 , 아니면 0 출력
        if is_babygin == 2:
            print(f'#{tc} true')
        else:
            print(f'#{tc} false')

# 3. 1,2 둘다 시간 초과 나는데 어캄?

T = int(input())
 
# 테스트 케이스만큼 반복한다
for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    # 테스트케이스 별로 6장의 카드 순서 정보를 전달 받는다. (order)
    order = list(map(int, input().strip()))  # 순회를 돌 것이기 때문에 list 변환 필요
    # 플레이어가 가지고 있는 카드 번호별 수를 나타내는 리스트를 만든다. (hand)
    hand = [0] * 10  # 각각의 인덱스가 숫자에 대응한다 (0~9)
 
    # card를 임시변수로 하는 반복문으로 order를 탐색한다.
    for card in order:
        # card를 인덱스로 가지는 hand의 요소에 +1 해준다. (숫자를 카운트한다.)
        hand[card] += 1
 
    # hand를 체크하여 베이비 진인지 검사한다.
    # Triplet 카드들을 빼준다
    for i in range(len(hand)):
        while hand[i] >= 3:
            hand[i] -= 3
    # Run 카드들을 빼준다
    for i in range(len(hand) - 2):
        while hand[i] and hand[i+1] and hand[i+2]:
            hand[i] -= 1
            hand[i+1] -= 1
            hand[i+2] -= 1
    # 베이비 진이라면? -> 모두 제거되어서 총 합이 0일 것
    is_baby_gin = not sum(hand)
    print('true' if is_baby_gin else 'false')