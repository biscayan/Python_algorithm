def make_one(n):

    for i in range(2, n+1):
        
        ### calculation 1. 1을 뺀다.
        dp_table[i] = dp_table[i-1] + 1
       
        ### calculation 2. 2로 나누어 떨어지면 2로 나눈다.
        if i % 2 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i//2] + 1)

        ### calculation 3. 3으로 나누어 떨어지면 3으로 나눈다.
        if i % 3 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i//3] + 1)

        ### calculation 4. 5로 나누어 떨어지면 5로 나눈다.
        if i % 5 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i//5] + 1)

    result = dp_table[n]

    return result

if __name__ == '__main__':

    x = 26
    dp_table = [0] * 30001

    print(make_one(x))