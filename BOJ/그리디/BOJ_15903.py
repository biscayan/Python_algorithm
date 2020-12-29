import sys
import heapq

sys.stdin =  open("input.txt", "r")

def card_game(cards):
    
    global m

    heapq.heapify(cards)
    
    while m != 0:
    
        popped1 = heapq.heappop(cards)
        popped2 = heapq.heappop(cards)

        ###두 장의 카드를 합체
        new_element = popped1 + popped2

        heapq.heappush(cards, new_element)
        heapq.heappush(cards, new_element)

        m-=1

    result = sum(cards)

    return result

if __name__ == '__main__':

    n, m = map(int, sys.stdin.readline().split())
    card_list =list(map(int, sys.stdin.readline().split())) 

    print(card_game(card_list))