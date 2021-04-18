def merge_sort(l_idx, r_idx):

    if l_idx < r_idx:
        
        m_idx = (l_idx + r_idx) // 2

        ### divide
        merge_sort(l_idx, m_idx)
        merge_sort(m_idx+1, r_idx)

        p1, p2 = l_idx, m_idx+1

        tmp_array = []

        ### copy
        while p1 <= m_idx and p2 <= r_idx:
            if array[p1] < array[p2]:
                tmp_array.append(array[p1])
                p1 += 1

            elif array[p1] >= array[p2]:
                tmp_array.append(array[p2])
                p2 += 1    

        ### residual
        if p1 <= m_idx:
            tmp_array = tmp_array + array[p1:m_idx+1]
        if p2 <= r_idx:
            tmp_array = tmp_array + array[p2:r_idx+1]

        ### paste
        for i in range(len(tmp_array)):
            array[l_idx+i] = tmp_array[i]


if __name__ == '__main__':

    array = [23,11,45,36,15,67,33,21]

    print("Before sorting : ", end=' ')
    print(array)

    ### sorting
    merge_sort(0, len(array)-1)

    print("After sorting : ", end=' ')
    print(array)