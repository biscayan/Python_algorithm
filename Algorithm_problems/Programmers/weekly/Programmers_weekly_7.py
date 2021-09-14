from collections import deque

def solution(enter, leave):
    n = len(enter)
    leave = deque(leave)
    in_room = []
    answer = [0] * (n+1)
    for i in range(n):
        in_room.append(enter[i])
        while leave and leave[0] in in_room:
            answer[leave[0]] += (len(in_room)-1)
            in_room.remove(leave[0])
            for j in range(len(in_room)):
                answer[in_room[j]] += 1
            leave.popleft()
    return answer[1:]