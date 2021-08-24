import sys

N = int(sys.stdin.readline())
people = []
for i in range(N):
    old, name = sys.stdin.readline().split()
    people.append((int(old),name,i))
people.sort(key = lambda x:(x[0],x[2]))
for person in people:
    print(person[0], person[1])