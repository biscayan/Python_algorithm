def ugly_num(n):

    dp_table = [0] * (n+1)

    ### 2의 배수, 3의 배수, 5의 배수 인덱스
    i2, i3, i5 = 1, 1, 1

    ### 2의 배수, 3의 배수, 5의 배수 값
    n2, n3, n5 = 2, 3, 5

    dp_table[1] = 1

    for i in range(2, n+1):
        
        dp_table[i] = min(n2, n3, n5)

        if dp_table[i] == n2:

            i2 += 1
            n2 = dp_table[i2] * 2

        if dp_table[i] == n3:
            i3 += 1
            n3 = dp_table[i3] * 3

        if dp_table[i] == n5:
            i5 += 1
            n5 = dp_table[i5] * 5

    result = dp_table[n]

    return result


if __name__ == '__main__':

    N = 10

    print(ugly_num(N))