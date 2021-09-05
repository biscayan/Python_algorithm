def solution(files):
    answer = []
    for file_name in files:
        head, number, tail = '', '', ''
        num_check = False
        for i in range(len(file_name)):
            if file_name[i].isdigit():
                number += file_name[i]
                num_check = True
            elif not num_check:
                head += file_name[i]
            else:
                tail = file_name[i:]
                break
        answer.append((head, number, tail))
    answer.sort(key = lambda x:(x[0].lower(),int(x[1])))
    return [''.join(x) for x in answer]