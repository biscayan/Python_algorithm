def merge_sort(num_list):

    if len(num_list)==1: #there exists only a single element
        return
    
    ###divide part###
    
    middle_index=len(num_list)//2
    
    left_half=num_list[:middle_index] #left subarray
    right_half=num_list[middle_index:] #right subarray

    merge_sort(left_half)
    merge_sort(right_half)

    ###conquer part###
    
    i,j,k=0,0,0 #i->index of left subarray j->index of right subarray k->index of result array

    while i<len(left_half) and j<len(right_half):
        if left_half[i]<right_half[j]:
            num_list[k]=left_half[i]
            i+=1

        else:
            num_list[k]=right_half[j]
            j+=1

        k+=1

    while i<len(left_half):
        num_list[k]=left_half[i]
        i+=1
        k+=1

    while j<len(right_half):
        num_list[k]=right_half[j]
        j+=1
        k+=1

if __name__=='__main__':
    a=[1,0,2,-1,3,4,-5]
    merge_sort(a)
    print(a)

        
