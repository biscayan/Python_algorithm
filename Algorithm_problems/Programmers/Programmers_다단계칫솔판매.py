def solution(enroll, referral, seller, amount):

    tree = {}
    profit = {}
    answer = []

    for i in range(len(enroll)):
        tree[enroll[i]] = referral[i]
        profit[enroll[i]] = 0
    
    for i in range(len(seller)):
        child_node = seller[i]
        money = amount[i] * 100
        # 추천인이 없을 때까지 반복해서 수익을 나눔
        while child_node != '-':
            parent_node = tree[child_node]
            div = money//10
            # 몫이 원 단위일 경우
            if div == 0:
                profit[child_node] += money
                break
            profit[child_node] += money - div
            money = div
            child_node = parent_node

    for key,value in profit.items():
        answer.append(value)

    return answer