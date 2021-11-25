import sys
sys.stdin = open("input.txt", "r")
string = sys.stdin.readline().strip()
result = []
for i in range(len(string)):
    result.append(string[i:])
result.sort()
for sub_str in result:
    print(sub_str)