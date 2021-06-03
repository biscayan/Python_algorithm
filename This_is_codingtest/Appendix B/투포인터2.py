def union(arr1, arr2):

    n, m = len(arr1), len(arr2)
    i,j = 0, 0
    result = []

    while i < n or j < m:
        if j >= m or (i < n and arr1[i] <= arr2[j]):
            if arr1[i] != arr2[j]:
                result.append(arr1[i]) 
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    return result

if __name__ == '__main__':
    array1 = [1,3,4,5,7,8,9]
    array2 = [2,4,6,8,9,10]

    print(union(array1, array2))
