import sys
sys.stdin = open("input.txt","r")

N, M = map(int,sys.stdin.readline().split())

passenger_list = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)

boat_num = 0

while passenger_list:
    ###마지막에 1명만 남아 있을 경우
    if len(passenger_list) == 1:
        boat_num += 1
        break

    if passenger_list[0] + passenger_list[-1] <= M:
        del passenger_list[0]
        del passenger_list[-1]
        boat_num += 1
    else:
        del passenger_list[0]
        boat_num += 1
        
print(boat_num)

