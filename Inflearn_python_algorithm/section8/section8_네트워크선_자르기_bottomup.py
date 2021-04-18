def Cut_line(n):

    dp_table = [0] * (n+1)

    dp_table[1] = 1
    dp_table[2] = 2

    for i in range(3,n+1):
        dp_table[i] = dp_table[i-2] + dp_table[i-1]
    
    result = dp_table[n]

    return result

if __name__ == '__main__':

    N = 7

    print(Cut_line(N))