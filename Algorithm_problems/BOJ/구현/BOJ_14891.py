import sys

sys.stdin = open("input.txt", "r")

def rotate_wheel(rotate_list):
    for wheel_num, direction in rotate_list:

        clock, counter_clock = [], []

        if wheel_num == 1:
            if direction == 1:
                clock.append(wheel1)
                if wheel1[2] != wheel2[6]:
                    counter_clock.append(wheel2)
                    if wheel2[2] != wheel3[6]:
                        clock.append(wheel3)
                        if wheel3[2] != wheel4[6]:
                            counter_clock.append(wheel4)
            elif direction == -1:
                counter_clock.append(wheel1)
                if wheel1[2] != wheel2[6]:
                    clock.append(wheel2)
                    if wheel2[2] != wheel3[6]:
                        counter_clock.append(wheel3)
                        if wheel3[2] != wheel4[6]:
                            clock.append(wheel4)

        elif wheel_num == 2:
            if direction == 1:
                clock.append(wheel2)
                if wheel2[6] != wheel1[2]:
                    counter_clock.append(wheel1)
                if wheel2[2] != wheel3[6]:
                    counter_clock.append(wheel3)
                    if wheel3[2] != wheel4[6]:
                        clock.append(wheel4)
            elif direction == -1:
                counter_clock.append(wheel2)
                if wheel2[6] != wheel1[2]:
                    clock.append(wheel1)
                if wheel2[2] != wheel3[6]:
                    clock.append(wheel3)
                    if wheel3[2] != wheel4[6]:
                        counter_clock.append(wheel4)

        elif wheel_num == 3:
            if direction == 1:
                clock.append(wheel3)
                if wheel3[6] != wheel2[2]:
                    counter_clock.append(wheel2)
                    if wheel2[6] != wheel1[2]:
                        clock.append(wheel1)
                if wheel3[2] != wheel4[6]:
                    counter_clock.append(wheel4)
            elif direction == -1:
                counter_clock.append(wheel3)
                if wheel3[6] != wheel2[2]:
                    clock.append(wheel2)
                    if wheel2[6] != wheel1[2]:
                        counter_clock.append(wheel1)
                if wheel3[2] != wheel4[6]:
                    clock.append(wheel4)

        elif wheel_num == 4:
            if direction == 1:
                clock.append(wheel4)
                if wheel4[6] != wheel3[2]:
                    counter_clock.append(wheel3)
                    if wheel3[6] != wheel2[2]:
                        clock.append(wheel2)
                        if wheel2[6] != wheel1[2]:
                            counter_clock.append(wheel1)
            elif direction == -1:
                counter_clock.append(wheel4)
                if wheel4[6] != wheel3[2]:
                    clock.append(wheel3)
                    if wheel3[6] != wheel2[2]:
                        counter_clock.append(wheel2)
                        if wheel2[6] != wheel1[2]:
                            clock.append(wheel1)
        # rotation
        for wheel in clock:
            popped = wheel.pop()
            wheel.insert(0,popped)
        for wheel in counter_clock:
            popped = wheel.pop(0)
            wheel.append(popped)

    score = 0
    if wheel1[0] == 1:
        score += 1
    if wheel2[0] == 1:
        score += 2
    if wheel3[0] == 1:
        score += 4
    if wheel4[0] == 1:
        score += 8

    return score

if __name__ == '__main__':
    wheel1 = list(map(int, sys.stdin.readline().strip()))
    wheel2 = list(map(int, sys.stdin.readline().strip()))
    wheel3 = list(map(int, sys.stdin.readline().strip()))
    wheel4 = list(map(int, sys.stdin.readline().strip()))

    K = int(sys.stdin.readline())
    rotate_list = []

    for _ in range(K):
        wheel_num, direction = map(int, sys.stdin.readline().split())
        rotate_list.append((wheel_num, direction))

    print(rotate_wheel(rotate_list))