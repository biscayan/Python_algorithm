def solution(skill,skill_trees):
    
    answer=0
    
    for skill_tree in skill_trees:
        
        skill_list=list(skill)
        
        for skill_element in skill_tree:
            if skill_element in skill:
                
                #C->B->D의 순서 탐색
                if skill_element!=skill_list.pop(0):
                    break
        else:
            #조건을 어기지 않으면 +1
            answer+=1
    
    return answer
        
if __name__=='__main__':
    
    #test case
    skill="CBD"
    skill_trees=["BACDE","CBADF","AECB","BDA"]
    
    print(solution(skill,skill_trees))
