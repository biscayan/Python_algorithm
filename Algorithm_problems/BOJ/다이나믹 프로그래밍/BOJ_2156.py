import sys

sys.stdin = open("input.txt", "r")

def wine_tasting(wine_list, n):

    dp_table = [0] * n

    if n == 1:
        return wine_list[0]
    elif n == 2:
        return wine_list[0]+wine_list[1]
    elif n == 3:
        return max(wine_list[0]+wine_list[2], wine_list[1]+wine_list[2], wine_list[0]+wine_list[1])
    else:
        dp_table[0] = wine_list[0]
        dp_table[1] = wine_list[0]+wine_list[1]
        dp_table[2] = max(wine_list[0]+wine_list[2], wine_list[1]+wine_list[2], dp_table[1])

        for i in range(3,n):
            dp_table[i] = max(dp_table[i-2]+wine_list[i], # oxo 
                              dp_table[i-3]+wine_list[i-1]+wine_list[i], # oxoo
                              dp_table[i-1]) # ox

        return dp_table[n-1]

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    wine_list = []

    for _ in range(n):
        wine = int(sys.stdin.readline())
        wine_list.append(wine)

    print(wine_tasting(wine_list, n))