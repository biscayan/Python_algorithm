import sys

sys.stdin = open("input.txt", "r")

def change_money(n):
    change = 1000-n
    money_list = [500, 100, 50, 10, 5, 1]
    count = 0
    for i in money_list:
        count += change // i
        change %= i
    return count

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print(change_money(N))