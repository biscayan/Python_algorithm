import sys

sys.stdin = open("input.txt","r")

def plus_cycle(num):

    count = 0

    new_num = num

    while True:

        if len(new_num) == 1:
            new_num = "0"+new_num

        num_sum = str(int(new_num[0]) + int(new_num[1]))

        new_num = new_num[1] + num_sum[-1]

        count += 1

        if len(num) == 1:
            if "0"+num == new_num:
                break
        else:
            if num == new_num:
                break

    return count
        

if __name__ == '__main__':

    input_num = sys.stdin.readline().strip()

    print(plus_cycle(input_num))