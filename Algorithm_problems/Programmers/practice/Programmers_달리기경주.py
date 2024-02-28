def solution(players, callings):
    dict = {}
    for i in range(len(players)):
        dict[players[i]] = i

    for call in callings:
        idx = dict[call]
        tmp = players[idx-1]
        players[idx-1] = call
        players[idx] = tmp
        dict[call] -= 1
        dict[tmp] +=1

    return players