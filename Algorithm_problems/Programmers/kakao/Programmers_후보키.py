from itertools import combinations

def solution(relation):
    row, col = len(relation), len(relation[0])
    combination = []
    for i in range(1,col+1):
        comb = list(combinations(range(col), i))
        combination.extend(comb)

    # uniqueness
    keys = []
    for tup in combination:
        tmp_arr = ['' for _ in range(row)]
        for idx in list(tup):
            for i, rel in enumerate(relation):
                tmp_arr[i] += rel[idx]
        if len(set(tmp_arr)) == row:
            keys.append(set(tup))

    # minimality
    remove = []
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
            if keys[i].issubset(keys[j]):
                if keys[j] not in remove:
                    remove.append(keys[j])

    return len(keys) - len(remove)