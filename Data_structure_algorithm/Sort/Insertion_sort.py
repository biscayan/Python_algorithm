def insertion_sort(num_list):
    for i in range(len(num_list)):
        j=i
        while j>0 and num_list[j-1]>num_list[j]: #lots of shifts between items
            num_list[j],num_list[j-1]=num_list[j-1],num_list[j]
            j=j-1
    return num_list

if __name__=='__main__':
    a=[1,5,3,8,10,-2,4]
    print(insertion_sort(a))
            
