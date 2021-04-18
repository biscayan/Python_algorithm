def Cross_bridge(n):

    dp_table = [0] * (n+2)

    dp_table[1], dp_table[2] = 1, 2

    for i in range(3,n+2):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    result = dp_table[n+1]

    print(result)

    
if __name__ == '__main__':

    N = 7

    Cross_bridge(N)
