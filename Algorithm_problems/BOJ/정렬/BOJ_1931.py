import sys

sys.stdin = open("input.txt", "r")

def assign_room(rooms):

    cur_room = rooms[0]
    cnt = 1

    for i in range(1,N):
        if rooms[i][0] >= cur_room[1]:
            cur_room = rooms[i]
            cnt += 1

    return cnt


if __name__ == '__main__':

    meeting_room = []

    N = int(sys.stdin.readline())

    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        meeting_room.append((start, end))

    meeting_room.sort(key = lambda x:(x[1], x[0]))

    print(assign_room(meeting_room))