from itertools import combinations
from collections import Counter

def solution(orders, course):

    # couse has nums from 2 to 10
    course_list = [[] for _ in range(11)]
    food_combination = []
    answer = []

    for num in course:
        for order in orders:
            # can make a combination
            if len(order) >= num:
                comb_list = list(combinations(order, num))
                for comb in comb_list:
                    # delete the redundancy by sorting the alphabets
                    food_combination.append(''.join(sorted(comb)))

    for foods in food_combination:
        if len(foods) in course:
            course_list[len(foods)].append(foods)

    for course_ele in course_list:
        if course_ele != []:
            course_count = Counter(course_ele).most_common()
            most_frequent = course_count[0][1]
            for i in range(len(course_count)):
                if course_count[i][1] == most_frequent and course_count[i][1]>=2: # at least two customers
                    answer.append(course_count[i][0])
                else:
                    break

    answer.sort()

    return answer