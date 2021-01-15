import sys

sys.stdin = open("input.txt", "r")

def line_up(array):

    inc_array = sorted(array)
    desc_array = sorted(array, reverse = True)

    if array == inc_array:
        print("INCREASING")
    elif array == desc_array:
        print("DECREASING")
    elif array != inc_array and array != desc_array:
        print("NEITHER")

if __name__ == '__main__':

    N = int(sys.stdin.readline())

    array = []

    for i in range(N):
        person = sys.stdin.readline().strip()
        array.append(person)

    line_up(array)
