def insetion_sort(array):

    for i in range(1,len(array)):

        ### 역순으로 탐색
        for j in range(i,0,-1):

            if array[j]<array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            
            ### 앞에는 이미 정렬되어 있으므로 더 이상 탐색할 필요가 없음
            else:
                break

    return array 
    
if __name__ == '__main__':
    
    array = [5,2,7,6,9,1,3,0,4,8]
    print(insetion_sort(array))