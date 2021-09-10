def solution(weights, head2head):
    answer = []
    n = len(weights)
    for i in range(n):
        total, win, win_heavy = 0, 0, 0
        for j in range(n):
            if head2head[i][j] == 'N':
                continue
            if head2head[i][j] == 'W':
                if weights[i] < weights[j]:
                    win_heavy += 1
                win += 1
            total += 1
        win_rate = 0 if total == 0 else win/total
        answer.append((win_rate, win_heavy ,weights[i], i+1))
    answer.sort(key = lambda x: (-x[0], -x[1], -x[2], x[3]))
    return [x[3] for x in answer]