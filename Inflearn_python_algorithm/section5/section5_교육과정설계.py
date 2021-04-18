import sys
from collections import deque

sys.stdin = open('input.txt','r')

def course_plan(subjects, imp_subjects, course):

    for i in range(len(subjects)):
        if subjects[i] == imp_subjects[0]:
            imp_subjects.popleft()
            
            ###필수과목 충족 시 break
            if not imp_subjects:
                break

    if imp_subjects:
        print("#{} NO".format(course+1))

    else:
        print("#{} YES".format(course+1))
    
if __name__ == '__main__':

    ###필수과목
    imp_subject_list = list(input())

    ###test case개수
    course_num = int(input())

    for course in range(course_num):

        ###case마다 deque를 초기화
        imp_subject_deque = deque(imp_subject_list)

        subjects = list(input())

        course_plan(subjects, imp_subject_deque, course)