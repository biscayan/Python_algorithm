def quick_sort(l_idx, r_idx):
    
    if l_idx < r_idx:

        position = l_idx
        pivot = array[r_idx]

        for i in range(l_idx, r_idx):
            if array[i] <= pivot:
                array[i], array[position] = array[position], array[i]
                position += 1
        
        array[r_idx], array[position] = array[position], array[r_idx]

        quick_sort(l_idx, position-1)
        quick_sort(position+1, r_idx) 


if __name__ == '__main__':

    array = [23,11,45,36,15,67,33,21,9,47]

    print("Before sorting : ", end=' ')
    print(array)

    ### sorting
    quick_sort(0, len(array)-1)

    print("After sorting : ", end=' ')
    print(array)