def count_intersum(array,m):

    count, interval_sum, end = 0, 0, 0
    n = len(array)

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += array[end]
            end += 1
        if interval_sum == m:
            count += 1
        interval_sum -= array[start]

    return count

if __name__ == '__main__':
    data = [1,2,3,2,5]
    print(count_intersum(data,5))