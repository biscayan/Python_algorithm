import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def lie(know, parties):

    queue = deque(know)

    while queue:
        person = queue.popleft()
        for party in parties:
            if person in party:
                queue.extend(party)
                parties.remove(party)

    print(len(parties))

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    know_list = list(map(int, sys.stdin.readline().split()))[1:]
    party_list = []
    for _ in range(M):
        party_list.append(list(map(int, sys.stdin.readline().split()))[1:])

    if know_list == []:
        print(M)
    else:
        lie(know_list, party_list)