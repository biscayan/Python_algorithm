def selection_sort(num_list):
    for i in range(len(num_list)-1):

        index=i

        for j in range(i+1,len(num_list),1):
            if num_list[j]<num_list[index]:
                index=j

        if index!=i:
            num_list[index],num_list[i]=num_list[i],num_list[index] #swap

    return num_list

if __name__=='__main__':
    a=[-3,2,6,4,8,1]
    print(selection_sort(a))
    

                                                     
