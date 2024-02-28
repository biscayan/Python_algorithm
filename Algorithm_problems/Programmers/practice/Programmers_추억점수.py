def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    for pho in photo:
        score = 0
        for p in pho:
            if p in dict:
                score += dict[p]
        answer.append(score)
    return answer