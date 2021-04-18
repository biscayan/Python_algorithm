def Ascend_stair(n):

    if memoization[n] != 0:
        return memoization[n]

    if n == 1 or n == 2:
        return n

    else:
        memoization[n] = Ascend_stair(n-1) + Ascend_stair(n-2)
        return memoization[n]
        
if __name__ == '__main__':

    N = 7

    memoization = [0] * (N+1)

    print(Ascend_stair(N))