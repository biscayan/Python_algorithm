def solution(scores):

    n = len(scores)
    answer = ''

    for i in range(n):
        total = []
        for j in range(n):
            score = scores[j][i]
            if i == j:
                my_score = score
            total.append(score)
        total.sort()
        if total.count(my_score) == 1 and (my_score == total[0] or my_score == total[-1]):
            avg = (sum(total) - my_score) / (n-1)
        else:
            avg = sum(total) / n

        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 50:
            grade = 'D'
        else:
            grade = 'F'
        answer += grade

    return answer