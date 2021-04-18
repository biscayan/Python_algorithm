def solution(arr):
    num=0
    for i in range(len(arr)):
        num+=arr[i]
    answer=num/len(arr)
        
    return answer

if __name__=='__main__':
    #test case1
    arr=[1,2,3,4]
    print(solution(arr))

    #test case2
    arr=[5,5]
    print(solution(arr))
