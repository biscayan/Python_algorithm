def bubble_sort(num_list):
    for i in range(len(num_list)-1):
        for j in range(0,len(num_list)-1,1):
            if num_list[j]>num_list[j+1]:
                num_list[j],num_list[j+1]=num_list[j+1],num_list[j] #swap
    return num_list

if __name__=='__main__':
    a=[1,5,3,2,4,8,7]
    print(bubble_sort(a))

