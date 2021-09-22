# solution 1. 
# runtime : 2784ms, memory : 15.1mb
def canCompleteCircuit(gas, cost):
    n = len(gas)
    for i in range(n): 
        tank = 0
        can_travel = True
        for j in range(i, i+n):
            idx= j%n
            tank += gas[idx]
            tank -= cost[idx]
            if tank < 0:
                can_travel = False
                break
        if can_travel:
            return i
    return -1

# solution 2. 
# runtime : 40ms, memory : 15.2mb
def canCompleteCircuit(gas, cost):
    n = len(gas)
    if sum(gas) < sum(cost):
        return -1
    idx, tank = 0, 0
    for i in range(n):
        if gas[i]+tank < cost[i]:
            idx = i+1
            tank = 0
        else:
            tank += gas[i] - cost[i]
    return idx