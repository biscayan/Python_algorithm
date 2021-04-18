def selection_sort(array):

    for i in range(len(array)):
        
        min_index = i

        for j in range(i+1,len(array)):
            
            if array[j]<array[min_index]:
                ### min index 정보를 update
                min_index = j

        ### swapping        
        array[i], array[min_index] = array[min_index], array[i]

    return array

if __name__ == '__main__':

    array = [3,0,1,5,4,6,7,9,2,8]
    print(selection_sort(array))