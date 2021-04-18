def solution(bridge_length,weight,truck_weights):
    
    answer=0 #time
    current_weight=0
    
    ongoing=[0]*bridge_length

    while truck_weights: #while the array is not empty
        
        answer+=1 #time goes
        
        current_weight=current_weight-ongoing.pop(0)

        if (current_weight+truck_weights[0])<=weight: #weight=threshold
            departure=truck_weights.pop(0)
            ongoing.append(departure)
            current_weight+=departure
        else:
            ongoing.append(0)
            
    while current_weight!=0: #the last truck is still on the bridge
        
        answer+=1 #time goes
        
        current_weight=current_weight-ongoing.pop(0)
        
    return answer

if __name__=='__main__':
    #test case1
    bridge_length=2
    weight=10
    truck_weights=[7,4,5,6]
    print(solution(bridge_length,weight,truck_weights))

    #test case2
    bridge_length=100
    weight=100
    truck_weights=[10]
    print(solution(bridge_length,weight,truck_weights))

    #test case3
    bridge_length=100
    weight=100
    truck_weights=[10,10,10,10,10,10,10,10,10,10]
    print(solution(bridge_length,weight,truck_weights))

    
