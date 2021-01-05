def count_sort(array, count):

    for i in range(len(array)):
        count[array[i]]+= 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


if __name__ == '__main__':

    array = [3,6,4,7,9,2,1,5,7,0,2,3,5,6,8]
    
    count_list = [0] * (max(array)+1)

    count_sort(array,count_list)