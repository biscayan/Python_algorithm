import sys
sys.stdin=open('input.txt','r')

card_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for _ in range(10):
        
    a,b,=map(int,input().split())

    #swap
    for _ in range((b-a+1)//2):
        card_list[a-1],card_list[b-1]=card_list[b-1],card_list[a-1]
        a+=1
        b-=1

#프린트 방법1
print(' '.join(map(str,card_list)))

#프린트 방법2
for card in card_list:
    print(card,end=' ')
