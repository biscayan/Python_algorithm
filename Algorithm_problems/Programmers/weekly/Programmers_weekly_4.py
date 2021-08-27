def solution(table, languages, preference):
    result = []
    for job in table:
        works = job.split(' ')
        score = 0
        for i, lang in enumerate(works[::-1]):
            for j in range(len(languages)):
                if lang == languages[j]:
                    score += (preference[j] * (i+1))
                    break
        result.append((score,works[0]))
    result.sort(key = lambda x: (-x[0],x[1]))
    return result[0][1]