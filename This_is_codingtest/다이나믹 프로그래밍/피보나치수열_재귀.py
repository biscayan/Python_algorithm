def fibonacci(x):
    if x == 1 or x == 2:
        return 1

    if memoization[x] != 0:
        return memoization[x]

    memoization[x] = fibonacci(x-1) + fibonacci(x-2)
    
    return memoization[x]

if __name__ == '__main__':

    memoization = [0] * 100

    print(fibonacci(99))