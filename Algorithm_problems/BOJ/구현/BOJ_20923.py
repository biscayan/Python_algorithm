### Cpython은 실패 pypy로는 통과

from collections import deque
import sys

sys.stdin = open("input.txt", "r")

def halli_galli(do_cards, su_cards):

    global M

    do_ground, su_ground = [], []
    do_deque, su_deque = deque(do_cards), deque(su_cards)

    ### 0->do's turn / 1->su's turn
    flag = 0

    while M > 0:

        ### do's turn
        if flag == 0:

            card = do_deque.pop()
            do_ground.append(card)

            if not do_deque:
                break

            ### do's bell
            if do_ground[-1] == 5:
                do_deque.extendleft(su_ground)
                do_deque.extendleft(do_ground)
                do_ground, su_ground = [], []

            ### su's bell
            elif len(su_ground) >= 1:
                if do_ground[-1] + su_ground[-1] == 5:
                    su_deque.extendleft(do_ground)
                    su_deque.extendleft(su_ground)
                    do_ground, su_ground = [], []

            M-=1
            
            if M == 0:
                break

        flag = 1

        ### su's turn
        if flag == 1:
            card = su_deque.pop()
            su_ground.append(card)

            if not su_deque:
                break
            
            ### do's bell
            if su_ground[-1] == 5:
                do_deque.extendleft(su_ground)
                do_deque.extendleft(do_ground)
                do_ground, su_ground = [], []

            ### su's bell
            elif len(do_ground) >= 1:
                if su_ground[-1] + do_ground[-1] == 5:
                    su_deque.extendleft(do_ground)
                    su_deque.extendleft(su_ground)
                    do_ground, su_ground = [], []

            M-=1

        flag = 0

    if len(do_deque) == len(su_deque):
        print("dosu")
    elif len(do_deque) > len(su_deque):
        print("do")
    elif len(do_deque) < len(su_deque):
        print("su")
        

if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    do_cards = []
    su_cards = []

    for _ in range(N):

        do, su = map(int, sys.stdin.readline().split())
        do_cards.append(do)
        su_cards.append(su)

    halli_galli(do_cards, su_cards)