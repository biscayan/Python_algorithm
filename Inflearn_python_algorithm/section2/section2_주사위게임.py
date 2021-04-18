import sys
sys.stdin=open('input.txt','r')

def dice_game(dice_list):
    ### Rule1
    if dice_list[0]==dice_list[1]==dice_list[2]:
        money1=10000+dice_list[0]*1000
        return money1

    ### Rule2
    elif dice_list[0]==dice_list[1]!=dice_list[2]:
        money2_1=1000+dice_list[0]*100
        return money2_1
    elif dice_list[0]==dice_list[2]!=dice_list[1]:
        money2_2=1000+dice_list[0]*100
        return money2_2
    elif dice_list[1]==dice_list[2]!=dice_list[0]:
        money2_3=1000+dice_list[1]*100
        return money2_3

    ###Rule3
    elif dice_list[0]!=dice_list[1]!=dice_list[2]:
        money3=max(dice_list)*100
        return money3

        
if __name__=='__main__':
    N=int(input())
    result=0
    for test_case in range(N):
        dice_list=list(map(int,input().split()))
        
        money=dice_game(dice_list)
        if money>result:
            result=money
    print(result)
