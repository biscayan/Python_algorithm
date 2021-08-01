# 시간초과

def to_second(time):

    hour, minute, second = time.split(":")

    return int(hour) * 3600 + int(minute) * 60 + int(second)

def to_time(sec):

    sec, second = divmod(sec, 60)
    sec, minute = divmod(sec, 60)
    hour = sec

    return f'{hour:02d}:{minute:02d}:{second:02d}'

def solution(play_time, adv_time, logs):

    play_second = to_second(play_time)
    adv_second = to_second(adv_time)

    total = [0 for i in range(play_second+1)]

    for log in logs:
        start_time, end_time = log[:8], log[9:]
        start_second = to_second(start_time)
        end_second = to_second(end_time)
        total[start_second] += 1
        total[end_second] -= 1
    
    for i in range(1,len(total)):
        total[i] += total[i-1]
        
    # accumulated
    for i in range(1,len(total)):
        total[i] += total[i-1]

    max_play, max_time = total[adv_second], 0

    for start in range(1, play_second):
        if start + adv_second < play_second:
            end = start + adv_second
        else:
            end = play_second

        play = total[end] - total[start]

        if max_play < play:
            max_play = play
            max_time = start + 1
        
    answer = to_time(max_time)

    return answer