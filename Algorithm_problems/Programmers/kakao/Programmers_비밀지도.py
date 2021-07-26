def solution(n, arr1, arr2):

    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        
        password = ''
        
        ### 값을 이진수로 바꾸고 헤더는 제거
        bin1, bin2 = bin(a1)[2:], bin(a2)[2:]

        ### 삭제된 0을 복원
        if len(bin1) < n:
            bin1 = '0'*(n-len(bin1)) + bin1
            
        if len(bin2) < n:
            bin2 = '0'*(n-len(bin2)) + bin2
        
        for i in range(n):
            if bin1[i] == '1' or bin2[i] == '1':
                password += '#'
            elif bin1[i] == '0' and bin2[i] == '0':
                password += ' '
                
        answer.append(password)
                
    return answer