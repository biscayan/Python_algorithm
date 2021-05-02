def solution(record):

    ID_name_dict = {}
    answer = []
    
    ### name 변경
    for case in record:

        case = case.split(' ')

        if case[0] in ['Enter', 'Change']:
            ID_name_dict[case[1]] = case[2]     
    
    ### result에 message 기록
    for case in record:

        case = case.split(' ')

        if case[0] == 'Enter':
            message = f'{ID_name_dict[case[1]]}님이 들어왔습니다.'
            answer.append(message)
        elif case[0] == 'Leave':
            message = f'{ID_name_dict[case[1]]}님이 나갔습니다.'
            answer.append(message)

    return answer


if __name__ == '__main__':

    ### test case
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))