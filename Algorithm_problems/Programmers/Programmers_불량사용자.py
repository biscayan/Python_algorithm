from itertools import permutations

def id_match(cand_id, ban_id):
    for i in range(len(ban_id)):
        if ban_id[i] == '*':
            continue
        if ban_id[i] != cand_id[i]:
            return False
        
    return True


def check_id(candidate, banned_id):
    
    for i in range(len(banned_id)):
        if len(candidate[i]) != len(banned_id[i]):
            return False
        if id_match(candidate[i], banned_id[i]) == False:
            return False
        
    return True


def solution(user_id, banned_id):
    
    cases = []
    
    ### banned될 수 있는 모든 경우의 순열을 생성
    banned_candidate = list(permutations(user_id, len(banned_id)))
    
    for candidate in banned_candidate:
        
        if check_id(candidate, banned_id) == True:

            candidate = list(candidate)
            candidate.sort()
            
            if candidate not in cases:
                cases.append(candidate)
                
    answer = len(cases)
    
    return answer