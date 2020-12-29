import sys

sys.stdin = open('input.txt','r')

N, M = map(int,input().split())

never_seen_heard_dict = {}
never_seen_heard_list = []

###never heard (듣도 못한)
for _ in range(N):
    
    never_heard = input()
    
    if never_heard in never_seen_heard_dict:
        never_seen_heard_dict[never_heard] += 1
    else:
        never_seen_heard_dict[never_heard] = 1

###never seen (보도 못한)
for _ in range(M):
    
    never_seen = input()
    
    if never_seen in never_seen_heard_dict:
        never_seen_heard_dict[never_seen] += 1
    else:
        never_seen_heard_dict[never_seen] = 1
        
#print(never_seen_heard_dict)

###듣보잡 저장 
for person in never_seen_heard_dict.keys():
    if never_seen_heard_dict[person] == 2:
        never_seen_heard_list.append(person)

###듣보잡을 알파벳 순으로 정렬
never_seen_heard_list = sorted(never_seen_heard_list)

###듣보잡 수
print(len(never_seen_heard_list))

###듣보잡 이름
for _ in range(len(never_seen_heard_list)):
    print(never_seen_heard_list.pop(0))
