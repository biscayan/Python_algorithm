import sys

sys.stdin = open("input.txt", "r")

def kor_eng_math(array):

    ### lambda를 이용하여 순서대로 정렬
    ### +면 오름차순, -면 내림차순
    sorted_array = sorted(array, key = lambda x: (-x[1], x[2], -x[3], x[0]))

    for students in sorted_array:
        print(students[0])


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    array = []

    for _ in range(N):
        student, korean, english, math = sys.stdin.readline().split()
        array.append((student, int(korean), int(english), int(math)))

    kor_eng_math(array)