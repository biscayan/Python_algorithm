import sys
from collections import deque

sys.stdin = open('input.txt','r')
N, M = map(int, sys.stdin.readline().split())

###index,value의 튜플 쌍으로 리스트를 생성
patient_list = [(idx, val) for idx, val in enumerate(list(map(int, sys.stdin.readline().split())))]
patient_deque = deque(patient_list)

answer = 0

while True:

    patient = patient_deque.popleft()

    ###현재의 patient가 뒤의 patient들보다 위험도가 작으면
    if any(patient[1] < x[1] for x in patient_deque):
        patient_deque.append(patient)

    else:
        answer += 1
        if patient[0] == M:
            break

print(answer)