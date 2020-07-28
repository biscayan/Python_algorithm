def solution(seoul):
    location=seoul.index("Kim")
    answer = '김서방은 '+str(location)+'에 있다'
    return answer

print(solution(['Jane', 'Kim']))
