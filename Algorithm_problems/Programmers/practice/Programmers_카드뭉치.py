
def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1_idx, cards2_idx = 0, 0
    for i in range(len(goal)):
        if cards1_idx < len(cards1):
            if goal[i] == cards1[cards1_idx]:
                cards1_idx += 1
                continue
        if cards2_idx < len(cards2):
            if goal[i] == cards2[cards2_idx]:
                cards2_idx += 1
                continue
        answer = 'No'
        return answer
    return answer