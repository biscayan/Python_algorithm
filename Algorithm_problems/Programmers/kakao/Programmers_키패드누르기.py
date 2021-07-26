def get_distance(hand, target):

    ### 핸드폰 자판의 위치를 딕셔너리로 저장
    phone = {'1':(0,0), '2':(0,1), '3':(0,2),
             '4':(1,0), '5':(1,1), '6':(1,2),
             '7':(2,0), '8':(2,1), '9':(2,2),
             '*':(3,0), '0':(3,1), '#':(3,2)}

    hand, target = str(hand), str(target)

    hand_x, hand_y = phone[hand]
    target_x, target_y = phone[target]

    distance = abs(hand_x - target_x) + abs(hand_y - target_y)

    return distance


def solution(numbers, hand):

    answer = ''

    lhand, rhand = '*', '#'

    for num in numbers:
        if num in [1,4,7]:

            answer +=  'L'
            lhand = num

        elif num in [3,6,9]:

            answer += 'R'
            rhand = num

        elif num in [2,5,8,0]:

            lhand_distance = get_distance(lhand, num)
            rhand_distance = get_distance(rhand, num)

            if lhand_distance > rhand_distance:
                answer += 'R'
                rhand = num
            elif lhand_distance < rhand_distance:
                answer +=  'L'
                lhand = num
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = num
                else:
                    answer += 'R'
                    rhand = num

    return answer


if __name__ == '__main__':

    ### test case
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
    hand = "right"

    print(solution(numbers, hand))