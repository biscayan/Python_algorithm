def fibonacci(n):

    dp_table[1] = 1
    dp_table[2] = 1

    for i in range(3, n+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    return dp_table[n]
    
if __name__ == '__main__':

    dp_table = [0]*100
    n = 99

    print(fibonacci(n))