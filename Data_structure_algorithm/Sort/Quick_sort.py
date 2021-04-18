def quick_sort(num_list,low,high):

    if low>=high: #base case, terminate the argorithm
        return 
    
    pivot_index=partition(num_list,low,high)
    
    quick_sort(num_list,low,pivot_index-1) #left subarray
    quick_sort(num_list,pivot_index+1,high) #right subarray

def partition(num_list,low,high):
    pivot_index=(low+high)//2 #middle index

    swap(num_list,pivot_index,high)

    index=low

    for j in range(low,high,1):
        if num_list[j]<=num_list[high]: #ascending order
        #if num_list[j]>=num_list[high]: #descending order
            swap(num_list,index,j)
            index+=1
            
    swap(num_list,index,high)

    return index

def swap(num_list,index1,index2):
    temp=num_list[index1]
    num_list[index1]=num_list[index2]
    num_list[index2]=temp

if __name__=='__main__':
    num_list=[4,-2,3,1,-5,6,0]
    quick_sort(num_list,0,len(num_list)-1)
    print(num_list)
    
        
     
