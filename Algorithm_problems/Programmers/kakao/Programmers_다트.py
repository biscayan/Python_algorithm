def solution(dartResult):

    nums = []
    idx = -1

    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            if dartResult[i-1] == '0':
                ### 10점
                if dartResult[i-2] == '1':
                    num = dartResult[i-2] + dartResult[i-1]
                ### 0점
                else:
                    num = dartResult[i-1]
            ### 1~9점
            else:
                num = dartResult[i-1]

            nums.append(int(num))
            idx += 1

        elif dartResult[i] == 'D':
            if dartResult[i-1] == '0':
                if dartResult[i-2] == '1':
                    num = dartResult[i-2] + dartResult[i-1]
                else:
                    num = dartResult[i-1]
            else:
                num = dartResult[i-1]

            nums.append(pow(int(num),2))
            idx += 1

        elif dartResult[i] == 'T':
            if dartResult[i-1] == '0':
                if dartResult[i-2] == '1':
                    num = dartResult[i-2] + dartResult[i-1]
                else:
                    num = dartResult[i-1]
            else:
                num = dartResult[i-1]

            nums.append(pow(int(num),3))
            idx += 1
        
        elif dartResult[i] == '*':
            if idx == 0:
                nums[idx] *= 2
            else:
                nums[idx] *= 2
                nums[idx-1] *= 2

        elif dartResult[i] == '#':
            nums[idx] = -nums[idx]

    answer = sum(nums)
        
    return answer


if __name__ == '__main__':

    ### test cases
    dartResult = '1S2D*3T'	
    print(solution(dartResult))

    dartResult = '1D2S#10S'
    print(solution(dartResult))

    dartResult = '1D2S0T'
    print(solution(dartResult))

    dartResult = '1S*2T*3S'	
    print(solution(dartResult))

    dartResult = '1D#2S*3S'	
    print(solution(dartResult))

    dartResult = '1T2D3D#'
    print(solution(dartResult))

    dartResult = '1D2S3T*'
    print(solution(dartResult))
