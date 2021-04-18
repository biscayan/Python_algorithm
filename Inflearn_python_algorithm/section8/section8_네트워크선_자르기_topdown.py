def Cut_line(n):

    ### cut edge
    if memoization[n] != 0:
        return memoization[n]

    if n == 1 or n == 2:
        return n
    
    ### memoization
    else:
        memoization[n] = Cut_line(n-1) + Cut_line(n-2)
        return memoization[n]
    

if __name__ == '__main__':

    N = 7

    memoization = [0] * (N+1)

    print(Cut_line(N))