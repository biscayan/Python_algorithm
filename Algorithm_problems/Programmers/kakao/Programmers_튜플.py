def solution(s):

    s = s[2:-2].split("},{")

    ans = []

    for element in s:
        element.split(",")
        ans.append(list(map(int,element.split(','))))

    ans.sort(key=len)

    answer = []

    for arr in ans:
        for num in arr:
            if num not in answer:
                answer.append(num)

    return answer


if __name__ == '__main__':

    ### test case1
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))

    ### test case2
    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
    print(solution(s))

    ### test case3
    s = "{{20,111},{111}}"
    print(solution(s))

    ### test case4
    s = "{{123}}"
    print(solution(s))

    ### test case5
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    print(solution(s))