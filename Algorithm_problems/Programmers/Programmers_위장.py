def solution(clothes):

    cloth_dict = {}
    answer = 1
    
    for cloth in clothes:

        cloth_name = cloth[0] #value
        cloth_type = cloth[1] #key

        if cloth_type in cloth_dict:
            cloth_dict[cloth_type].append(cloth_name)
        else:
            cloth_dict[cloth_type] = [cloth_name]

    #print(cloth_dict)

    for key in cloth_dict.keys():
        answer *= len(cloth_dict[key])+1

    #아무것도 안입은 경우의 수는 제외
    return answer-1
            

    
if __name__=='__main__':
    #test case1
    clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))
 
    #test case2
    clothes=[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(clothes))
