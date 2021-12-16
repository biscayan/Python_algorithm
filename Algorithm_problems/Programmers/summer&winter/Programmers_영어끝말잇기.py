def solution(n, words):
    called = []
    turn = 1
    number = 0
    for word in words:
        number += 1
        if not called:
            called.append(word)
        else:
            if word in called:
                return [number, turn]
            else:
                if called[-1][-1] != word[0]:
                    return [number, turn]
                else:
                    called.append(word)
        if number == n:
            number = 0
            turn += 1
    return [0, 0]